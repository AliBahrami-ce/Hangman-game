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
    def __init__(self, results=None):
      if results is None:
          self.results = []
      else:
          self.results = results

      
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
        writer.writerow(['#', 'Word', 'W/L'])

        for index, item in enumerate(self.results, start=1):
            writer.writerow([index, item[0], item[1]])

            
# p = logic()

# print(p.win('c' ,'ali', 4))