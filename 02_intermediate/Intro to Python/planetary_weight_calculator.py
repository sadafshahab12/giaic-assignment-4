# Calculating the weight on Mars, which we do by multiplying the Earth weight by 0.378. To make the program easy to read, we store this number in a constant called MARS_MULTIPLE.


# MARS_MULTIPLE = 0.378
# def main():
#     earth_weight_str = input("Enter a weight on earth: ")
#     earth_weight = float(earth_weight_str)

#     mars_weight = earth_weight * MARS_MULTIPLE
#     rounded_mars_weight = round(mars_weight, 2)
#     print(f"The equivalent weight on Mars: {rounded_mars_weight}")


# if __name__ == "__main__":
#     main()

# """ Prompts the user for a weight on Earth and a planet (in separate inputs). Then prints the equivalent weight on that planet.

# Note that the user should type in a planet with the first letter as uppercase, and you do not need to handle the case where a user types in something other than one of the planets (that is not Earth). """

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0


def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on earth: "))
    # Prompt the user for the name of a planet
    planet = input("Enter a planet: ")

    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY
    planetry_weight = earth_weight * gravity_constant
    rounded_planetry_weight = round(planetry_weight, 2)
    print(f"The equivalent weight on {planet} is {rounded_planetry_weight} ")


if __name__ == "__main__":
    main()
