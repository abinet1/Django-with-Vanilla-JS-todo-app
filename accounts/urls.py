from django.urls import path 
from accounts.views import View_Profile, Edit_Profile, Change_Password, Delete_Account, Sign_Up, Sign_In, Sign_Out

urlpatterns = [
    path('profile/<int:pk>/', View_Profile.as_view(), name="view_profile"),
    path('profile/<int:pk>/edit/', Edit_Profile.as_view(), name="edit_profile"),
    path('forget/password/', Change_Password.as_view(), name="change_password"),
    path('delete/', Delete_Account.as_view(), name="delete_account"),
    path('sign_up/', Sign_Up.as_view(), name="sign_up"),
    path('sign_in/', Sign_In.as_view(), name="sign_in"),
    path('sign_out/', Sign_Out.as_view(), name="sign_out"),
]
