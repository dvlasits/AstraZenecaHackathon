from random import random


class TopTrumpClass:

    def __init__(self, id, height, weight):
        self.id = id
        self.height = height
        self.weight = weight
        self.choices = {"id": self.id, "height": self.height, "weight": self.weight}

    def __repr__(self):
        return f"id : {self.id}, height : {self.height}, weight : {self.weight}"

    def pick(self, opp):
        choice = input("pick a choice")
        num = self.choices[choice]
        print("Computers Card:")
        print(opp)
        if opp.choices[choice] < num:
            print("Yess nailed it")
            return 1
        print("Damn Unlucky")
        return 0


MyTopTrumpCards = [TopTrumpClass(random(), random(), random()) for k in range(10)]

ComputersCards = [TopTrumpClass(random(), random(), random()) for k in range(10)]


def fight():
    currCard = MyTopTrumpCards.pop(0)
    opp = ComputersCards.pop(0)
    print(currCard)
    return currCard.pick(opp)


YouScore = 0
OppScore = 0
for i in range(len(MyTopTrumpCards)):
    win = fight()
    YouScore += win
    OppScore += (1 - win)
    print(f"Your score is {YouScore}, and computer has {OppScore}")
