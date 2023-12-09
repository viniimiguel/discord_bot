import random
import time

class Forca:
    def __init__(self):
        self.word = []
        self.guess = ["-"]
        self.max_attempts = 6
        self.attempts = 0
        self.qtl = 0

    def main(self):
        self.add_words()

    def add_words(self):
        try:
            with open("palavras.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                lines = [line.strip() for line in lines]
                print(lines)
                if lines:
                    l_lines = len(lines)
                    self.qtl += l_lines
                    print(self.qtl)
            
                    rd = random.randint(1, self.qtl)
                    print(rd)

                    self.word.append(lines[rd])

                    print(self.word)
        except:
            print("nao foi possivel executar esta ação tente novamente.")

    def start_game(self):
        pass
                
            


forca = Forca()
forca.main()
