import random
virus_day_remain = random.randint(0, 30)
class Me:

    def open_my_eyes(self):
        print("Open my eyes.")

    def close_my_eyes(self):
        print("Close my eyes.")

    def eat(self):
        print("Eat.")


me = Me()
for i in range(virus_day_remain):
    me.open_my_eyes()
    me.eat()
    me.eat()
    me.eat()
    me.close_my_eyes()