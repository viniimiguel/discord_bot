import random
import time

class Forca:
    def __init__(self):
        self.word = ""
        self.guess = ["-"]
        self.max_attempts = 6
        self.attempts = 0
        self.qtl = 0

    def main(self):
        self.add_words()
        self.game_define()

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

                    self.word = lines[rd]

                    print(self.word)
        except:
            print("nao foi possivel executar esta ação tente novamente.\n")

    def question(self):
        inpt = input("digite uma letra: ")

        
        print(f"tentativa: {self.attempts}. \n")
        print(f"voce tem: {self.max_attempts} vidas.\n")
        print(palavra)


        if inpt[0] in self.word:
            print(f"voce acertou a letra {inpt[0]}\n")
            indices = [indice for indice, letra in enumerate(self.word) if letra == inpt[0]]
            for indice in indices:
                self.guess[indice] = inpt[0]
                if "-" not in self.guess:
                    print(f"voce venceu a palavra era {self.word}")
                    exit()

            print(indices)
            print(self.guess)
            self.attempts += 1
        
        elif self.attempts == 6:
            print("sua ultima chance.\n")
            end = input("digite qual foi a palavra?: \n")
            if end != self.word:
                print(f"voce errou! a palavra era {self.word}\n")
            elif end == self.word:
                print("voce venceu!\n")
        
        elif self.attempts >= 7:
            print(f"voce perdeu a palavra era: \n{self.word}")
            exit()
            
        elif inpt[0] not in self.word:
            print(f"{inpt[0]} nao existe na palavra.\n")
            self.attempts += 1
            self.max_attempts -= 1


    def game_define(self):
        global palavra

        lword = len(self.word)
        self.guess = ["-"] * lword
        palavra = "".join(self.guess)

        print(palavra)
        print(self.word)

        while self.attempts < 7:
            self.question()

        print(f"Você perdeu! A palavra era: {self.word}")
        exit()

forca = Forca()
forca.main()
