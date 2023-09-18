from django.urls import path
from . views import CreateTask, Task_RUD, getList, CurrentDayTasks
urlpatterns = [
    path('create-task', CreateTask.as_view(), name="Create New Task"),
    path('task-rud/<str:pk>', Task_RUD.as_view(), name="Task_RUD"),
    path('tasklist', view=getList, name="TaskList_ByMonth"),
    path('current-tasklist', CurrentDayTasks.as_view(), name="Current_TaskList")
]