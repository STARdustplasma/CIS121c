import playOneGame

print("Game two:")
game2 = playOneGame.HighTwoGame( playOneGame.Player("Dexter", playOneGame.Die(6), playOneGame.Die(10)), playOneGame.Player("Eugene", playOneGame.Die(6), playOneGame.Die(10)) )
game2.playManyGames(3)