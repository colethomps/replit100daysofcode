# This code should output 'Hello there'
firstName = (input("First Name:"))
lastName = (input("Last Name:"))

print(firstName[0:3] + lastName[0:3].lower())

maiden = input("What is your mother's maiden name?")
city = input("What city were you born in?")
print("Your star wars name is " + maiden[0:2] + city[-3:].lower())