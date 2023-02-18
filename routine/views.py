from rest_framework import status
from rest_framework.views import APIView, Listview
from rest_framework.response import Response
from routine.models import Routine, RoutineDay, RoutineResult

class RoutineCreateView(APIView):
    def post(self, request):
        pass
    
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

