import secrets
import string

def pass_gen():


    # Set the length of the password
    password_length = 10

    # Define the pool of characters to choose from
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))

    # Print the password
    print("Your password is:", password)

    # Return the generated Password
    return password


