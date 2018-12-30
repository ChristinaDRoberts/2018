fruit = ['apple' , 'banana', 'clementine' , 'dragon fruit']
length = len(fruit)
for x in range (0, length):
    print('the fruit at index %s is %s' % (x, fruit[x]))




numbers = [5, 4, 10, 30, 22]
print(max(numbers))


strings = 's,t,r,i,n,g,S,T,R,I,N,G,'
print(max(strings))

pine = 'a,f,l,j,r,C,H,R,I,W'
print(len(pine))

print(max(10, 300, 450, 50, 90))

print(max(25, 255, 475, 10, 900))

numbers = [5, 4, 10, 30, 22]
print(min(numbers),max(numbers))

guess_this_number = 61
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
    print('Boom! You all lose')
else:
    print('You win!')

for x in range(0, 5):
          print(x)

print(list(range(0,5)))


count_by_twos = list(range(0, 30, 2))
print(count_by_twos)

count_down_by_twos = list(range(40, 10, -2))
print(count_down_by_twos)

count_by_threes =list(range(0, 22, 3))
print(count_by_threes)

my_list_of_numbers = list(range(0, 500, 50))

print(my_list_of_numbers)
print(min(my_list_of_numbers))
print(max(my_list_of_numbers))
print(len(my_list_of_numbers))
print(sum(my_list_of_numbers))



