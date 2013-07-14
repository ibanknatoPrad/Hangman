# A simple hangman game programmed in Python 3
#
# You need to have Python 3 installed on your system to be able to run this game.
# Tested on Python 3.3.2.
#
# The game prompts the user to enter a letter to start guessing a word.
# 11 incorrect guesses are allowed, after the 11th, hangman is hanged and the game is over.
# You can enable/disable audio output (see output function)
#
# TODO
# - retrieve words-to-be-guessed from a file (with minimum length of e.g. 5 letters/word)
# - build hangman (ASCII graphics)
# - check for multiple submissions of correct (!) guesses
# - voice output for placeholder word
#
# Further ideas:
# - let user guess the entire word
# - allow phrases and words with hyphens

import random # module for randomisation
from os import system # enable command line functions

def stringtogether(thislist): # function to string together elements in a list
	for element in thislist:
		print(element,end='')
	print()

def output(text,voice='true',printit='true'):
	# set voice to 'false' to suppress audio output
	if printit == 'true':
		print(text)
	if voice == 'true':
		system('say -r 160 %s' % (text))		

mywords = ["cherry", "summer", "winter", "programming", "hydrogen", "Saturday",
			"unicorn", "magic", "artichoke", "juice", "hacker", "python", "Neverland",
			"baking", "sherlock", "troll", "batman", "japan", "pastries", "Cairo",
			"Vienna", "raindrop", "waves", "diving", "Malta", "cupcake", "ukulele"]

text = "Let us play hangman: guess the word!"
output(text)

theword = random.choice(mywords).upper()

possibletries = 11 # 11 incorrect guesses are allowed
placeholder = list("-"*len(theword)) # a list consisting of placeholder characters
guessedletters = '' # string for incorrectly guessed letters
tryword = 'tries'

stringtogether(placeholder) # show blank word

while possibletries > 0:

	text = "Please pick a letter: "
	output(text,printit='false')
	pickedletter = input(text)

	if not pickedletter.isalpha() : # don't allow digits, special characters
		text = "Sorry, but that was not a letter! Try again.".format(pickedletter)
		output(text)

	elif pickedletter.upper() in guessedletters: # no multiple guesses of same letter
		text = "You already guessed the letter '{}'!".format(pickedletter.upper())
		output(text)

	else:
		pickedletter = pickedletter.upper() # uppercase all input (better for say)

		if pickedletter in theword.upper():
			
			# replace placeholder letters with correctly guessed ones
			letterposition = 0
			for letterexists in theword.upper():
				if letterexists == pickedletter:
					placeholder[letterposition] = theword[letterposition]
				letterposition += 1

			stringtogether(placeholder)

			text = "You guessed correctly, well done!"
			output(text)


		else:
			# add incorrect letters to guessedletters
			guessedletters += pickedletter			
			possibletries -= 1

			text="Sorry, '{}' is an incorrect guess!".format(pickedletter.upper())
			output(text)

			if (guessedletters != '') and (possibletries > 0):
				if possibletries == 1:
					tryword = 'try' 

				text = "You have {} {} left.".format(possibletries,tryword)
				output(text)
				text = "Incorrectly guessed letters so far: " +guessedletters+ "."
				output(text)

				stringtogether(placeholder)

		if not "-" in placeholder:
			text = "We have a winner! Thanks for playing. :)"
			output(text)
			break

else:
	text = "\nGame over. :( "
	output(text)

text = "The word we you were looking for was: " +theword+ "."
output(text)
