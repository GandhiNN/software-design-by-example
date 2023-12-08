from objects_and_classes import shapes
from typing import Any

import math

def example() -> str:
    print("in example")

def square_perimeter(thing: Any):
    return 4 * thing["side"]

def square_area(thing: Any):
    return thing["side"] ** 2

def square_new(name: str, side: float):
    return {
        "name": name,
        "side": side,
        "perimeter": square_perimeter,
        "area": square_area
    }

def circle_perimeter(thing: Any):
    return math.pi * 2 * thing["radius"]

def circle_area(thing: Any):
    return math.pi * thing["radius"] ** 2

def circle_new(name: str, radius: float):
    return {
        "name": name,
        "radius": radius,
        "perimeter": circle_perimeter,
        "area": circle_area
    }

def call(thing: dict, method_name: str):
    return thing[method_name](thing)

def main():
    # Function aliasing
    alias = example
    alias()

    # Objects and classes example
    examples1 = [shapes.Square("sq", 3), shapes.Circle("ci", 2)]
    examples2 = [square_new(name="sq", side=3), circle_new(name="ci", radius=2)]

    # Using the objects directly
    for thing in examples1:
        n = thing.name
        p = thing.perimeter()
        a = thing.area()
        print(f"{n} has perimeter {p:.2f} and area {a:.2f}")

    # Using the call()
    for thing in examples2:
        n = thing["name"]
        p = call(thing, "perimeter")
        a = call(thing, "area")
        print(f"{n} has perimeter {p:.2f} and area {a:.2f}")


if __name__ == '__main__':
    main()