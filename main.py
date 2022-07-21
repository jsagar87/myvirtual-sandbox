import re
import collections

import custom_types.types as types
from modules.dry_run import print_mypath as pathfn


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    pathfn("mypath")

c = 3


def add():
    global c
    c = c + 1
    print(c)


add()
print("In main C:", c)

a = [1, 2, 99, 4]
print("In main C: %s " % a[2])
print(*a)

print("==============")
f = open("alert_data.txt", mode='r', encoding='utf-8')
Ip_string = f.readlines()
print(len(Ip_string))
f.close()
print(Ip_string)
print(re.search("\"ProviderId\": \"(.*?)\"", str(Ip_string)).group())
provider_match = re.search("\"ProviderId\": \"(.*?)\"", str(Ip_string))
if provider_match:
    print("Mila")
else:
    print("Nahi mila")

provider_id = provider_match.group()

message = "# Provider Id:- " + provider_id.split(":")[1] + "\n"

print(message)

# mysql -uroot -proot -h127.0.0.1 -P6603 -e 'show global variables like "max_connections"';

fruits = types.Fruits(["apple", "banana", "watermelon", "strawberry", "mango"])
fruits.print_list()
print(len(fruits))
print(fruits[2])
beer_card = types.Card('7', 'diamonds')
print(beer_card)
print("----------")

deck = types.FrenchDeck()

for card in deck[12::13]:
    print(card)
print("----------")

for card in reversed(deck):  # doctest: +ELLIPSIS
    print(card)
print("----------")

print(types.Card('8', 'spades') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spade_high(pick_card):
    rank_value = types.FrenchDeck.ranks.index()
    return rank_value * len(suit_values) + suit_values[pick_card.suits]


d = collections.deque()
d.append(5)
d.append(2)
d.append(9)
d.append(7)

try:
    d.pop()
except IndexError:
    print("Fill the queue first")
    print("This must be index error %r" % IndexError)
