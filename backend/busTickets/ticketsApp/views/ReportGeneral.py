from django.db import connection
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ticketsApp.models import Ticket
from ticketsApp.serializers.reports.reportGeneralSerializer import ReportGeneralSerializer
from ticketsApp.views.querys.QueryReportsGeneral import SQL_QUERY_REPORT_GENERAL


class ReportGeneral(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()

    @action(detail=False, methods=['get'], url_path='report-general')
    def report_general(self, request, pk=None):
        params = {
            'name': request.data.get('name', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None)
        }

        if params['name'] is None or params['initial_date'] is None or params['final_date'] is None:
            return Response({'error': 'name and initial_date and final_date required'}, status=400)

        with connection.cursor() as cursor:
            cursor.execute(SQL_QUERY_REPORT_GENERAL, (params['name'], params['initial_date'], params['final_date']))
            columns = [col[0] for col in cursor.description]
            values = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(values, status=200)
