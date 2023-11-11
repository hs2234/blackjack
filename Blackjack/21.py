import random

NAIPES = ['Paus', 'Ouros', 'Copas', 'Espadas']
VALORES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    def __init__(self):
        self.cartas = [Carta(valor, naipe) for naipe in NAIPES for valor in VALORES]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_carta(self):
        return self.cartas.pop()

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_carta(self, carta):
        self.mao.append(carta)

    def calcular_pontuacao(self):
        total = sum(carta.valor for carta in self.mao)

        for carta in self.mao:
            if total > 21 and carta.valor == 11:
                total -= 10

        return total

def jogo_21():
    jogador = Jogador("Jogador")
    computador = Jogador("Robô")
    baralho = Baralho()

    baralho.embaralhar()
    jogador.receber_carta(baralho.distribuir_carta())
    jogador.receber_carta(baralho.distribuir_carta())
    computador.receber_carta(baralho.distribuir_carta())
    computador.receber_carta(baralho.distribuir_carta())

    while True:
        print(f"\nSua mão: {' - '.join(str(carta) for carta in jogador.mao)}")
        escolha = input("Deseja pedir uma carta? (s/n): ").lower()
        if escolha == 's':
            carta = baralho.distribuir_carta()
            jogador.receber_carta(carta)
            print(f"Você recebeu a carta: {carta}")

            pontuacao_jogador = jogador.calcular_pontuacao()
            if pontuacao_jogador > 21:
                print("Perdeu, morreu estourado :(")
                return
        elif escolha == 'n':
            break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")

    while computador.calcular_pontuacao() < 17:
        computador.receber_carta(baralho.distribuir_carta())

    print(f"\nMão do Robô: {' - '.join(str(carta) for carta in computador.mao)}")
    print(f"\nSua Pontuação: {jogador.calcular_pontuacao()}")
    print(f"Pontuação do Robô: {computador.calcular_pontuacao()}")

    pontuacao_jogador = jogador.calcular_pontuacao()
    pontuacao_computador = computador.calcular_pontuacao()

    if pontuacao_jogador > 21:
        print("Perdeu, morreu estourado :(")
    elif pontuacao_computador > 21 or pontuacao_jogador == 21 or pontuacao_jogador > pontuacao_computador:
        print("Parabéns! Você ganhou do robô :)")
    elif pontuacao_jogador == pontuacao_computador:
        print("Empate! Raro, mas acontece...")
    else:
        print("Você perdeu. A casa sempre vence...")

jogo_21()
