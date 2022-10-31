from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup_view'),
    path('', views.login_view, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('add_balance/', views.Add_Balance, name='Add_Balance'),
    path('enter_secretCode/', views.transfer_money, name='Transfer_money'),
    path('money_sent/', views.Money_Sent, name='Money_Sent'),
    path('log_out/', views.log_out, name='log_out'),
    path('money_received/', views.Money_Received, name='Money_Received'),
    path('machine_learning/', views.machine_learning, name='machine_learning')
    
]