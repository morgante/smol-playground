import random

def fortune_generator():
    fortunes = [
        "You will have a great day!",
        "Be patient, good things come to those who wait.",
        "Your hard work will soon pay off.",
        "You will find what you're looking for in unexpected places.",
        "A pleasant surprise is waiting for you.",
        "Your kindness will lead you to success.",
        "You will make a change for the better.",
        "Your dreams are closer than you think.",
        "You will receive some high praise or award.",
        "Your greatest desire will come true."
    ]

    return random.choice(fortunes)