import csv

hangman_ascii = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

class logic():
        
    def win(self, guess, game_word, attempt):
      if guess in game_word: 
        hangman = hangman_ascii[attempt]
        return True, hangman, attempt
      
      else:
        attempt += 1
        hangman = hangman_ascii[attempt]
        return False, hangman, attempt
        
    def save_results(self):
      with open('save.csv', mode='w', newline='', encoding='utf-8') as file:
          writer = csv.writer(file)
            
            
# p = logic()

# print(p.win('c' ,'ali', 4))