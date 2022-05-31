from django.urls import path 
from accounts.views import Test_Home, View_Profile, Edit_Profile, Change_Password, Delete_Account, Sign_Up, Sign_In, Sign_Out

urlpatterns = [
    path('', View_Profile.as_view(), name="view_profile"),
    path('', Edit_Profile.as_view(), name="edit_profile"),
    path('', Change_Password.as_view(), name="change_password"),
    path('', Delete_Account.as_view(), name="delete_account"),
    path('home/', Test_Home.as_view(), name="home"),
    path('sign_up/', Sign_Up.as_view(), name="sign_up"),
    path('sign_in/', Sign_In.as_view(), name="sign_in"),
    path('sign_out/', Sign_Out.as_view(), name="sign_out"),
]
