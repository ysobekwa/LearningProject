# Capture information for two users

users = []
name= input("please Enter name: ")
age = int(input("please Enter age: "))
height = float(input("please Enter height: "))

# store in dictionary
users.append ({
    'name': name,
    'age': age,
    'height': height
})
name= input("please Enter name: ")
age = int(input("please Enter age: "))
height = float(input("please Enter height: "))

users.append ({
    'name': name,
    'age': age,
    'height': height
})
print(type(users))
print()
# display each user information in as sentence using a loop
for user in users:
    print(f"{user['name']} is {user['age']} years old and {user['height']} cm tall.")
    print()

#calculate and display the total combined height for users
def total_height(users) :
    total = 0
    for user in users:
        total += user['height']
    return total
print(f"The total combined height of both users is {total_height(users)} cm ")


