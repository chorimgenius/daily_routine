from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from routine.models import Routine, RoutineDay, RoutineResult
from routine.serializers import RoutineCreateSerializer

class RoutineCreateView(APIView):
    def post(self, request):
        DAYS_DICT = {"MON":"0","TUE":"1","WED":"2","THU":"3","FRI":"4","SAT":"5","SUN":"6"}
        data = request.data.copy()
        data["days"] = [DAYS_DICT[x] for x in data.get("days", [])]
        serializer = RoutineCreateSerializer(data = data)
        if serializer.is_valid():
            serializer.save(account_id = request.user.id)
            return Response({"msg": "You have successfully created the routine."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RoutineListView(APIView):
    def get(self, request):
        pass

class RoutineDetailView(APIView):
    def get(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass

