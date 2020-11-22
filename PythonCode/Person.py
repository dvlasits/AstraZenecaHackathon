class Person:
    def __init__(self, name, password, savedCarbon, admin = False):
        self.name = name
        self.password = password
        self.savedCarbon = savedCarbon
        self.admin = admin



    def PersonSaved(self):
        total = 0
        for item in self.savedCarbon:
            total += self.savedCarbon[item]
        return total

    def __repr__(self):
        return self.name + str(self.savedCarbon)
