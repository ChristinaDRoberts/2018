""" This program is for teaching times tables,creating a quizzes, and printing
facts"""


import random
import sys 
import time


TEST_QUESTION = (4,6)
QUESTION_TEMPLATE = "What is %sx%s? "
LOWER = 1
UPPER = 12
MAX_QUESTIONS = 3
TIMES_TABLE_ENTRY = "%2s x %2s = %3s "
INSTRUCTIONS = """Welcome to math trainer. This application will train you
on your times tables. It can either print oneor more of the tables
for you so that you can revise (training) or it can test
your times tables. """
CONFIRM_QUIT_MESSAGE = "Are you sure you want to quit (Y/n)? "
SCORE_TEMPLATE = "You scored %s (%i%%) in %.1f seconds  "



def make_question_list(lower=LOWER, upper=UPPER, random_order=True):
    """ making a list of all possible questions for times table 1-12
    and in random order when random order = true"""
    
    
    spam =[(x+1, y+1) for x in range(lower-1,upper)
                      for y in range(lower-1,upper)]
    if random_order:
        random.shuffle(spam)
        return spam

def do_testing():
    score = 0
    start_time = time.time()
    question_list = make_question_list()
    for i, question in enumerate(question_list):
        if i >=MAX_QUESTIONS:
            break
        prompt = QUESTION_TEMPLATE%question
        correct_answer = question[0] * question[1]
        answer = input(prompt)
        if int(answer) == correct_answer:
            print("Correct!")
            score = score+1
        else:
            print("Incorrect,should have been %s"%(correct_answer))

    end_time = time.time()
    time_taken = end_time-start_time
    percent_correct = int(score/float(MAX_QUESTIONS)*100)
    print(SCORE_TEMPLATE%(score, percent_correct, time_taken))

def display_times_tables(upper=UPPER):
    """display times tables up to UPPER"""
    tables_per_line = 5
    tables_to_print = range(1, upper+1)
 
    batch = tables_to_print[:tables_per_line]
    
    tables_to_print = tables_to_print[tables_per_line:]
    while batch != []:
        for x in range (1, upper+1):
            accumulator = []
            for y in batch:
            
                accumulator.append(TIMES_TABLE_ENTRY%(y, x, x*y))
            print(" ".join(accumulator))
        print("\n") 
        batch = tables_to_print[:tables_per_line]
        tables_to_print = tables_to_print[tables_per_line:]
        break
                                   
           
def do_quit():
    """quit the application"""
    if confirm_quit():
        sys.exit()
    print("In Quit (not quitting, returning!)")

def confirm_quit():
    """Ask user to confirm that they want to quit. default to yes
    Return True (yes,quit) or Flase (no, dont quit)"""
    spam = input(CONFIRM_QUIT_MESSAGE)
    if spam == "n":
        return False
    else:
        return True
    
    
    


if __name__ == "__main__" :
    while True:
        print(INSTRUCTIONS)
        input_prompt = "Press: 1 for training,"+\
                       "2 for testing, 3 to quit.\n"
        selection = input(input_prompt)
        selection = selection.strip()
        while selection not in ["1", "2", "3"]:
            selection = input("Please type either 1, 2, or 3: ")
            selection = selection.strip()

        if selection == "1":
            display_times_tables()
        elif selection == "2":
            do_testing()
        else:
            do_quit()

