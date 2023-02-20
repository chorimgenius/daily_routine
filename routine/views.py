from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from routine.models import Routine, RoutineDay, RoutineResult
from routine.serializers import RoutineCreateSerializer, RoutineListSerializer

class RoutineCreateView(APIView):
    def post(self, request):
        DAYS_DICT = {"MON":"0","TUE":"1","WED":"2","THU":"3","FRI":"4","SAT":"5","SUN":"6"}
        data = request.data.copy()
        data["days"] = [DAYS_DICT[x] for x in data.get("days", [])]
        serializer = RoutineCreateSerializer(data = data)
        if serializer.is_valid():
            routine = serializer.save(account_id = request.user.id)
            routine_id = routine.id
            message = {
            "msg": "You have successfully created the routine",
            "status": "ROUTINE_CREATED_OK"
            }
            data = {
                "routine_id": routine_id
            }
            response_data = {
                "data": data,
                "message": message
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RoutineListView(APIView):
    def get (self, request, account_id):
        today = request.data['today']
        routines = Routine.objects.filter(Q(account_id=account_id)|Q(created_at=today))
        serializer = RoutineListSerializer(routines, many=True)
        data = serializer.data
        message = {
            "msg": "Routine lookup was successful",
            "status": "ROUTINE_LIST_OK"
        }
        response_data = {
                "data": data,
                "message": message
            }
        return Response(response_data, status=status.HTTP_200_OK)

class RoutineDetailView(APIView):
    def get(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass

