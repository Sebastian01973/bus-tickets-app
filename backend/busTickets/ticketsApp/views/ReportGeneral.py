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

        queryset = Ticket.objects.raw(SQL_QUERY_REPORT_GENERAL, params.values())
        print('Paso a serializer', 'Error Aca')
        serializer = ReportGeneralSerializer(queryset, many=True)
        return Response({serializer.data}, status=200)
