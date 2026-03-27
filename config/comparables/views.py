# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from comparables.graphs.table_agent_graph import table_agent_graph

# class GenerateComparisonTableView(APIView):
#     def post(self, request):
#         query = request.data.get("query", "").strip()

#         if not query:
#             return Response(
#                 {"error": "Query is required"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         result = table_agent_graph.invoke({
#             "user_query": query
#         })

#         return Response(result["final_response"], status=status.HTTP_200_OK)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from comparables.services.agent_service import run_table_agent


class GenerateComparisonTableView(APIView):
    def post(self, request):
        query = request.data.get("query", "").strip()

        if not query:
            return Response(
                {"error": "Query is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        result = run_table_agent(query)
        return Response(result, status=status.HTTP_200_OK)