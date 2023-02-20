from rest_framework import serializers
from routines.models import Routine, RoutineDay, RoutineResult

class RoutineCreateSerializer(serializers.ModelSerializer):
    days = serializers.ListField()
    class Meta:
        model = Routine
        fields = ('title','category' ,'goal','is_alarm','days')

    def create(self, validated_data):
        days_list = validated_data.pop("days")
        routine = super().create(validated_data)
        for day in days_list:
            RoutineDay.objects.create(day=int(day), routine=routine)
        return routine
