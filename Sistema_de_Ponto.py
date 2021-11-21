import time


class Horario:

    def __init__(self, hour, minute, second):

        self.h = hour
        self.m = minute
        self.s = second

    def __sub__(self, other):
        '''
        Retorna um intervalo de tempo entre o primeiro horário e o segundo.
        '''
        hora = self.h - other.h
        minuto = self.m - other.m
        segundo = self.s - other.s

        # pressupondo que sempre receberemos um input maior primeiro
        while segundo < 0:
            minuto -= 1
            segundo += 60

        while minuto < 0:
            hora -= 1
            minuto += 60

        while hora < 0:
            hora += 24

        return Horario(hora, minuto, segundo)

    def __gt__(self, other):
        '''
        Compara se o primeiro horário é maior que o segundo.
        '''

        if self.h > other.h or (self.h == other.h and self.m > other.m) or (
                self.h == other.h and self.m == other.m and self.s > other.s):
            return True
        else:
            return False


class Sistema_de_Ponto:

    def __init__(self):
        self.diaria = {}

    def bater_ponto(self):

        hour = int(input("Insira a hora: "))
        minute = int(input("Insira o minuto: "))
        second = int(input("Insira o segundo: "))

        # aqui usei o esquema de copiar  para um dicionário os objetos instanciados pelos usuarios,
        # botando como chave cada batida de ponto

        batida_de_ponto = Horario(hour, minute, second)
        self.diaria[(len(self.diaria) + 1)] = batida_de_ponto

        if len(self.diaria) == 1:
            print(f"Horário de entrada: {self.diaria[1].h:02d}:{self.diaria[1].m:02d}:{self.diaria[1].s:02d}")

        elif len(self.diaria) == 2:
            print(f"Horário de saída para almoço: {self.diaria[2].h:02d}:{self.diaria[2].m:02d}:{self.diaria[2].s:02d}")

        elif len(self.diaria) == 3:
            comparacao = self.diaria[3] - self.diaria[2]

            # comparando o intervalo entre o retorno do almoço e saída para almoço para verificar
            # se esse intervalo é de pelo menos 1 hora.
            if comparacao < (Horario(1, 0, 0)):
                print(
                    f"Você deve aguardar {(Horario(1, 0, 0) - comparacao).m:02d} minuto(s) e {(Horario(1, 0, 0) - comparacao).s:02d} segundo(s) para retornar do almoço.")
                self.diaria.pop(3)
            else:
                print(
                    f"Horário de retorno do almoço: {self.diaria[3].h:02d}:{self.diaria[3].m:02d}:{self.diaria[3].s:02d}")

        elif len(self.diaria) == 4:
            comparacao = self.diaria[4] - self.diaria[1] - (self.diaria[3] - self.diaria[2])

            if (comparacao.h > 10) or (comparacao.h == 10 and (comparacao.m > 0 or comparacao.s > 0)):
                print("Aê vacilão, da próxima vez que você trabalhar mais que 10 horas o CEO vai pessoalmente")
                print("na sua casa sair no soco contigo.")
                print(
                    f"Você trabalhou {comparacao.h:02d} hora(s), {comparacao.m:02d} minuto(s) e {comparacao.s:02d} segundo(s).")
            else:
                print(
                    f"Você trabalhou {comparacao.h:02d} hora(s), {comparacao.m:02d} minuto(s) e {comparacao.s:02d} segundo(s). Tenha um ótimo descanso!")

            self.diaria.clear()

    def run(self):

        print('=' * 45)
        print('Bem-vindo ao Sistema de Ponto da Let\'s Code'.center(45))
        print('=' * 45)

        print("\n1 - Bater ponto.")
        print("2 - Sair.")

        time.sleep(0.5)

        opcao = int(input("\nEscolha uma opção: \n"))

        while opcao != 2:

            if opcao == 1:
                self.bater_ponto()

            elif opcao == 2:
                break

            else:
                print("Opção inválida.")

            opcao = int(input("\nEscolha uma opção: \n"))

        print("\nAté logo.")

        # O que esse código não faz:
        # 1. lidar com valores de input fora do que se espera de um valor de horario.
        # 2. Mensagem personalizada para jornadas de trabalho em horários não convencionais.

    # Sistema_de_Ponto().run() para rodar

Sistema_de_Ponto().run()
