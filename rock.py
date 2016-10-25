"""
===================
Rock-Paper-Scissors
===================

* **members :** Bae SeongHun
* **date :** 2016.10.12
* **input :**

* before start input user name
* while loop : 0(scissors), 1(rock), 2(paper)
* more game? (Y/N)

* **output**

    +-------------+-------------+-------------------+
    | computer    | user        | print             |
    +-------------+-------------+-------------------+
    | rock(1)     | rock(1)     |                   |
    +-------------+-------------+                   +
    | scissors(0) | scissors(0) | Draw!!!           |
    +-------------+-------------+                   +
    | paper(2)    | paper(2)    |                   |
    +-------------+-------------+-------------------+
    | rock(1)     | scissors(0) |                   |
    +-------------+-------------+                   +
    | scissors(0) | paper(2)    | Computer Wins!!!  |
    +-------------+-------------+                   +
    | paper(2)    | rock(0)     |                   |
    +-------------+-------------+-------------------+
    | scissors(0) | scissors(0) |                   |
    +-------------+-------------+                   +
    | rock(1)     | paper(2)    | User Wins!!!      |
    +-------------+-------------+                   +
    | paper(2)    | rock(1)     |                   |
    +-------------+-------------+-------------------+

"""

import random

def rocksp():
    user_name = input("������� �̸��� �Է����ּ���. ")
    while True:
        hand = ["����", "����", "��"]
        com_hand = int(random.randrange(3))
        user_hand = int(input("������ ���ðڽ��ϱ�? (0:����, 1:����, 2:��) "))
        print("��ǻ�Ͱ� �� ���� "+ hand[com_hand]+ " �Դϴ�.")
        print(user_name + "�� �� ���� " + hand[user_hand] + " �Դϴ�.")
        if (com_hand==user_hand):
            print("Draw!!!")
        elif ((user_hand-com_hand==1) or (user_hand-com_hand==-2)):
            print("User Wins!!!")
        else:
            print("Computer Wins!!!")
        more = input("�� �Ͻðڽ��ϱ�? (Y/N)")
        if more == "N":
            print("������������ �����մϴ�.")
            break

rocksp()
