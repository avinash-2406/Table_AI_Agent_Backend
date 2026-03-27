import os
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))

print("DEBUG KEY:", os.getenv("GOOGLE_API_KEY"))  # temporary check

ALLOWED_GROUPS = [
    "identity",
    "investment",
    "livability",
    "connectivity",
    "developer_quality",
    "ranking",
]

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a query planner for a real-estate comparable table system.

Return ONLY valid JSON.

Choose attribute_groups only from:
["identity", "investment", "livability", "connectivity", "developer_quality", "ranking"]

Output keys:
intent, comparison_mode, attribute_groups, filters, reasoning_summary

Do not invent new keys.
"""),
    ("human", "User query: {query}")
])

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

def parse_query_to_plan(query: str) -> dict:
    chain = prompt | llm
    response = chain.invoke({"query": query})
    text = response.content.strip()

    # Basic cleanup if model wraps JSON in markdown
    text = text.replace("```json", "").replace("```", "").strip()
    data = json.loads(text)

    # Safety validation
    groups = data.get("attribute_groups", [])
    data["attribute_groups"] = [g for g in groups if g in ALLOWED_GROUPS]

    if "identity" not in data["attribute_groups"]:
        data["attribute_groups"].insert(0, "identity")
    if "ranking" not in data["attribute_groups"]:
        data["attribute_groups"].append("ranking")

    return data