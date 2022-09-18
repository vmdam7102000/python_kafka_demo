from email import message
import random
import string

user_ids = list(range(1,100))
recipient_ids = list(range(1,101))

def generate_message() -> dict:
    random_user_id = random.choice(user_ids)

    # copy the recipients array
    recipient_ids_copy = recipient_ids.copy()

    # user cant send message to him self
    recipient_ids_copy.remove(random_user_id)
    random_recipient_ids = random.choice(recipient_ids_copy)

    # gen random message
    message = ''.join(random.choice(string.ascii_letters) for i in range(32))

    return {
        'user_id': random_user_id,
        'recipient_id': random_recipient_ids,
        'message': message
        }

#testing
if __name__ == '__main__':
    print(generate_message())