from django.urls import path
from routine import views

urlpatterns = [
    path('create/', views.RoutineCreateView.as_view(), name="routine"),
    path('routinelist/<int:account_id>/', views.RoutineListView.as_view(), name="routinelist"),
    path('<int:account_id>/<int:routine_id>/', views.RoutineDetailView.as_view(), name="routinedetail"),
]