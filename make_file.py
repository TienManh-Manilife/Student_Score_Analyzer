import random
import math

def round_up_to_0_1(value):
    return math.ceil(value * 10) / 10

with open("scores.txt", "r", encoding="utf-8") as fin, \
     open("time.txt", "w", encoding="utf-8") as fout:
    for line in fin:
        x = float(line.strip())
        a = random.gauss(10, 0.5)
        b = random.gauss(2, 0.5)
        noise = random.gauss(0, 0.2)
        y = a * x + b + noise
        y = round_up_to_0_1(y)
        fout.write(f"{y}\n")
