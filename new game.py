import random

print("|------------------|")
print("|   Paradox Arena  |")
print("|------------------|")

input("ENTER para começar... ")

nome = input("Seu nome: ")

print("Bem-vindo,", nome + "!")

# Escolha da classe
print("1 - Guerreiro")
print("2 - Mago")
print("3 - Arqueiro")

classe = input("Escolha sua classe: ")

# Variáveis
vida = 0
defesa = 0

ataque1 = ""
ataque2 = ""

dano1_min = 0
dano1_max = 0

dano2_min = 0
dano2_max = 0

# Classes
match classe:

    case "1":
        classe_nome = "Guerreiro"

        vida = 200
        defesa = 20

        ataque1 = "Espadada"
        dano1_min = 25
        dano1_max = 40

        ataque2 = "Lanças"
        dano2_min = 10
        dano2_max = 20

    case "2":
        classe_nome = "Mago"

        vida = 150
        defesa = 10

        ataque1 = "Fogo"
        dano1_min = 30
        dano1_max = 50

        ataque2 = "Gelo"
        dano2_min = 15
        dano2_max = 25

    case "3":
        classe_nome = "Arqueiro"

        vida = 130
        defesa = 15

        ataque1 = "Flecha"
        dano1_min = 20
        dano1_max = 35

        ataque2 = "Chuva de Flechas"
        dano2_min = 8
        dano2_max = 18

    case _:
        print("Classe inválida!")
        exit()

print("Você escolheu", classe_nome + "!")
print("Vida:", vida)
print("Defesa:", defesa)

# Inimigo
vida_goblin = 120
ataque_goblin_min = 15
ataque_goblin_max = 30

print("Um Goblin apareceu!")

# Combate
while vida > 0 and vida_goblin > 0:

    print("------------------")
    print("Sua vida:", vida)
    print("Vida do Goblin:", vida_goblin)

    print("1 -", ataque1)
    print("2 -", ataque2)
    print("3 - Defender")

    escolha = input("Escolha: ")

    match escolha:

        case "1":

            dano = random.randint(dano1_min, dano1_max)

            vida_goblin -= dano

            print("Você usou", ataque1 + "!")
            print("Dano causado:", dano)

        case "2":

            # vários danos pequenos
            hit1 = random.randint(dano2_min, dano2_max)
            hit2 = random.randint(dano2_min, dano2_max)
            hit3 = random.randint(dano2_min, dano2_max)

            dano_total = hit1 + hit2 + hit3

            vida_goblin -= dano_total

            print("Você usou", ataque2 + "!")
            print("Acertos:", hit1, hit2, hit3)
            print("Dano total:", dano_total)

        case "3":

            dano_goblin = random.randint(ataque_goblin_min, ataque_goblin_max)

            dano_recebido = dano_goblin - defesa

            if dano_recebido < 0:
                dano_recebido = 0

            vida -= dano_recebido

            print("Você se defendeu!")
            print("Goblin tentou causar:", dano_goblin)
            print("Dano recebido:", dano_recebido)

            continue

        case _:
            print("Opção inválida!")
            continue

    # Ataque do Goblin
    if vida_goblin > 0:

        dano_goblin = random.randint(ataque_goblin_min, ataque_goblin_max)

        vida -= dano_goblin

        print("O Goblin atacou!")
        print("Goblin causou", dano_goblin, "de dano!")

# Resultado
print("==================")

if vida > 0:
    print("Você venceu!")
    print("Vida restante:", vida)

else:
    print("Você perdeu!")

print("==================")