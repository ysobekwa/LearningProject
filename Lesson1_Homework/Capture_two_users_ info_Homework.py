# Capture information for two users
#user1
users = [] #list
name= str(input("please Enter name: "))
if not name.isalpha():
    print("please enter letters only")
else:
    print("valid name")

age = int(input("please Enter age: "))
height = float(input("please Enter height: "))

# dictionary inside a list
user1 = ({
    'name': name,
    'age': age,
    'height': height
})
users.append(user1)
print(type(user1))
print()

#user2
name2= str(input("please Enter name: "))
if not name2.isalpha():
    print("please enter letters only")
else:
    print("valid name")

age2 = int(input("please Enter age: "))
height2 = float(input("please Enter height: "))

# store in dictionary
user2 = ({
    'name': name2,
    'age': age2,
    'height': height2
})
users.append(user2)
print(type(user2))
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


