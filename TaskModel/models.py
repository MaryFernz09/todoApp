from dataclasses import dataclass
from django.db import models
from django.utils import timezone
import uuid
def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)

class TaskModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    isCompleted = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=one_day_hence)
    
    def __str__(self) -> str:
        return self.title
    
    
@dataclass
class TaskList_ByMonths:
    Month : str|None
    WeekCount : str | None
    DayOfTheWeek : str | None
    taskList : list[TaskModel] | None
    
    
           
        
