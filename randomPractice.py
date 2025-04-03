import random

random_number = random.randint(1, 10)
print(random_number)

toys = ["car", "doll", "ball", "bunny", "teddy bear", "chick"]
print(random.choice(toys))
print(random.randint(0, len(toys) - 1))

# name = "sadaf"
# print(random.choice(name))
