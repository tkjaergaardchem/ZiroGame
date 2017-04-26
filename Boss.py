class Boss:

    def __init__(self, name, lvl, hp, str, int, agi, is_alive=True):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.str = str
        self.int = int
        self.agi = agi
        self.is_alive = True

    def take_damage(self, damage):
        remaining_points = self.hp - damage
        if remaining_points >= 0:
            self.hp = remaining_points
            print("{} took {} damage and have {} left".format(self.name,damage,remaining_points))
        else:
            self.is_alive = False
            print("{} have been killed".format(self.name))

    def __str__(self):
        return "Name: {0.name}, Lvl:{0.lvl}".format(self)

