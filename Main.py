import Char
import Boss

Jacob = Char.Player("Jacob")
Snugs = Char.Warrior("Snugs")
Nui = Char.Archmage("Nui")
Ragnaros = Boss.Boss("Ragnaros", 5, 100, 5, 5, 5)

Ragnaros.take_damage(5)
Ragnaros.take_damage(96)
Snugs.greet()
Snugs.attack()
