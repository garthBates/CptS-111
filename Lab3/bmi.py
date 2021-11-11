####
#Lab 3 task 3
####

def convert_height(height):
    height = height * 0.0254
    return height

def convert_weight(weight):
    weight = weight * 0.45359237
    return weight

def calc_bmi(height, weight):
    bmi = weight / (height ** 2)
    print("BMI     = ", bmi)
    print("Mass    = ", weight, " [kilograms]")
    print("Height  = ", height, " [meters]")


weight = float(input("Enter weight [pounds]:"))
height = float(input("Enter height [inches]:"))

weight = convert_weight(weight)
height = convert_height(height)

calc_bmi(height, weight)
