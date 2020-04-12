import random


def main():

    jokes = ["Stole christmas with",
             "Babysat",
             "Kissed",
             "Fought",
             "Killed",
             "Went on that talkshow with",
             "had a chickenfight with",
             "Bash on The Simpsons with", "Gets random job with",
             "took a bag of nickels to the nuts with",
             "Got drunk with",
             "Had sex with", "Robbed a bank with", "Partied with",
             "Puked with", "Puked on",
             "Took on a dump in the street with",
             "Lost weight with",
             "Hijacked a plane with",
             "Went to war with",
             "Ended up back in time with",
             "Slapped Shakespeer with",
             "Was stuck in a hole with", ]
    charachter = input(
        "Choose between Peter, Lois, Bryan, Meg, Chris or Stewie: ")
    celeberties = input(
        "Now select a celeberty you'd like to see in the cutaway-gag: ")
    scenario = "Remember that time when"
    print(scenario + " " + charachter + " " +
          random.choice(jokes) + " " + celeberties + " ")
    exit()

