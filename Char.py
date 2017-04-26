# Opret en spiller
class Player:

    def __init__(self, player_name):
        self.player_name = player_name
        print("Player named {0} created".format(player_name))


# En spiller opretter en char
# Class er superklassen for de forskellige klasser
class Class:

    def __init__(self, name, hp, stam):
        self._name = name
        self._hp = hp
        self._stam = stam

    def greet(self):
        print("{} says greet".format(self._name))

# Warrior udvider Class
class Warrior(Class):

    def __init__(self, name):
        Class.__init__(self, name=name, hp=100, stam=15)
        self._str = 5
        self._int = 0
        self._agi = 5
        self._lvl = 1
        self._xp = 0
        print("A warrior named {} was created with hp of {} and lvl {}".format(name, self._hp, self._lvl))

    def attack(self):
        print ("{} attacks".format(self._name))

# Archmage udvider Class
class Archmage(Class):

    def __init__(self, name):
        Class.__init__(self, name=name, hp=90, stam=11)
        self._str = 0
        self._int = 6
        self._agi = 2
        self._lvl = 1
        self._xp = 0
        print("A mage named {} was created with hp of {} and lvl {}".format(name, self._hp, self._lvl))
