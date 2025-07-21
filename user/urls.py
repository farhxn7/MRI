from django.urls import path
from user import views
urlpatterns = [
    path('', views.index ,name='index'),
    path('adminbase/', views.Admin_base , name='adminbase'),
    path('adminlogin/', views.Admin_login , name='adminlogin'),
    path('registeruserview/', views.RegisterUsersView , name = 'registeruserview'),
    path('deleteuser/', views.Deleteuser , name= 'deleteuser'),
    path('activateuser/', views.Activate, name='activateuser'),
    path('userbase/', views.User_Base, name='userbase'),
    path('userlogin/', views.User_Login , name='userlogin'),
    path('logout', views.logout , name='logout'),
    path('userregister/', views.User_register , name='userregister'),
    path('upload/', views.uploaded , name='upload'),
    path('predectionresult/', views.prediction_Result , name='predectionresult'),
    
    # path('dataset/' , views.dataset , name='dataset'),
]