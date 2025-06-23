# creating walking meter in pixela
from datetime import datetime ,timedelta
from http.client import responses

import requests

API_END_KEY = "https://pixe.la/v1/users"
TOKEN = "shdgfjsgddsjcdckjsdsk"
USER_NAME = "heartsofseven"
GRAPH_ID = "varun"

headers = {
    "X-USER-TOKEN" : TOKEN ,
}



# login to pixela
"""
user_params = {
    "token" : "shdgfjsgddsjcdckjsdsk" ,
    "username" : "heartsofseven" ,
    "agreeTermsOfService" : "yes" ,
    "notMinor" : "yes" ,
}
response = requests.post(url=API_END_KEY,json=user_params)
print(response.text)

"""

# creating a graph in pixela

"""

graph_params = {
    "id" : "varun" ,
    "color" : "ajisai" ,
    "unit" : "metre" ,
    "name" : "Varun Walking Meter",
    "type" : "float" ,
}
response = requests.post(url=f"{API_END_KEY}/{USER_NAME}/graphs",headers=headers,json=graph_params)
print(response.text)

"""



"""

i have created my graph
link = https://pixe.la/v1/users/heartsofseven/graphs/varun.html

"""

post_params = {
    "date" : datetime.now().strftime("%Y%m%d") ,
    "quantity" : input("How many kilo  metres did you walk today : ") ,

}



response = requests.post(url=f"{API_END_KEY}/{USER_NAME}/graphs/{GRAPH_ID}",headers=headers,json=post_params)
print(response.text)


params = {
    "quantity" : "4"
}

update_end_point = f"{API_END_KEY}/{USER_NAME}/graphs/{GRAPH_ID}/{"20250625"}"

"""

# updating the pixel

response = requests.put(url=,json=params,headers=headers)
print(response.text)

"""


"""

# deleting a pixel
response = requests.delete(url=update_end_point,headers=headers)
print(response.text)


"""
