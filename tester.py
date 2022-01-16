from hangman import Game, valid_guess
from avl import AVL_Tree, TreeNode
from txt2Arr import toArr
 

if __name__ == '__main__':
    #this loop keeps the program runninng 
    keepGoing = True
    print("Please hold. We are loading the AVL tree now. We want to avoid any long waits later. Thank you for" +
    " understanding. While guessing type \"quit\" to exit the game.")
   
    #this puts our dictoinary into the tree
    dictionary = open('dictionary.txt', 'r')
    dic = toArr(dictionary)
    myTree = AVL_Tree() 
    root = None
    for item in dic:
        root = myTree.insert(root, item)

    while keepGoing:
        game = Game()
        print ("WELCOME TO HANGMAN")
        game
        #here we selected player or random word 
        mode = input("Random word or Selected word. Please type \"random\" or \"player\"\n")
        if(mode == "player"):
            userWord = input("please type an english word:\n")
            game.setWord(userWord, myTree, root)
        
        #this loop keeps the actual guess part going
        while not game.gameover:
            guess = valid_guess(game)
            if(guess == 'quit'):
                break
            else:
                game.guess_letter(guess)
                print(game)
       #here we ask the user if they want to keep playing 
        play_again = input("Play again? (y/n): ").lower()
        if "n" in play_again:
            keepGoing = False
    print ("Thanks for playing!" )
