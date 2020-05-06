import random


class Forca():
    with open('palavras.txt', 'r') as arquivo:
        lista = []
        dados = arquivo.readlines()
        for i in dados:
            lista.append(i.strip())

    def __init__(self):

        self.palavra = random.choice(Forca.lista).lower()
        self.letraerro = []
        self.letracorreta = []
        self.acerto = False
        self.tentativa = 0
        self.forca = [' +---+', ' |   |', '     |', '     |', '     |', '     |', '=========']
        self.corpo = [' O   |', ' |   |', '(|   |', '(|)  |', '(    |', '( )  |']
        self.sub = ''

    def letra(self):

        while True:

            jogo.desenho()

            print('Palavras: ', end='')
            for z in self.palavra:
                if z in self.letracorreta:
                    print(z, end='')
                else:
                    print('_', end='')
            print(f'\n\nLetras erradas:')
            for x in self.letraerro:
                print(x)
            print(f'\nLetras Corretas:')
            for y in self.letracorreta:
                print(y)
            c = 0
            for w in self.palavra:
                if w in self.letracorreta:
                    c += 1
            if c == len(self.palavra):
                print('Parabens você ganhou')
                break
            if len(self.letraerro) == 6:
                print(f'Game Over! Você perdeu, a palavra era {self.palavra}.')
                break
            self.letra = str(input('\nDigite uma letra:')).lower()
            if self.letra in self.palavra:
                self.letracorreta.append(self.letra)
                self.acerto = True
            else:
                self.letraerro.append(self.letra)
                self.acerto = False

            self.tentativa+=1

    def desenho(self):

        if self.tentativa == 0:
            for i in self.forca:
                print(i)

        elif self.acerto == False and len(self.corpo) == 6:

            self.sub = self.corpo[0]
            self.forca[2] = self.sub
            self.corpo.remove(self.sub)
            for i in self.forca:
                print(i)

        elif self.acerto == False and len(self.corpo) == 3:

            self.sub = self.corpo[0]
            self.forca[3] = self.sub
            self.corpo.remove(self.sub)
            for i in self.forca:
                print(i)

        elif self.acerto == False and len(self.corpo) == 4:
            self.sub = self.corpo[0]
            self.forca[3] = self.sub
            self.corpo.remove(self.sub)
            for i in self.forca:
                print(i)

        elif self.acerto == False and len(self.corpo) == 5:
            self.sub = self.corpo[0]
            self.forca[3] = self.sub
            self.corpo.remove(self.sub)
            for i in self.forca:
                print(i)


        elif self.acerto == False and len(self.corpo) == 2 or len(self.corpo) == 1:

            self.sub = self.corpo[0]
            self.forca[4] = self.sub
            self.corpo.remove(self.sub)
            for i in self.forca:
                print(i)
        else:
            for i in self.forca:
                print(i)


jogo = Forca()
jogo.letra()
