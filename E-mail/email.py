email = input("Enter your email address:")

if len(email) >= 6 and email.count("@") == 1:
    username, domain = email.split("@")
    if username.isalpha() and domain.count(".") == 1:
        domain_name, extension = domain.split(".")
        if all(c.isalnum() or c in ['_', '.'] for c in username) and all(c.isalpha() for c in domain_name) and all(c.isalpha() or c == '.' for c in extension):
            print("Valid email address:", email)
        else:
            print("Invalid email address")
    else:
        print("Invalid email address")
else:
    print("Invalid email address")
