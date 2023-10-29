from django.urls import path

from . import views

app_name = 'tickets'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:id>/information/', views.DetailView.as_view(), name='detail'),
    path('<int:id>/information/buy_ticket/', views.BuyView.as_view(), name='buyTicket'),
    path('<int:id>/information/buy_ticket/buy/', views.buy, name='buy'),
]