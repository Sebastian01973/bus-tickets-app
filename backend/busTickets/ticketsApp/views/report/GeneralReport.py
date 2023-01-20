from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ticketsApp.models import Ticket
from ticketsApp.views.querys.QueryReportsGeneral \
    import SQL_QUERY_REPORT_GENERAL, SQL_PURCHASE_BY_CLIENT, SQL_USER_REPORT, SQL_GENERAL_USER_REPORT, \
    SQL_REPORT_GENERAL_TOTAL
from ticketsApp.utils.QueryCursor import execute_query


class ReportGeneral(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()

    @action(detail=False, methods=['get'], url_path='general')
    def report_general(self, request, pk=None):
        params = {
            'nit': request.data.get('nit', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None)
        }

        if params['nit'] is None or params['initial_date'] is None or params['final_date'] is None:
            return Response({'error': 'nit and initial_date and final_date required'}, status=400)

        values = execute_query(SQL_QUERY_REPORT_GENERAL, tuple(params.values()))
        return Response(values, status=200)

    @action(detail=False, methods=['get'], url_path='general-total')
    def report_general_total(self, request, pk=None):
        params = {
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None),
            'nit': request.data.get('nit', None),
        }
        if params['nit'] is None or params['initial_date'] is None or params['final_date'] is None:
            return Response({'error': 'nit and initial_date and final_date required'}, status=400)
        values = execute_query(SQL_REPORT_GENERAL_TOTAL, tuple(params.values()))
        return Response(values, status=200)

    @action(detail=False, methods=['get'], url_path='purchase-by-client')
    def purchases_by_client_company(self, request, pk=None):
        params = {
            'id_client': request.data.get('id_client', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None),
            'nit': request.data.get('nit', None),
        }
        if params['id_client'] is None or params['initial_date'] is None or params['final_date'] is None or params[
            'nit'] is None:
            return Response({'error': 'id_client and initial_date and final_date and nit required'}, status=400)
        values = execute_query(SQL_PURCHASE_BY_CLIENT, tuple(params.values()))
        return Response(values, status=200)

    @action(detail=False, methods=['get'], url_path='user-report')
    def user_report(self, request, pk=None):
        params = {
            'identification': request.data.get('identification', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None),
        }
        if params['identification'] is None or params['initial_date'] is None or params['final_date'] is None:
            return Response({'error': 'identification and initial_date and final_date required'}, status=400)

        values = execute_query(SQL_USER_REPORT, tuple(params.values()))
        return Response(values, status=200)

    @action(detail=False, methods=['get'], url_path='general-user-report')
    def general_user_report(self, request, pk=None):
        params = {
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None),
            'nit': request.data.get('nit', None),
            'box_id': request.data.get('box_id', None),
        }
        if params['initial_date'] is None or params['final_date'] is None or params['nit'] is None or params[
            'box_id'] is None:
            return Response({'error': 'initial_date and final_date and nit and box_id required'}, status=400)
        value = execute_query(SQL_GENERAL_USER_REPORT, tuple(params.values()))
        return Response(value, status=200)
