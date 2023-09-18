from rest_framework import serializers
from . models import TaskModel, TaskList_ByMonths
from rest_framework_dataclasses.serializers import DataclassSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= TaskModel
        fields='__all__'
    
    def create(self, validated_data):
        task = TaskModel.objects.create(**validated_data)
        task.save()
        return task
    
    def get_all_tasks(self):
        taskList = TaskModel.objects.all()
        return taskList  
        

class TaskListByMonth_Serializer(DataclassSerializer):
    class Meta:
        dataclass = TaskList_ByMonths     