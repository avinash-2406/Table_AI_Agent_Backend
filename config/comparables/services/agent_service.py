# from comparables.graphs.table_agent_graph import table_agent_graph


# def run_table_agent(user_query: str) -> dict:
#     """
#     Main entry point for the dynamic table agent.

#     Input:
#         user_query: raw query from frontend user

#     Output:
#         final response dict containing:
#         - title
#         - query_plan
#         - columns
#         - rows
#     """
#     try:
#         initial_state = {
#             "user_query": user_query
#         }

#         result = table_agent_graph.invoke(initial_state)

#         return result.get("final_response", {
#             "title": "No response generated",
#             "query_plan": {},
#             "columns": [],
#             "rows": []
#         })

#     except Exception as e:
#         return {
#             "title": "Error while generating table",
#             "query_plan": {},
#             "columns": [],
#             "rows": [],
#             "error": str(e)
#         }

from comparables.graphs.table_agent_graph import table_agent_graph


def run_table_agent(user_query: str) -> dict:
    try:
        result = table_agent_graph.invoke({"user_query": user_query})
        return result.get(
            "final_response",
            {
                "title": "No response generated",
                "response_type": "text",
                "query_plan": {},
                "answer": "The system could not generate a response.",
                "columns": [],
                "rows": [],
            },
        )
    except Exception as exc:
        return {
            "title": "Error while generating response",
            "response_type": "text",
            "query_plan": {},
            "answer": str(exc),
            "columns": [],
            "rows": [],
        }
