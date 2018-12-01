from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from janus_backend_app.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from janus_backend_app.models import Vehicle
from janus_backend_app.serializers import VehicleSerializer
import requests

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@csrf_exempt
def vehicle_list(request):
    if request.method == 'GET':

        

        # url = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles/"

        # headers = {
        #     'authorization': "Bearer d1dd7a7c-9779-4b91-a270-1c11e256ed45",
        #     'Accept': "application/json",
        #     }

        # response = requests.request("GET", url, headers=headers)

        # url = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles/"

        # headers = {
        #     'authorization': "Bearer d1dd7a7c-9779-4b91-a270-1c11e256ed45",
        #     'Accept': "application/json",
        #     }

        # response = requests.request("GET", url, headers=headers)

        # url = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles/"

        # headers = {
        #     'authorization': "Bearer d1dd7a7c-9779-4b91-a270-1c11e256ed45",
        #     'Accept': "application/json",
        #     }

        # response = requests.request("GET", url, headers=headers)
        



        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def vehicle_detail(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)

    except Vehicle.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VehicleSerializer(vehicle)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehicleSerializer(vehicle, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vehicle.delete()
        return HttpResponse(status=204)

