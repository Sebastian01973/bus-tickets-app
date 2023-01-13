from rest_framework import serializers

from ticketsApp.models.payroll import Payroll


class PayrollSerializer(serializers.ModelSerializer):
    """Serializer for PayRoll Model Class"""
    class Meta:
        model = Payroll
        fields = '__all__'
