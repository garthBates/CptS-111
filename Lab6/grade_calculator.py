#Garth Bates
#2/21/2018
#Cpts 111
#Lab #6, Task 1


def get_scores():
    print("Please enter the following information: \n")

    exam1 = int(input("Exam 1 score: "))
    exam2 = int(input("Exam 2 score: "))
    final_exam = int(input("Final exam score: "))
    prog_assign = int(input("Programming assignments score: "))
    zyPA = int(input("zyBooks participation activities score: "))
    zyCA = int(input("zyBooks challenge activities score: "))
    labs = int(input("Labs score: "))
    return exam1, exam2, final_exam, prog_assign, zyPA, zyCA, labs

def calc_score(exam1, exam2, final_exam, prog_assign, zyPA, zyCA, labs):
    score = .17 * exam1 + .18 * exam2 + .18 * final_exam +.25 * prog_assign + .08 *zyPA + .02 *zyCA + .12 * labs
    return score

def calc_grade(score):
    if (score >= 95):
        return "A"
    elif (score < 95 and score >= 90):
        return "A-"
    elif (score < 90 and score >= 85):
        return "B+"
    elif (score < 85 and score >= 80):
        return "B"
    elif (score < 80 and score >= 75):
        return "B-"
    elif (score < 75 and score >= 70):
        return "C+"
    elif (score < 70 and score >= 65):
        return "C"
    elif (score < 65 and score >= 60):
        return "C-"
    elif (score < 60 and score >= 50):
        return "D"
    else:
        return "F"

def main():
    exam1, exam2, final_exam, prog_assign, zyPA, zyCA, labs = get_scores()
    score = calc_score(exam1, exam2, final_exam, prog_assign, zyPA, zyCA, labs)
    grade = calc_grade(score)

    print("Your score for CptS is:", score)
    print("Your grade for CptS is:", grade)


main()

    

    
        
