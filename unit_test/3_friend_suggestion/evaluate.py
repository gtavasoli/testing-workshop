def send_email(person):
    print("Send email to {}".format(person))


def let_down_gently(person):
    print("Disliked poor {}".format(person))


def give_it_time(person):
    print("Give it time for {}".format(person))


def evaluate(person1, person2):
    if person1 in person2['likes']:
        send_email(person1)
        send_email(person2)
    elif person1 in person2['dislike']:
        let_down_gently(person1)
    elif person1 not in person2['likes'] and person1 not in person2['dislike']:
        give_it_time(person1)
