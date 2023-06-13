phone_book = []
path = 'phones.txt'


def get_phone_book(phonebook: list):
    line = ''
    for contact in phonebook:
        row = ':'.join([str(value) for value in contact.values()])
        line += row + '\n'

    return line

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment, *_ = contact.strip().split(':')
        phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})

def save_file():
    with open(path, 'w', encoding='UTF-8') as file:

        file.write(get_phone_book(phone_book))


def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))
    return {'id': max(uid_list) + 1}


def add_contact(new: dict):
    id_dict = check_id()
    id_dict.update(new)
    phone_book.append(id_dict)


def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result


def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index - 1][key] = field

def delete(index: int):
    del phone_book[index-1]