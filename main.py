import requests
from datetime import datetime

Token="jnfcjewve484egewdgv"
Username="pariyul001"
Graph="graph001"

api_endpoint="https://pixe.la/v1/users"
api_params={
    "token": Token,
    "username": Username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#
# response=requests.post(url=api_endpoint,json=api_params)
# print(response.text)
graph_endpoint=f"{api_endpoint}/{Username}/graphs"
graph_params={
    "id": Graph,
    "name":"Coding Graph",
    "unit": "Hour",
    "type": "int",
    "color": "ajisai"

}
Headers={
    "X-USER-Token": Token
}
# response=requests.post(url=graph_endpoint,json=graph_params,headers=Headers)
# print(response.text)

today=datetime.now()

pixel_endpoint=f"{api_endpoint}/{Username}/graphs/{Graph}"



pixel_params={
    "date": today.strftime("%Y%m%d"),
    "quantity": "6",

}

# response=requests.post(url=pixel_endpoint,json=pixel_params,headers=Headers)
# print(response.text)

update_endpoint= f"{api_endpoint}/{Username}/graphs/{Graph}<<{today.strftime('%Y%m%d')}"
pixel_new_data={
    "quantity" : input("how many hour did you code today:")
}
response=requests.put(url=update_endpoint,json=pixel_new_data,headers=Headers)


