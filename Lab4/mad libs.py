############
#Garth Bates
#CS 111
#Lab 4, task 4
#2/7/2018
############

def get_sent_part():
    sent_part = input("Enter part of speech: ")
    return sent_part

def build_sentence(verb, noun1, noun2, noun3, noun4, adj1, adj2, adj3):
    print("A", noun1, "was an undead,", noun2, ", usually an increadibly powerful", noun3, "\nor king has employed", adj1, "magic to", verb, "his", noun4, "\nto his own", adj2, "corpse, thus achieving a", adj3, "form\nof immortality.")

def main():
    print("Welcome to Mad-libs!\n Enter one verb, four nouns, and three adjectives respectivly")
    verb = get_sent_part()
    noun1 = get_sent_part()
    noun2 = get_sent_part()
    noun3 = get_sent_part()
    noun4 = get_sent_part()
    adj1 = get_sent_part()
    adj2 = get_sent_part()
    adj3 = get_sent_part()
    build_sentence(verb, noun1, noun2, noun3, noun4, adj1, adj2, adj3)

main()
