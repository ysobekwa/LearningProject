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

for user in users:
    print(f"{user['name']} is {user['age']} years old and {user['height']} cm tall.")




    #    'age': 15,
        #'height': 156.2
    #{
     #   'name': 'Tania',
     #   'age': 20,
     #   'height': 178.0
    #}
#]
#print(users)
#print (type(users))
#rint()

#display users info using a loop

#for i, user in enumerate(users,1):
       # print(f"{i} user['name'], user['age' ]}, user['height in cm']" )


#display

#name1 =[ input("Enter first user's name: ") ,age1 = int(input("Enter first user's age: ")),height1 = float(input("Enter first user's height in cm: "))]
#age1 = int(input("Enter first user's age: "))
#height1 = float(input("Enter first user's height in cm: "))

print()

# Capture information for User 2
#name2 = input("Enter second user's name: ")
#age2 = int(input("Enter second user's age: "))
#height2 = float(input("Enter second user's height in cm: "))

#print()


# Display user information
#print(f"{name1} is {age1} years old and is {height1} cm tall.")
#print(f"{name2} is {age2} years old and is {height2} cm tall.")

#print()

# Calculate and display total combined height
#total_height = height1 + height2

#print(f"The total combined height of both users is {total_height} cm.")