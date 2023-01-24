from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, inline_serializer
from drf_spectacular.types import OpenApiTypes
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers

from ticketsApp.models import Ticket
from ticketsApp.serializers.ticketSerializer import TicketSerializer
from ticketsApp.views.querys.QueryReportsGeneral \
    import SQL_QUERY_REPORT_GENERAL, SQL_PURCHASE_BY_CLIENT, SQL_USER_REPORT, SQL_GENERAL_USER_REPORT, \
    SQL_REPORT_GENERAL_TOTAL, SQL_PAYROLL_REPORT
from ticketsApp.utils.QueryCursor import execute_query


class GeneralReport(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @extend_schema(
        summary="Reporte general",
        description="Reporte general de las empresas",
        request=inline_serializer(
            name="InlineFormSerializer",
            fields={
                "nit": serializers.CharField(),
                "initial_date": serializers.DateField(),
                "final_date": serializers.DateField(),
            },
        ),
        responses={200: OpenApiTypes.OBJECT},
    )
    @action(detail=False, methods=['post'], url_path='general')
    def report_general(self, request, pk=None):
        params = {
            'nit': request.data.get('nit', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None)
        }
        print(tuple(params.values()))
        if params['nit'] is None or params['initial_date'] is None or params['final_date'] is None:
            return Response({'error': 'nit and initial_date and final_date required'}, status=400)

        values = execute_query(SQL_QUERY_REPORT_GENERAL, tuple(params.values()))
        return Response(values, status=200)

    @extend_schema(
        summary="Reporte general total",
        description="Reporte general total de las empresas",
        request=inline_serializer(
            name="InlineFormSerializer",
            fields={
                "initial_date": serializers.DateField(),
                "final_date": serializers.DateField(),
                "nit": serializers.CharField(),
            },
        ),
        responses={200: OpenApiTypes.OBJECT},
    )
    @action(detail=False, methods=['post'], url_path='general-total')
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

    @extend_schema(
        summary="compras por cliente en una empresa",
        description="Reporte general compras por cliente en una empresa",
        request=inline_serializer(
            name="InlineFormSerializer",
            fields={
                "id_client": serializers.IntegerField(),
                "initial_date": serializers.DateField(),
                "final_date": serializers.DateField(),
                "nit": serializers.CharField(),
            },
        ),
        responses={200: OpenApiTypes.OBJECT},
    )
    @action(detail=False, methods=['post'], url_path='purchase-by-client')
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

    @extend_schema(
        summary="Reporte por usuario",
        description="Reporte por usuario en una fechas inicial y final",
        request=inline_serializer(
            name="InlineFormSerializer",
            fields={
                "identification": serializers.CharField(),
                "initial_date": serializers.DateField(),
                "final_date": serializers.DateField(),
            },
        ),
        responses={200: OpenApiTypes.OBJECT},
    )
    @action(detail=False, methods=['post'], url_path='user-report')
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

    @extend_schema(
        summary="Reporte general por usuario",
        description="Reporte general por usuario en una fechas inicial y final",
        request=inline_serializer(
            name="InlineFormSerializer",
            fields={
                "initial_date": serializers.DateField(),
                "final_date": serializers.DateField(),
                "nit": serializers.CharField(),
                "box_id": serializers.IntegerField(),
            },
        ),
        responses={200: OpenApiTypes.OBJECT},
    )
    @action(detail=False, methods=['post'], url_path='general-user-report')
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

    @extend_schema(
        summary="Reporte de la planilla de los box office",
        description="Reporte de la planilla en una fechas inicial y final",
        request=inline_serializer(
            name="InlineFormSerializer",
            fields={
                "initial_date": serializers.DateField(),
                "final_date": serializers.DateField(),
                "box_id": serializers.IntegerField(),
            },
        ),
        responses={200: OpenApiTypes.OBJECT},
    )
    @action(detail=False, methods=['post'], url_path='pay-roll-report')
    def pay_roll_report(self,request,pk=None):
        params = {
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None),
            'box_id': request.data.get('box_id', None),
        }
        if params['initial_date'] is None or params['final_date'] is None or params['box_id'] is None:
            return Response({'error': 'initial_date and final_date and box_id required'}, status=400)

        value = execute_query(SQL_PAYROLL_REPORT, tuple(params.values()))
        return Response(value, status=200)
