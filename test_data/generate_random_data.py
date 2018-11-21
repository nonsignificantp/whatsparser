import time
import random
import string


def get_rand_datetime():
    ts = 1290381327 + random.random() * 252460830
    return time.strftime('%d/%m/%Y %I:%M:%S %p', time.localtime(ts))


def get_rand_name():
    names = ['Raoul Fabijan', 'Nikolche Luna', 'Brad Hayder',
             'Arieh Ahura Mazda', 'Odile Pema']
    ix = random.randint(0, 4)
    return names[ix]


def get_rand_content():
    length = random.randint(50, 250)
    return "".join([random.choice(string.printable) for i in range(length)])


def get_msg():
    msg = f"{get_rand_datetime()}: {get_rand_name()}: {get_rand_content()}\n"
    return msg


if __name__ == '__main__':
    lines = 200
    with open('./data.txt', 'a') as file:
        for i in range(lines):
            msg = get_msg()
            file.write(msg)
