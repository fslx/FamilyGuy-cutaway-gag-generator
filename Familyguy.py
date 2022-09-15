import random


def main():

    jokes = ["Stole christmas with",
             "Babysat",
             "Kissed",
             "Fought",
             "Went on that talkshow with",
             "had a chickenfight with",
             "Bash on The Simpsons with", "Gets random job with",
             "Lost weight with",
             "Hijacked a plane with",
             "Went to war with",
             "Ended up back in time with",
             "Slapped Shakespeer with",
             "Was stuck in a hole with", ]
    charachter = ["Peter", "Lois","Bryan","Meg","Chris", "Stewie"]
    
    user_input_by_integer_choices = int(input("Choose between Peter: 1, Lois: 2, Bryan: 3, Meg: 4, Chris: 5 or Stewie: 6 :  "))
    person_of_choice = str(input("Now input the name of any person you'd like to see in the cutaway-gag: "))
    match user_input_by_integer_choices:
        case 1:
            return charachter[0]
        case 2:
            return charachter[1]
        case 3:
            return charachter[2]
        case 4:
            return charachter[3]
        case 5:
            return charachter[4]
        case  6:
            return charachter[5]
        case 7:
            return 0

    scenario = "Remember that time when"
    
    print(scenario + " " + user_input_by_integer_choices + " " +
          random.choice(jokes) + " " + person_of_choice + " ")
    exit()

main()
