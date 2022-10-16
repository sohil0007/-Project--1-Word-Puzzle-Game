import random

name = input("What is your name? ")
print("Good Luck ! ", name)


words = {'rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board'}

words_list = ['nbowrai', 'mcoptuer', 'csiecne', 'morpgraming', 'tphyno', 'themamaicst', 'layper', 'ondiciont', 'verrees', 'awtre', 'draob']

def word_puzzle(words_list):
    random_list = random.sample(words_list,5)

    score = []

    for e in random_list:
        print("Arrange the letters to form a valid word:",e)
        ans = input("answer:")
        if ans in words:
            print("Correct")
            score.append(1)

        else:
            print("Wrong")
            score.append(-1)

    print("Net Score is",sum(score))            
                        
while True:
    if input("Do you want to continue the game[y/n]:")=="y":
        word_puzzle(words_list)

    else:
        break                           