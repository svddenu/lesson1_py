domain = ['.ru', '.net', '.com']
issue = ['Невозможно отправить письмо с {} на {}', 'Нельзя отправить письмо самому себе!', 'Невозможно отправить, не найден домен этого адреса!']

def send_email(message, recipient, sender='university.help@gmail.com'):
    send = ''
    ch = '@'
    for i in domain:
        if i in recipient and sender != recipient:
            send = 'Письмо успешно отправлено'
            return send
        elif i == domain[-1]:
            send = issue[2]
            return send
        elif sender == recipient:
            send = issue[1]
            return send
        elif ch not in recipient:
            send = issue[0].format(sender, recipient)
            return send



print(send_email('fdgfdfgd', 'adress@gmail.com'))
print(send_email('fdgfdfgd', 'adress@gmail.ff'))
print(send_email('fdgfdfgd', 'adress@gmail.ru'))
print(send_email('fdgfdfgd', 'adress@gmail.net'))
print(send_email('fdgfdfgd', 'adress@gmail.net', sender='urban.teacher@mail.uk'))
print(send_email('fdgfdfgd', 'urban.teacher@mail.uk', sender='urban.teacher@mail.uk'))
print(send_email('fdgfdfgd', 'adressgmail.net', sender='urban.teachermail.uk'))
