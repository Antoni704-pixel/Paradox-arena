print("|------------------|")
print("|   Paradox Arena  |")
print("|------------------|")

input("ENTER para começar... ")
nome = input("Seu nome: ")

print(f"Bem-vindo, {nome}!")

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
dano1 = 0
dano2 = 0

match classe:

    case "1":
        classe_nome = "Guerreiro"
        vida = 200
        defesa = 20
        ataque1 = "Espadada"
        dano1 = 35
        ataque2 = "Giro"
        dano2 = 45

    case "2":
        classe_nome = "Mago"
        vida = 150
        defesa = 10
        ataque1 = "Fogo"
        dano1 = 40
        ataque2 = "Gelo"
        dano2 = 50

    case "3":
        classe_nome = "Arqueiro"
        vida = 130
        defesa = 15
        ataque1 = "Flecha"
        dano1 = 30
        ataque2 = "Chuva"
        dano2 = 55

    case _:
        print("Classe inválida!")
        exit()

print(f"Você escolheu {classe_nome}!")
print("Vida:", vida)

# Inimigo
vida_goblin = 120
ataque_goblin = 25

print("Um Goblin apareceu!")

# Combate
while vida > 0 and vida_goblin > 0:

    print("Sua vida:", vida)
    print("Vida do Goblin:", vida_goblin)

    print("1 -", ataque1)
    print("2 -", ataque2)
    print("3 - Defender")

    escolha = input("Escolha: ")

    match escolha:

        case "1":
            vida_goblin -= dano1
            print("Você atacou!")

        case "2":
            vida_goblin -= dano2
            print("Ataque forte!")

        case "3":
            dano = ataque_goblin - defesa

            if dano < 0:
                dano = 0

            vida -= dano
            print("Você defendeu!")
            print("Dano recebido:", dano)
            continue

        case _:
            print("Opção inválida!")
            continue

    if vida_goblin > 0:
        vida -= ataque_goblin
        print("O Goblin atacou!")

# Resultado
if vida > 0:
    print("Você venceu!")
else:
    print("Você perdeu!")
    
    