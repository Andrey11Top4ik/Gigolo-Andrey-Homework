class Kopilka:
    def __init__(self):
        self.balance = 100
        self.goal = 0
    def polozhit(self, money):
        self.balance = self.balance + money
        print("Баланс:", self.balance)
    def snyat(self, money):
        self.balance = self.balance - money
        print("Баланс:", self.balance)
    def postavit_tzel(self, money):
        self.goal = money
        print("цель поставлена:", self.goal)
    def hvatit_na_tzel(self):
        if self.balance >= self.goal:
            print("Хватает на цель")
        else:
            print("Не хватает на цель")

k = Kopilka()
while True:
    cmd = input("Что сделать? ").lower()
    if cmd == "exit":
        break
    if cmd == "polozhit":
        x = int(input("Сколько положить: "))
        k.polozhit(x)
    if cmd == "snyat":
        x = int(input("Сколько снять: "))
        k.snyat(x)
    if cmd == "postavit_tzel":
        x = int(input("Какая цель: "))
        k.postavit_tzel(x)
    if cmd == "hvatit_na_tzel":
        k.hvatit_na_tzel()
