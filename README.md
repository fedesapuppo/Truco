# Truco
A little program for the game of "Truco"

This is my first project and, with the first few tools I'm learning, this is an attempt to build a little calculator for a card game. It takes six parameters: the first two parameters represent the number and the suit of one Spanish playing card, the second two represent the number and the suit of a second card, and the third two represent the number and the suit of a third card. The possible numbers are 1 trough 7 and 10 trough 12. The suits are "golds", "cups", "swords", and "clubs".
In this part of the game, the points are calculated this way:

1) If you have two or three cards of the same suit, you take the highest two, sum them up, and then add 20 to the result.
2) If all three cards are of different suits, then you take the highest value of them all and that represent your points.

The value of the cards are as follows:

Cards from 1 through 7 have their number value. 
The cards with the numbers 8 and 9 are not used in the game. 
Cards with the numbers 10 through 12 have value "0".

So, for example, the function "puntaje" is expected to return these values:

                  puntaje (num1, palo1, num2, palo2, num3, palo3)


parameters: (7, "swords", 6, "swords", 1, "swords")

should return: 33 (the highest possible outcome)

parameters: (1, "golds", 1, "cups", 1, "club")

should return: 1 (the lowest possible outcome)

parameters: (1, "clubs", 4, "clubs", 12 "clubs")

should return: 25

parameters: (12, "golds", 4, "golds", 12 "swords")

should return: 24

parameters: (10, "golds", 12, "swords", 7, "cups")

should return: 7

parameters: (10, "golds", 12, "golds", 7, "cups")

should return: 20


And that it is for now :)
