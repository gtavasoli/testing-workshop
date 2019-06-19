from get_random_person import get_random_person


def get_next_person(user):
    person = get_random_person()
    while person in user['people_seen']:
        person = get_random_person()
    return person


if __name__ == '__main__':
    user = {'people_seen': []}

    print(get_next_person(user))
