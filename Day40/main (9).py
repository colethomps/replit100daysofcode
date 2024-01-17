contacts = {"name":"", "DOB":"","Phone":"","Email":"","Address":""}
print("Contact Card")
contacts["name"] = input("Input your name:")
contacts["DOB"] = input("Input your DOB:")
contacts["Phone"] = input("Input your Phone:")
contacts["Email"] = input("Input your Email:")
contacts["Address"] = input("Input your Address:")

print(f"Hi {contacts['name']}. Our dictionary says that you were born on {contacts['DOB']}. We can call you on {contacts['Phone']}, email you at {contacts['Email']} or write to {contacts['Address']}.")