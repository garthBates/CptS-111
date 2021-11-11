#Garth Bates
#1/17/2018
#Cpts 111
#Lab #1, Task 4

print("Please enter the following information: \n")

exam_1 = int(input("Exam 1 score: "))
exam_2 = int(input("Exam 2 score: "))
final_exam = int(input("Final exam score: "))
prog_assign = int(input("Programming assignments score: "))
zyPA = int(input("zyBooks participation activities score: "))
zyCA = int(input("zyBooks challenge activities score: "))
labs = int(input("Labs score: "))

class_score = .17 * exam_1 + .18 * exam_2 + .18 * final_exam +.25 * prog_assign + .08 *zyPA + .02 *zyCA + .12 * labs


print("Your score for Cpts 11 is: ", class_score) 
