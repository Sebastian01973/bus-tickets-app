from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from ticketsApp.models import Ticket
from ticketsApp.utils.QueryCursor import execute_query
from ticketsApp.views.querys.QueryTickets import SQL_GENERAL_TICKET, SQL_TICKET


class TicketReport(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()

    @action(detail=False, methods=['post'], url_path='general-ticket')
    def ticket_report_general(self, request, pk=None):
        params = {
            'internal_number': request.data.get('internal_number', None),
            'id_road': request.data.get('id_road', None),
            'initial_date': request.data.get('initial_date', None),
            'final_date': request.data.get('final_date', None)
        }

        if params['internal_number'] is None or params['initial_date'] is None or params['final_date'] is None or params['id_road'] is None:
            return Response({'error': 'internal_number and initial_date and final_date and id_road required'}, status=400)

        value = execute_query(SQL_GENERAL_TICKET, tuple(params.values()))
        return Response(value, status=200)

    @action(detail=False, methods=['post'], url_path='ticket')
    def ticket_report(self, request, pk=None):
        params = {
            'id_box': request.data.get('id_box', None),
            'id_ticket': request.data.get('id_ticket', None),
        }
        if params['id_box'] is None or params['id_ticket'] is None:
            return Response({'error': 'id_box and id_ticket required'}, status=400)

        value = execute_query(SQL_TICKET, tuple(params.values()))
        return Response(value, status=200)


