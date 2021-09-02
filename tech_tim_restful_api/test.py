import requests

BASE = "http://127.0.0.1:5000/"


data = [{"name":"vaibhav", "likes":1000, "views":5000},
        {"name":"ketan", "likes":7000, "views":8000},
        {"name":"rahul", "likes":8000, "views":9000},
        {"name":"rrrrr", "likes":3000, "views":4000}]

# for i in range(len(data)):
#     response = requests.put(BASE + f"video/{i}", data[i])
#     print(response.json())

# input()

# response = requests.patch(BASE + f"video/{2}", {"likes":999})
# print(response.json())

# input()

response = requests.delete(BASE + "video/2")
print(response.json)

input()

response = requests.get(BASE + "video/2")
print(response.json())


