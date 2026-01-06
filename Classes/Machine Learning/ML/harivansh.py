def countdown(n):
    """Prints a countdown from n to 0."""
    while n >= 0:
        yield n
        n -= 1
        
gen = countdown(5)
# print(gen)  # This will print 'None' since countdown does not return anything
print(next(gen, None))  # This will raise an error since countdown is not a generator
# print(next(gen, None))  # This will raise an error since countdown is not a generator
# print(next(gen, None))  # This will raise an error since countdown is not a generator
# print(next(gen, None))  # This will raise an error since countdown is not a generator 



class chararacter:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack_enemy(self):
        return f"{self.name} attacks with power {self.power}!"
hero = chararacter("Archer", 50)
print(hero.attack_enemy())

villain = chararacter("Goblin", 30)
print(villain.attack_enemy())


