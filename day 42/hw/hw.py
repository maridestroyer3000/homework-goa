data = []

def register():

    print("Welcome to registration!")

    username = input("Enter your username:")
    password = input("Create a password:")

    current_user = {
        "name": username,
        "password": password
    }
    if len(data) == 0:
             print("Registration successfull")
             data.append(current_user)

    elif len(data) > 0:
            for i in data:
                if i ["name"] == current_user["name"]:
                    print("username already exists")
                    username = input("Enter your username again: ")
                    current_user["name"] = username
                    data.append(current_user)
                    break
            else: 
                print("Registration successfull")
                data.append(current_user)

            print(data)

def login():
                  
                  print("Welcome to login!")
                  username = input("Enter your username: ")
                  password = input("Enter your password: ")
                  
                  current_user = {
                        
                        "name": username,
                        "password": password

                  }

                  for i in data: 
                        if current_user in data:
                              print("Logged in")
                        else:
                              print("Incorrect username or password, please try again")


register()
login()
print(data)

