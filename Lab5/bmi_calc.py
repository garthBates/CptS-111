#########
#Garth Bates
#Lab 5, task 4
#2/14/2018
#########

#Global Variables
kg_per_lb = 0.45359237
m_per_inch = 0.0254

#Functions
def convert_height(height):
    height = height * m_per_inch
    return height

def convert_weight(weight):
    weight = weight * kg_per_lb
    return weight

def calc_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if (bmi <= 18.5):
        return "Underweight"
    elif (bmi > 18.5 and bmi <= 24.99):
        return "Normal weight"
    elif(bmi > 25 and bmi <= 29.99):
        return "Overweight"
    elif (bmi > 30 and bmi <= 34.99):
        return Obestiy (I)
    elif (bmi > 34 and bmi <= 39.99):
        return "Normal weight"
    elif (bmi >= 40):
        return "Morbid Obesity"

def main():
    weight = float(input("Enter weight [pounds]:"))
    height = float(input("Enter height [inches]:"))

    weight = convert_weight(weight)
    height = convert_height(height)

    bmi = calc_bmi(height, weight)
    classification = classify_bmi(bmi)

    print("BMI     = ", bmi)
    print("Mass    = ", weight, " [kilograms]")
    print("Height  = ", height, " [meters]")
    print("BMI Classification = ", classification)
    

main()
