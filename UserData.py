user_data = []

def main():
    import random
    import string

    firstName = input("Input your First Name: ")
    lastName = input("Input your Last Name: ")
    email = input("Input your Email address: ")
    length = 5
    random.choice(string.ascii_lowercase)
    ran = ''.join(random.choice(string.ascii_lowercase) for ran in range(length))
    password = firstName[0:2] + lastName[-2:] + ran
    print("Your password is: " + password)
    user_details = "Name: " + firstName + ' ' + lastName, "Email address: " + email, "Your password is: " + password
    user_satisfaction = input("Are you satisfied with this password? yes or no: ").lower()

    if user_satisfaction == "yes":
        print(user_details)
        user_data.append(user_details)

    elif user_satisfaction == "no":
        new_password = input("Enter your password: ")
        if len(new_password) < 7:
            print("Password should be at least 7 characters")
        else:
            new_user_details = "Name: " + firstName + ' ' + lastName, "Email address: " + email, "Your password is: " + new_password
            user_data.append(new_user_details)
            print(new_user_details)

    add_user = input("Do you wish to add another user? ").lower()
    if add_user == "yes":
        main()
    else:
        print(user_data)


# where the code starts
main()
