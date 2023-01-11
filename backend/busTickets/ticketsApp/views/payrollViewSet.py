from rest_framework import viewsets

from ticketsApp.models.payroll import Payroll
from ticketsApp.serializers.payrollSerializer import PayrollSerializer


class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
