from termcolor import colored
#import os
#def clear(): os.system('cls') #on Windows System
#clear()


def main():
    print("Welcome to my Madlibs game!\n Which topic would you like to use: programming, cars, or books? \n Please "
          "enter 1, 2, or 3. Enter 9 to end program.")

    while True:
        choice = int(input())
        if choice == 9:
            print("Thank you for playing have a nice day!")
            break
        elif choice == 1:
            print("Welcome to the programming madlib! Excellent choice!")
            programmingMadlib()
          #  clear()
            main()
        elif choice == 2:
            print("Welcome to the cars madlib! Fabulous!")
            carMadlib()
            #clear()
            main()
        elif choice == 3:
            print("Welcome to the books madlib! Feeling smart? Good!")
            booksMadlib()
            #clear()
            main()
        else:
            print("Sorry that was not a valid choice! Please type 1 for programming, 2 for cars, 3 for books, or 9 to exit")
            main()


def programmingMadlib():
    adj = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous person: ")
    color = input("Choose any color you like ")
    print("Computer programming is so "+colored(adj, color)+"! It makes me so excited all the time because I love to "
          +colored(verb1, color)+"."+ "\nStay hydrated and "+colored(verb2,color)+ " like you are "
          +colored(famous_person,color)+"!"+"\n\n\n\n\n")

def carMadlib():
    adj = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous person: ")
    color = input("Choose any color you like ")
    print("Cars are so " + colored(adj, color) + "! My favorite thing to do in a car is " + colored(verb1, color) + "" \
                                                                                                                ". I always do " + colored(
        verb2,color) + " A famous person I think about when I think about cars is " +colored(famous_person,color) + "!"+"\n\n\n\n\n")

def booksMadlib():
    adj = input("Adjective: ")
    noun = input("Noun: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous author: ")
    color = input("Choose any color you like ")
    print("Books make my mind more " + colored(adj,color) + " My favorite book is " + colored(noun,color) + " I always make" \
                                                                                                   "sure I " + colored(
        verb2,color) + " when I read. My favorite author is " + colored(famous_person,color) + "!\n\n\n\n\n")


main()
