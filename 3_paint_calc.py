import math

height = int(input("What is the height?"))
width = int(input("What is the width?"))
def getNum(w, h, can = 5):
    return math.ceil(w * h / can)

need = getNum(width,height,5)
print(f"You will need {need} cans of paint")