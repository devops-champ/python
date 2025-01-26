#mimicing three cup monte game using functions.
#we will learn that we can take results of one function and often use that as input to another function.


from random import shuffle

#shuffle the list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


#player guess
def player_guess():
    guess=''
    
    while guess not in ['0','1','2']:
        guess=input("pick a number: 0,1,or 2 \n")
    return int(guess)
    
#check the guess
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("correct")
        print(mylist)
    else:
        print("incorrect")
        print(mylist)


#initial list
mylist = ['','','O']


#check guess
check_guess(shuffle_list(mylist), player_guess())