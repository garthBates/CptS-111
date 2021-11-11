######
#Lab 3 task 1
#####

def calc_harris_score (harris):
    harris_poll = harris / 2850
    return harris_poll

def calc_coaches_score (coach):
    coach_poll = coach / 1475
    return coach_poll

def calc_bcs_score(harris_poll, coach_poll, computer):
    bcs_score = (harris_poll + coach_poll + computer) / 3
    return bcs_score

harris = int(input("Enter the team's Harris Poll ranking (1 - 2850): "))
coach = int(input("Enter the team's Coaches Poll ranking (1 - 1475): "))
computer = float(input("Enter the team's computer ranking (0 - 1): "))

harris_poll = calc_harris_score(harris)
coach_poll = calc_coaches_score(coach)
bcs_score = calc_bcs_score(harris_poll, coach_poll, computer)

print()
print("Harris Poll score:", harris_poll)
print("Coaches Poll score:", coach_poll)
print("Computer ranking:", computer)
print()
print("Resulting BCS score:", bcs_score)
