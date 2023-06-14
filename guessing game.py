#!/usr/bin/env python

#Guessing game
import random

def main():
    #Game explanation
    """Start a music genre guessing game."""
    print("Guess The Music Genre!")
    print("You only have 3 limit of guesses only.")

    #Keep track of guesses
    guess_count = 0
    guess_limit = 2

    print("===============================================================================================")

    #Show a list of choices
    a = [ 'Pop Music' ,'Funk Music' ,'Rock Music' ,'Kpop Music' ,'Jpop Music' ,'Country Music' ,'Instrumental Music' ]
    print("List of music genre you can guess from:",*a, sep = "\n")

    #Game Variables
    music_genre =[
        "Pop Music",
        "Funk Music",
        "Rock Music",
        "Kpop Music",
        "Jpop Music",
        "Country Music",
        "Instrumental Music"  
         ]
    
    print("===============================================================================================","\n")

    
       
    x = random.choice(music_genre,)
    guess = None

    #Game engine
    while x != guess:

        guess = str((input("What music genre am i?: " )))

        if guess_count >= guess_limit:
            print("Oh no!Your guess limit is out...","\n")
            break

        #Hints for music genre
        if x == 'Pop Music':
            print("hint:has catchy melody and lyrics")
        elif x == 'Funk Music':
            print("hint:has strong bass lines,or music lines played by low-pitched instruments and has a heavy syncopated")
        elif x == 'Rock Music':
            print("hint:music that emerged in the 1950s and is defined as a form of music with a strong beat")
        elif x == 'Kpop Music':
            print("hint:has cathcy melody and intense synchronized choreography accompanied with equally intense visuals")
        elif x == 'Jpop Music':
            print("hint:a combination of traditional Japanese music and Western pop music")
        elif x == 'Country Music':
            print("hint:honky-tonk music with simple form, folk lyrics and harmonies accompied by instruments as banjos and fiddles")
        else:
            print("hint:it just involves instruments with no singing")

        #If the answer wrong, guess count will be added by 1
        guess_count += 1

        #The ouput for player guesses
        if x == guess:
            print("Congratulation! I am {}. You got it right :].".format(guess),"\n")
            break
        else:
            print("Oops...I am not {}.Try again!<3".format(guess),"\n")

main()