from django.shortcuts import render
from rest_framework import generics, response
from . serializer import TaskSerializer, TaskListByMonth_Serializer
from .models import TaskModel, TaskList_ByMonths
import calendar, datetime
from rest_framework.decorators import api_view


class CreateTask(generics.CreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    


class Task_RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    
    
    
    
@api_view(["GET"])
def getList(request):
    tasks  =  TaskModel.objects.all()
    months = []
    for month in tasks:
        if month.created_date.month not in months:
            months.append(month.created_date.month)
        listByMonth = []  
        list = []  
        for month in months:
                
            for task in tasks:
                print(task.created_date)
                print(task.created_date.month) 
                print(week_of_month(task.created_date))
                if task.created_date.month == month:
                    listByMonth.append(task)
                    
            x = TaskList_ByMonths(
                Month= calendar.month_name[task.created_date.month],
                WeekCount=week_of_month(task.created_date),
                DayOfTheWeek=calendar.day_name[task.created_date.weekday()],
                taskList=listByMonth
            
                                )
            list.append(x)
            
        serializer =  TaskListByMonth_Serializer(list, many=True) 
        
        print(serializer.data)   
        
    return response.Response(serializer.data, status=200)     
    

class CurrentDayTasks(generics.ListAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        tasks = TaskModel.objects.all()
        taskList = []
        for task in tasks:
            if task.created_date == datetime.date.today():
                taskList.append(task)
                
        return taskList
    
    
    
def week_of_month(tgtdate):
    days_this_month = calendar.mdays[tgtdate.month]
    for i in range(1, days_this_month):
            d = datetime.date(tgtdate.year, tgtdate.month, i)
            if d.day - d.weekday() > 0:
                startdate = d.day - d.weekday()
                break
        # now we canuse the modulo 7 appraoch
    return startdate-1
        
        
   
    