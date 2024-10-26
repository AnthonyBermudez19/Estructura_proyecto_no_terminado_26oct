from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('add/', views.add_ticket, name='add_ticket'),
    path('current/', views.current_ticket, name='current_ticket'),
    path('attend/', views.attend_ticket, name='attend_ticket'),
    path('sorted/', views.sorted_tickets_view, name='sorted_tickets'),
    path('search/<int:ticket_id>/', views.search_ticket_view, name='search_ticket'),

]

