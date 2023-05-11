def server():
    while True:
        password=int(input("Enter your password:"))
        if password in ["good"]:
            print("Welcome server")
            break
        else:
            print("You are not allowed")
server()