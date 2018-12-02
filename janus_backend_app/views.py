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


ACCESS_TOKEN = "7a1b1db9-045f-4241-8d87-cc8553b826f5"
REFRESH_TOKEN = "8ffbce79-397d-4a3c-85f9-65025821d21e"




# def refresh_token():
#     url = "https://api.secure.mercedes-benz.com/oidc10/auth/oauth/v2/token"

#     payload = f"grant_type=refresh_token&refresh_token={REFRESH_TOKEN}&undefined="
#     headers = {
#         'authorization': "Basic NGM0NmI1ZTctNTRiZi00YWNiLThhODYtZjFhYjMyMWIyY2I1OjZkM2YwZmVjLTM2ZjAtNDM1OS1iNTEzLTc4ZjViMTk0ODAzZA==",
#         'content-type': "application/x-www-form-urlencoded",
#     }

#     response = requests.request("POST", url, data=payload, headers=headers)
#     response_json = response.json()
#     ACCESS_TOKEN[car_no] = response_json['access_token']
#     REFRESH_TOKEN[car_no] = response_json['refresh_token']
#     print(response.text)


# def get_vehicle_from_api():
#     print(ACCESS_TOKEN)
#     print(REFRESH_TOKEN)
#     url = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles/"

#     headers = {
#         'authorization': f"Bearer {ACCESS_TOKEN}",
#         'Accept': "application/json",
#     }

#     response = requests.request("GET", url, headers=headers)
#     print(response)
#     if response.status_code == 401:
#         print("access token is refreshing")
#         refresh_token()    
#     else:
#         print("access token still active")
#     print(response.json()[0]["id"])

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

        # get_vehicle_from_api()    

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
