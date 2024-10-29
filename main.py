import requests
import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "peter16"
TOKEN = "7huio901291lasjoe3q"
GRAPH_ID = "graph1"


#---------------- Create new user account -----------------
user_config = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_config)
# print(response.text)

#-------------------- Create new graph --------------------
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "My random graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#-------------------- Post value to graph--------------------
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today_date = dt.date.today().strftime("%Y%m%d")

update_data = {
    "date": today_date,
    "quantity": "9.5",
}

# response = requests.post(url=f"{pixel_creation_endpoint}", json=update_data, headers=headers)
# print(response.text)

# print(str(dt.datetime.now().date()).replace("-", ""))


#-------------------- Update value to graph--------------------
pixel_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/20241014"

config_data = {
    "quantity": "0",
}

response = requests.put(url=f"{pixel_update_endpoint}", json=config_data, headers=headers)
print(response.text)

#---------------- Delete value(pixel) on graph ----------------
pixel_delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today_date}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)

