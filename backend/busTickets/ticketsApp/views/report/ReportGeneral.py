from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ticketsApp.models import Ticket
from ticketsApp.views.querys.QueryReportsGeneral import SQL_QUERY_REPORT_GENERAL
from ticketsApp.utils.QueryCursor import execute_query


@extend_schema_view(
    list=extend_schema(description="List all reports General"),
)
class ReportGeneral(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()

    @action(detail=False, methods=['get'], url_path='report-general')
    def report_general(self, request):
        params = {
            'name': request.data.get('name', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None)
        }

        if params['name'] is None or params['initial_date'] is None or params['final_date'] is None:
            return Response({'error': 'name and initial_date and final_date required'}, status=400)

        response = execute_query(SQL_QUERY_REPORT_GENERAL, tuple(params.values()))
        return Response(response, status=200)
