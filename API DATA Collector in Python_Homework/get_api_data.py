import requests
import json

# Task 1: Fetch Data
def fetch_api_data():
    response = requests.get("https://www.ndosiautomation.co.za/APIDEV/groups")
    data = response.json()
    return data

#print (fetch_api_data())

# Task 2: Save data
def save_api_data(data):
    with open('groups.json', 'w') as file:
        json.dump(data, file)

# Task 3:
def search_group():
    with open("groups.json", "r") as file:
        data = json.load(file)

    group_name = input("Enter group name: ")

    for group in data["data"]:
       if group["Name"] == group_name:
            print("Found ID:", group["Id"])
            return

    print("Group not found")

group_data = fetch_api_data()
print(group_data)
print (save_api_data(group_data))
print (search_group())

