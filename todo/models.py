from datetime import datetime
from django.db import models
from django.forms import BooleanField

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    catagory = models.CharField(max_length=25)
    # status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    starting_date = models.DateTimeField()
    updated_date = models.DateTimeField(null=True, blank=True)
    do_data = models.DateTimeField()
    notify_me = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def get_status(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print(self.do_data.strftime('%Y-%m-%d %H:%M:%S'))
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')>self.do_data.strftime('%Y-%m-%d %H:%M:%S'))
        if self.is_completed:
            return "Completed"
        if self.is_deleted:
            return "Deleted"
        if datetime.now().strftime('%Y-%m-%d %H:%M:%S')>self.do_data.strftime('%Y-%m-%d %H:%M:%S'):
            return "Overdue"
        if datetime.now().strftime('%Y-%m-%d %H:%M:%S')>self.starting_date.strftime('%Y-%m-%d %H:%M:%S'):
            return "Active"
        if datetime.now().strftime('%Y-%m-%d %H:%M:%S')<self.starting_date.strftime('%Y-%m-%d %H:%M:%S'):
            return "Pending"
            
            

    