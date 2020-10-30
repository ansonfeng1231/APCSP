import random


def ball():
    query = input("Ask a question: ").strip().capitalize()
    timer = 1
    while timer < 5:
        print("Thinking... ")
        timer = timer + 1

    answers = ["Look to the person on your right for guidance.",
               "The first person you make eye contact with will have the answers you seek.",
               "Play Minesweeper 10 times, and if you lose even once then there is no definitive answer.",
               "May the Force be with you in your pursuit of the truth, because I certainly am not.",
               "You already know the answer.",
               "Go sit on the toilet and meditate for 15 minutes before asking again.",
               "Your brain is incapable of comprehending the answer.",
               "There are no answers, there are no truths. There are only bad Python programs."]

    print("Query: " + query)
    print("Answer: " + random.choice(answers))
    cont = input("Would you like to ask another question? (y/n) ").strip().lower()
    if cont == "n":
        print("Understandable, have a nice day.")
    else:
        ball()


ball()
