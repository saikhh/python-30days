import random
import string

def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters: "))
    num_ids = int(input("Enter the number of IDs to generate: "))

    chars = string.ascii_letters + string.digits

    for _ in range(num_ids):
        user_id = ''.join(random.choice(chars) for _ in range(num_chars))
        print(user_id)

# Call the function
user_id_gen_by_user()


