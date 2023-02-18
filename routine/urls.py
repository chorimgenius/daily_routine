from django.urls import path
from routine import views

urlpatterns = [
    path('create/', views.RoutineCreateview.as_view(), name="routine"),
    path('routinelist/<int:account_id>/', views.RoutineLListView.as_view(), name="routinelist"),
    path('<int:account_id>/<int:routine_id>/', views.RoutineDetailview().as_view(), name="routinedetail"),
]