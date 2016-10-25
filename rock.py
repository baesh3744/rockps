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
    user_name = input("사용자의 이름을 입력해주세요. ")
    while True:
        hand = ["가위", "바위", "보"]
        com_hand = int(random.randrange(3))
        user_hand = int(input("무엇을 내시겠습니까? (0:가위, 1:바위, 2:보) "))
        print("컴퓨터가 낸 것은 "+ hand[com_hand]+ " 입니다.")
        print(user_name + "이 낸 것은 " + hand[user_hand] + " 입니다.")
        if (com_hand==user_hand):
            print("Draw!!!")
        elif ((user_hand-com_hand==1) or (user_hand-com_hand==-2)):
            print("User Wins!!!")
        else:
            print("Computer Wins!!!")
        more = input("더 하시겠습니까? (Y/N)")
        if more == "N":
            print("가위바위보를 종료합니다.")
            break

rocksp()
