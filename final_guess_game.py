import random

PROMPT = 'What is your guess? '


QUIT = -1
QUIT_TEXT ='q'
QUIT_MESSAGE ='Thank you for playing'
CONFIRM_QUIT_MESSAGE ='Are you sure you want to quit (Y/n)? '





def confirm_quit():
    """Ask user to confirm that they want to quit
    default to yes
    Return True (yes, quit) or Falso (no, dont't quit) """
    spam =input(CONFIRM_QUIT_MESSAGE)
    if spam =='n':
        return False
    else:
        return True

def do_guess_round():
        """Choose a random number, ask the user for a guess
            check whether the guess is true
            and repeat until the user is correct"""
        computers_number = random.randint(1,100)
        number_of_guesses = 0 
        while True:
            players_guess =input(PROMPT)
            
            if players_guess == QUIT_TEXT:
                            if confirm_quit():
                                return QUIT
                            else:
                                continue 
            number_of_guesses = number_of_guesses+1 
            if computers_number ==int(players_guess):
                print('Correct!')
                return number_of_guesses 
            elif computers_number >int(players_guess):
                print('Too Low')
            else:
                print('Too High')
                
total_rounds = 0
total_guesses = 0

while True:
    total_rounds = total_rounds+1
    print("Starting round number: "+str(total_rounds))
    print("Let the guessing begin!!!")
    this_round = do_guess_round()

    
    if this_round == QUIT:
        total_rounds = total_rounds - 1
        avg = str(total_guesses/float(total_rounds))
        if total_rounds == 0:
            stats_message = 'You completed no rounds. '+\
                            'Please try again later.'
        else:
            stats_message = 'You played ' + str(total_rounds) +\
                            ' rounds, with an average of '+\
                            str(avg)
        break
    
    
    total_guesses = total_guesses+this_round
    avg =str(total_guesses/float (total_rounds))
    print("You took "+str(this_round)+" guesses")
    print("Your guessing average = "+avg)
    print("")


print(stats_message)
