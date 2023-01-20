from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ticketsApp.models import Ticket
from ticketsApp.utils.QueryCursor import execute_query
from ticketsApp.views.querys.QuerySalesGeneral import SQL_TOTAL_COMPANY_SALES, SQL_SALES_BY_COMPANY_DATE, \
    SQL_SALES_BY_BOX_OFFICE, SQL_SALES_BY_VEHICLE, SQL_SALES_BY_DESTINY_AND_COMPANY


class SalesReport(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()

    @action(detail=False, methods=['get'], url_path='sales-company-total')
    def total_company_sales(self, request, pk=None):
        params = {
            'id_box': request.data.get('id_box', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None)
        }
        if params['id_box'] is None or params['initial_date'] is None or params['final_date'] is None:
            return Response({'error': 'id_box_office and initial_date and final_date required'}, status=400)
        values = execute_query(SQL_TOTAL_COMPANY_SALES, tuple(params.values()))

        return Response(values, status=200)

    @action(detail=False, methods=['get'], url_path='sales-company-by-date')
    def sales_by_company_date(self, request, pk=None):
        params = {
            'nit': request.data.get('nit', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None)
        }
        if params['nit'] is None or params['initial_date'] is None or params['final_date'] is None:
            return Response({'error': 'nit and initial_date and final_date required'}, status=400)
        values = execute_query(SQL_SALES_BY_COMPANY_DATE, tuple(params.values()))
        return Response(values, status=200)

    @action(detail=False, methods=['get'], url_path='sales-by-box-office')
    def sales_by_box_office(self, request, pk=None):
        params = {
            'id_box': request.data.get('id_box', None),
            'nit': request.data.get('nit', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None)
        }
        if params['id_box'] is None or params['nit'] is None or params['initial_date'] is None or params[
            'final_date'] is None:
            return Response({'error': 'id_box_office and nit and initial_date and final_date required'}, status=400)
        values = execute_query(SQL_SALES_BY_BOX_OFFICE, tuple(params.values()))
        return Response(values, status=200)

    @action(detail=False, methods=['get'], url_path='sales-by-vehicle')
    def sales_by_vehicle(self, request, pk=None):
        params = {
            'internal_number': request.data.get('internal_number', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None)
        }
        if params['internal_number'] is None or params['initial_date'] is None or params['final_date'] is None:
            return Response({'error': 'internal_number and initial_date and final_date required'}, status=400)
        values = execute_query(SQL_SALES_BY_VEHICLE, tuple(params.values()))
        return Response(values, status=200)

    @action(detail=False, methods=['get'], url_path='sales-by-destiny-and-company')
    def sales_by_destiny_and_company(self, request, pk=None):
        params = {
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None),
            'id_destiny': request.data.get('id_destiny', None),
            'nit': request.data.get('nit', None),
        }
        if params['initial_date'] is None or params['final_date'] is None or params['id_destiny'] is None or params[
            'nit'] is None:
            return Response({'error': 'initial_date and final_date and id_destiny and nit required'}, status=400)

        values = execute_query(SQL_SALES_BY_DESTINY_AND_COMPANY, tuple(params.values()))
        return Response(values, status=200)
