from django.urls import path 
from todo.views import Home, Add_Task, Delete_Task, Update_Task, Edit_Task, Filter_Tasks
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('task/add/', Add_Task.as_view(), name='add_task'),
    # path('', Edit_Task.as_view(), name="edit_task"),
    # path('', Update_Task.as_view(), name="update_task"),
    # path('', Delete_Task.as_view(), name="delete_task"),
    # path('', Filter_Tasks.as_view(), name="filter_tasks"),
]
