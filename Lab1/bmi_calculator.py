#Garth Bates
#1/17/2018
#Cpts 111
#Lab #1, Task 3


weight = float(input("Enter weight [pounds]:"))
height = float(input("Enter height [inches]:"))

height = height * 0.0254
weight = weight * 0.45359237

bmi = weight / (height ** 2)

print("BMI     = ", bmi)
print("Mass    = ", weight, " [kilograms]")
print("Height  = ", height, " [meters]")
