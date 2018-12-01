from django.contrib.auth.models import User, Group
from rest_framework import serializers
from janus_backend_app.models import Vehicle, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ('vehicle_id', 'vehicle_name', 'vehicle_access_token', 'vehicle_refresh_token', 'vehicle_location_latitude', 'vehicle_location_longitude', 'vehicle_destination_latitude', 'vehicle_destination_longitude')

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('lat', 'lon', 'name', 'description', 'location_type')