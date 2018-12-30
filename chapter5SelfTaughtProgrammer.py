##Chapter 5 self taught programmer
#Christina Roberts

"""1. Create a list of your favorite musicians"""
fav_musicians = [ "casting crowns", "mercy me", "lauren daigle" ]


"""2. Create a list of tuples, with each tuple containing the long.
and lat. of somewhere youve lived or visited"""
homes = [ (27, 97), (48, 123), (34, 82)]

"""3. Create a dictionary that contains different attributes of you:
height, fav color, fav number"""
about_me = { "height" : "5.5", "fav_color" : "aqua", "fav_number": "27"}


"""4, Write a program that lets the user ask for your height, fav color, or
fav number, and returns the results from the dictionary you  created in the
previous challenge"""
def learn_about_me():
    about_me = { "height" : "5.5", "fav_color" : "aqua", "fav_number": "27"}
    answer = str(input("Type height, fav_color or fav_number: "))
    if answer in about_me:
        result = about_me[answer]
        print(result)


"""5. Create a dictionary mapping your fav musicians with their songs"""

artist_songs = { "casting crowns" : "who am i" , "mercy me": "even if" ,
                 "lauren daigle" : "these hands" }
