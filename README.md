# TEAM JANUS
## Hack.istanbul 2018
### Platoon.Me
#### Backend

Backend Application consists of a REST API that stores information of vehicles that connected to Platoon.Me application.

REST API is deployed on a Free-Tier Amazon EC2 instance.

Endpoint: Vehicles [GET] [POST]:
http://18.202.176.0:8000/vehicles

  Example Response:
  
  ```json
  [{
  	"vehicle_id" : "34ZRR34",
    	"vehicle_name" : "ZRR",
    	"vehicle_location_latitude" : "41.083030",
    	"vehicle_location_longitude" : "28.805453",
   	 "vehicle_destination_latitude" : "49.639412",
   	 "vehicle_destination_longitude" : "9.414035",
   	 "vehicle_description" : "none"
  }]
  ```

Endpoint: Vehicles/<vehicle_id > [GET] [PUT] [DELETE]
http://18.202.176.0:8000/vehicles/<vehicle_id>

  Example Response:
  ```json
  {
  	"vehicle_id" : "34ZRR34",
   	"vehicle_name" : "ZRR",
    	"vehicle_location_latitude" : "41.083030",
    	"vehicle_location_longitude" : "28.805453",
    	"vehicle_destination_latitude" : "49.639412",
    	"vehicle_destination_longitude" : "9.414035",
    	"vehicle_description" : "none"
  }
  ```

