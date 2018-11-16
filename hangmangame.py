'''
Programmer:
Date:
Description:
'''
import random


class Hangman:
    def __init__(self, words):
        self.words = ("temp")
        self.word = self.words[0] #change to random index later
        self.guesslimit = int(len(self.word)*2)
        self.status = []
        self.guesses = []
        for i in self.word:
            self.status.append(False)
        print("There are", len(self.word), "letters in the word")
        
    def userGuess(self):
        return((input("Enter a letter to guess > ")).lower()[0])
    def checkGuess(self, guess):
        if guess in guesses:
            print("You already guessed that one!")
        occurrence = 0
        count = 0
        hint = "You have: "
        self.guesslimit-=1
        for i in self.word:
            if guess == i: #if the guess is in the word
                self.status[count] = True #set its status to be guessed
                occurrence+=1
            if self.status[count]:
                hint+=i
            else:
                hint+=" _"
            count+=1
        if occurrence == 0:
            print("\nThat letter is not in the word.")
        else:
            print("\nThe letter " + guess + " appears " + str(occurrence)
                  + " times.")
        print(hint)
    def giveHint(self, count, letter):
        print(count)
        if self.status[count]:
            self.hint+=letter
        else:
            self.hint+=" _"
    def winner(self):
        win = True
        for i in self.status:
            if i == 0:
                win = False
        if win:
            print("Congratulations, you guessed the word!")
        return win

            
    def run(self):
        win = self.winner()
        while self.guesslimit != 0 and not win:
            self.checkGuess(self.userGuess())
            win = self.winner()
        if not win:
            print("Sorry, all out of guesses")


def main():
    game = Hangman(words)
    game.run()

main()
        
    
        
