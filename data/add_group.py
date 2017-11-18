from model.group import Group
import random
import string

constant = [
    Group(name="Name1", header="Header1", footer="Footer1"),
    Group(name="Name2", header="Header2", footer="Footer2")
]

# генерация случайных строк не превышаюших длину maxlen
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
   #Group(name=name, header=header, footer=footer)
    #for name in ["", random_string("name", 10)]
    #for header in ["", random_string("header", 10)]
    #for footer in ["", random_string("footer", 10)]
    Group(name=random_string("name",10), header=random_string("header", 20), footer=random_string("footer",20))
    for i in range(3)
]
