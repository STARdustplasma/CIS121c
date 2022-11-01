# """
# Matt Priem
# 3/22/22

# This program...
# """
import random

class Die :
    def __init__(self, sides) :
        self.sides = sides
        self.roll = 1

    def roll(self) :
        self.roll = random.randint(1, self.sides)
        return self.roll

    def getValue(self) :
        return(self.roll)

    def __str__(self) :
        print(f'die has {self.sides} sides')
        print(f'die last landed on {self.roll}')
        return ''

    def __add__ (self, i) :
        self.total = i + self.roll
        return self.total

    def __gt__ (self, notself) :
        if self.total > Die.__add__(notself) :
            return 'first number bigger'
        elif self.total < Die.__add__(notself) :
            return 'other number bigger'
        else :
            return 'numbers are equal'


class Player :
    def __init__ (self,name, die1, die2) :
        self.die1 = die1
        self.die2 = die2
        self.name = name

    def rollDice(self) :
        Die.roll(self.die1)
        Die.roll(self.die2)
        self.total = Die.__add__(self.die1, self.die2)
        return self.total

    def listName(self) :
        return self.name

    def getDiceValue(self) :    
        self.total = Die.__add__(self.die1, self.die2)
        return self.total
    
    def __str__(self) :
        print(f'player: {self.name}')
        print(f'{self.die1} {self.die2}')
        return ''

class HighTwoGame :
    def __init__(self, player1, player2) :
        self.player1 = player1
        self.player2 = player2 

        
    def playOneGame(self) :
        Player.rollDice(self.player1)
        Player.rollDice(self.player2)

        print(f'{Player.listName(self.player1)} rolled a {Player.getDiceValue(self.player1)}')
        print(f'{Player.listName(self.player2)} rolled a {Player.getDiceValue(self.player2)}')

        if Player.getDiceValue(self.player1) > Player.getDiceValue(self.player2) :
            print(f'{Player.listName(self.player1)} wins! \n')
        elif Player.getDiceValue(self.player1) < Player.getDiceValue(self.player2) :
            print(f'{Player.listName(self.player2)} wins! \n')
        else :
            print('tie \n')

    def playManyGames(self, i) :
        o = 0
        p = 0
        for j in range(i) :
            Player.rollDice(self.player1)
            Player.rollDice(self.player2)
            print(f'{Player.listName(self.player1)} rolled a {Player.getDiceValue(self.player1)}')
            print(f'{Player.listName(self.player2)} rolled a {Player.getDiceValue(self.player2)}')
            print('')

            if Player.getDiceValue(self.player1) > Player.getDiceValue(self.player2) :
                o += 1
            elif Player.getDiceValue(self.player1) < Player.getDiceValue(self.player2) :
                p += 1
            else :
                print('tie \n')
        print(f'with a score of {o} to {p}...')
        if o > p :
            print(f'{Player.listName(self.player1)} wins! \n')
        elif o < p :
            print(f'{Player.listName(self.player2)} wins! \n')
        else :
                print('tie \n')
            
        


print("Game one:") 
game1 = HighTwoGame( Player("Matt", Die(6), Die(10)), Player("Ashley", Die(6), Die(10)) )
game1.playOneGame()


print("")
print("Game two:")
game2 = HighTwoGame( Player("Dexter", Die(6), Die(10)), Player("Eugene", Die(6), Die(10)) )
game2.playManyGames(3)