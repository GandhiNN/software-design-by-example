import math

def square_perimeter(thing: dict) -> float:
    return 4 * thing["side"]

def square_area(thing: dict) -> float:
    return thing["side"] ** 2

def square_new(name, side):
    return {
        "name": name,
        "side": side,
        "_class": Square
    }

Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "_classname": "Square"
}

def circle_perimeter(thing: dict) -> float:
    return math.pi * thing["radius"] * 2

def circle_area(thing: dict) -> float:
    return math.pi * thing["radius"] ** 2

def circle_new(name, radius):
    return {
        "name": name,
        "radius": radius,
        "_class": Circle
    }

Circle = {
    "perimeter": circle_perimeter,
    "area": circle_area,
    "_classname": "Circle"
}

def call(thing, method_name):
    return thing["_class"][method_name](thing)

examples = [square_new("sq", 3), circle_new("ci", 2)]
for ex in examples:
    n = ex["name"]
    p = call(ex, "perimeter")
    a = call(ex, "area")
    c = ex["_class"]["_classname"]
    print(f"{n} is a {c}: {p:.2f} {a:.2f}")