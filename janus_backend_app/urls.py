from django.urls import path
from janus_backend_app import views

urlpatterns = [
    path('vehicles', views.vehicle_list),
    path('vehicles/<slug:vehicle_id>', views.vehicle_detail),
]