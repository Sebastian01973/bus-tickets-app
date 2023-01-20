from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from ticketsApp.models.payroll import Payroll
from ticketsApp.serializers.payrollSerializer import PayrollSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all payrolls",
        description="Return a list of all the payrolls"),
    retrieve=extend_schema(
        summary="Retrieve a payroll",
        description="Get details about a specific payroll"),
    create=extend_schema(
        summary="Create a payroll",
        description="Return details about a newly created payroll"),
    update=extend_schema(
        summary="Update a payroll",
        description="Return details about an updated payroll"),
    destroy=extend_schema(
        summary="Delete a payroll",
        description="Delete a payroll and return status code 204"),
)
class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
