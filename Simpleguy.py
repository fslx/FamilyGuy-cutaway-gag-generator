import random


def main():

    jokes = ["Went to Vietnam",
             "Babysat the pope",
             "Kissed Vanilla Ice",
             "Fought Adolf Hitler",
             "Killed Garth Marenghi",
             "'s great great great great great great great and so forth grandfather Julius Claudius Germanicus Griffinus invaded Gaul'",
             "had a chickenfight with Homer Simpsons",
             "Got lost in the matrix", "was sendt to the Gulags in Siberia",
             "took a bag of nickels to the nuts",
             "Got drunk with Quagmire and did unspeakable things",
             "Robbed a bank",
             "Puked for hours on end",
             "Took on a dump in the street",
             "Hijacked a plane",
             "Ended up back in time",
             "Slapped Shakespeer with the notes to Romeo and Juliet",
             "Was stuck in a hole", ]
    charachter = input(
        "Choose between Peter, Lois, Bryan, Meg, Chris or Stewie: ")
    scenario = "Remember that time when"
    print(scenario + " " + charachter + " " +
          random.choice(jokes) + " ")
    exit()
