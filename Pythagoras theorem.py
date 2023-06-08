def calculate_hypotenuse(adjacent_leg, opposite_leg):
    squared_hypotenuse = adjacent_leg * adjacent_leg + opposite_leg * opposite_leg

    hypotenuse = squared_hypotenuse ** 0.5

    return "Hypotenuse", hypotenuse
    

adjacent = int(input ("How Long Is The Adjacent leg ?: ") )

opposite = int(input ("How Long Is The Opposite Leg?: ") )

print(calculate_hypotenuse(adjacent, opposite))
