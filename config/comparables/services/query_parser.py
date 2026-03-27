# import os
# import json
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv

# load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))

# print("DEBUG KEY:", os.getenv("GOOGLE_API_KEY"))  # temporary check

# ALLOWED_GROUPS = [
#     "identity",
#     "investment",
#     "livability",
#     "connectivity",
#     "developer_quality",
#     "ranking",
# ]

# prompt = ChatPromptTemplate.from_messages([
#     ("system", """
# You are a query planner for a real-estate comparable table system.

# Return ONLY valid JSON.

# Choose attribute_groups only from:
# ["identity", "investment", "livability", "connectivity", "developer_quality", "ranking"]

# Output keys:
# intent, comparison_mode, attribute_groups, filters, reasoning_summary

# Do not invent new keys.
# """),
#     ("human", "User query: {query}")
# ])

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=os.getenv("GOOGLE_API_KEY"),
# )

# def parse_query_to_plan(query: str) -> dict:
#     chain = prompt | llm
#     response = chain.invoke({"query": query})
#     text = response.content.strip()

#     # Basic cleanup if model wraps JSON in markdown
#     text = text.replace("```json", "").replace("```", "").strip()
#     data = json.loads(text)

#     # Safety validation
#     groups = data.get("attribute_groups", [])
#     data["attribute_groups"] = [g for g in groups if g in ALLOWED_GROUPS]

#     if "identity" not in data["attribute_groups"]:
#         data["attribute_groups"].insert(0, "identity")
#     if "ranking" not in data["attribute_groups"]:
#         data["attribute_groups"].append("ranking")

#     return data

import os
import json
from typing import Dict, Any, List
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from comparables.services.column_registry import get_registry_keys

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))


PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert planning agent for a real-estate dynamic table generation system.

Your job is:
1. Understand the user's query.
2. Identify the real analysis goal.
3. Detect the target metric if any.
4. Identify the business factors needed to answer the query.
5. Extract filters if explicitly mentioned.
6. Suggest comparison mode.
7. Return ONLY valid JSON.

Available output keys:
- intent
- analysis_goal
- target_metric
- comparison_mode
- factor_hypotheses
- filters
- reasoning_summary

Rules:
- factor_hypotheses must be a list of plain business factors, not technical database names.
- target_metric should be one short value like: irr, roi, yield, living_quality, pricing_analysis, generic
- comparison_mode should be one short value like: investment, living_quality, financial, pricing, generic
- filters must be a JSON object
- Do not return markdown
- Do not return explanations outside JSON
"""
    ),
    (
        "human",
        """
User query: {query}

Available registry columns:
{available_columns}
"""
    ),
])


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)


def _safe_json_loads(text: str) -> Dict[str, Any]:
    cleaned = text.strip().replace("```json", "").replace("```", "").strip()
    return json.loads(cleaned)


def _fallback_plan(query: str) -> Dict[str, Any]:
    q = query.lower()

    target_metric = "generic"
    comparison_mode = "generic"
    factors: List[str] = ["project identity", "location", "configuration", "size"]

    if "irr" in q:
        target_metric = "irr"
        comparison_mode = "financial"
        factors = [
            "sales revenue",
            "land cost",
            "construction cost",
            "finance cost",
            "sales velocity",
            "cash flow timing",
            "exit value",
            "approval delay",
        ]
    elif "roi" in q:
        target_metric = "roi"
        comparison_mode = "financial"
        factors = [
            "revenue",
            "cost",
            "finance cost",
            "sales velocity",
            "pricing",
        ]
    elif "yield" in q or "rental" in q:
        target_metric = "yield"
        comparison_mode = "investment"
        factors = [
            "rental yield",
            "pricing",
            "location",
            "configuration",
        ]
    elif "living" in q or "quality" in q or "preference" in q or "amenities" in q:
        target_metric = "living_quality"
        comparison_mode = "living_quality"
        factors = [
            "amenities",
            "safety",
            "connectivity",
            "developer quality",
            "location",
        ]
    elif "price" in q or "rate" in q:
        target_metric = "pricing_analysis"
        comparison_mode = "pricing"
        factors = [
            "pricing",
            "area",
            "location",
            "configuration",
            "transaction date",
        ]

    return {
        "intent": "table_generation",
        "analysis_goal": f"Generate a table for query: {query}",
        "target_metric": target_metric,
        "comparison_mode": comparison_mode,
        "factor_hypotheses": factors,
        "filters": {},
        "reasoning_summary": "Fallback planner used because model output was unavailable or invalid.",
    }


def parse_query_to_plan(query: str) -> Dict[str, Any]:
    chain = PROMPT | llm

    try:
        response = chain.invoke({
            "query": query,
            "available_columns": ", ".join(get_registry_keys()),
        })
        data = _safe_json_loads(response.content)

        data.setdefault("intent", "table_generation")
        data.setdefault("analysis_goal", f"Generate a table for query: {query}")
        data.setdefault("target_metric", "generic")
        data.setdefault("comparison_mode", "generic")
        data.setdefault("factor_hypotheses", [])
        data.setdefault("filters", {})
        data.setdefault("reasoning_summary", "")

        if not isinstance(data["factor_hypotheses"], list):
            data["factor_hypotheses"] = []

        if not isinstance(data["filters"], dict):
            data["filters"] = {}

        return data

    except Exception:
        return _fallback_plan(query)