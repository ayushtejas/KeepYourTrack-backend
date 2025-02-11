from django.urls import path
from events import views

app_name = 'events'

urlpatterns = [
    path('timer/', views.TimerViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='timer-list'),

    path('timer/<uuid:pk>/', views.TimerViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='timer-detail'),

    path('event/', views.EventViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='event-list'),

    path('event/<uuid:pk>/', views.EventViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='event-detail')
]