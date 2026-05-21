import random
import time
import sys

# ==========================================
#         EFEITO DE DIGITAÇÃO
# ==========================================

def escrever(texto, velocidade=0.03):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()  # pula linha no final

# ==========================================
#           PARADOX ARENA
# ==========================================

print("╔══════════════════════╗")
print("║    PARADOX  ARENA    ║")
print("╚══════════════════════╝")
input("\nENTER para começar... ")

nome = input("Seu nome: ")
escrever(f"\nBem-vindo, {nome}!")

# ==========================================
#           ESCOLHA DE CLASSE
# ==========================================

print("\n╔══════════════════════════════════════╗")
print("║          ESCOLHA SUA CLASSE          ║")
print("╠══════════════════════════════════════╣")
print("║  1 - Guerreiro  (Vida alta, tanque)  ║")
print("║  2 - Mago       (Dano alto, frágil)  ║")
print("║  3 - Arqueiro   (Equilibrado)        ║")
print("╚══════════════════════════════════════╝")
classe = input("Escolha sua classe: ")

# Variáveis do jogador
vida_max = 0
vida = 0
defesa = 0
ataque1 = ""
ataque2 = ""
dano1_min = 0
dano1_max = 0
dano2_min = 0
dano2_max = 0
chance_critico = 0
pocoes = 2

match classe:
    case "1":
        classe_nome = "Guerreiro"
        vida_max = 220
        vida = 220
        defesa = 22
        ataque1 = "Espadada"
        dano1_min = 25
        dano1_max = 42
        ataque2 = "Golpe de Escudo"
        dano2_min = 12
        dano2_max = 22
        chance_critico = 15
    case "2":
        classe_nome = "Mago"
        vida_max = 150
        vida = 150
        defesa = 10
        ataque1 = "Bola de Fogo"
        dano1_min = 32
        dano1_max = 52
        ataque2 = "Raio de Gelo"
        dano2_min = 16
        dano2_max = 28
        chance_critico = 25
    case "3":
        classe_nome = "Arqueiro"
        vida_max = 170
        vida = 170
        defesa = 16
        ataque1 = "Flecha Certeira"
        dano1_min = 22
        dano1_max = 38
        ataque2 = "Chuva de Flechas"
        dano2_min = 8
        dano2_max = 18
        chance_critico = 30
    case _:
        escrever("Classe inválida!")
        exit()

escrever(f"\nVocê escolheu {classe_nome}!")
escrever(f"  Vida:           {vida}")
escrever(f"  Defesa:         {defesa}")
escrever(f"  Chance crítico: {chance_critico}%")
escrever(f"  Poções:         {pocoes}")
input("\nENTER para entrar na arena...")

# ==========================================
#         SISTEMA DE XP E NÍVEL
# ==========================================

xp = 0
nivel = 1
xp_proximo_nivel = 100

# ==========================================
#            LISTA DE INIMIGOS
# ==========================================

# Cada inimigo é uma lista: [nome, vida, ataque_min, ataque_max, defesa, xp_recompensa]
inimigos = [
    ["Goblin",       100, 12, 22,  5,  40],
    ["Orc",          160, 18, 30, 10,  70],
    ["Troll",        220, 22, 38, 15, 100],
    ["Dragão Negro", 300, 30, 50, 20, 150],
]

# ==========================================
#               BATALHAS
# ==========================================

for inimigo_dados in inimigos:
    inimigo_nome    = inimigo_dados[0]
    vida_inimigo    = inimigo_dados[1]
    inimigo_atk_min = inimigo_dados[2]
    inimigo_atk_max = inimigo_dados[3]
    inimigo_defesa  = inimigo_dados[4]
    inimigo_xp      = inimigo_dados[5]

    print("\n╔══════════════════════════════════════╗")
    escrever(f"  ⚔  Um {inimigo_nome} apareceu!", velocidade=0.05)
    print("╚══════════════════════════════════════╝")
    input("ENTER para batalhar...")

    inimigo_defendendo = False

    # ---------- LOOP DE COMBATE ----------
    while vida > 0 and vida_inimigo > 0:

        print("\n┌──────────────────────────────────────┐")
        print(f"│  {nome} [{classe_nome}] - Nível {nivel}")
        print(f"│  Vida: {vida}/{vida_max}  XP: {xp}/{xp_proximo_nivel}")
        print(f"│  {inimigo_nome} - Vida: {vida_inimigo}")
        print("├──────────────────────────────────────┤")
        print(f"│  1 - {ataque1}")
        print(f"│  2 - {ataque2}")
        print("│  3 - Defender")
        print(f"│  4 - Usar Poção ({pocoes} restantes)")
        print("└──────────────────────────────────────┘")
        escolha = input("Escolha: ")

        # ------ AÇÕES DO JOGADOR ------
        match escolha:

            # --- Ataque 1 ---
            case "1":
                dano = random.randint(dano1_min, dano1_max)
                critico = random.randint(1, 100) <= chance_critico
                if critico:
                    dano = dano * 2
                    escrever(f"\n⚡ CRÍTICO! Você usou {ataque1}!", velocidade=0.05)
                else:
                    escrever(f"\nVocê usou {ataque1}!")
                dano_final = max(0, dano - inimigo_defesa)
                vida_inimigo -= dano_final
                if inimigo_defesa > 0:
                    escrever(f"Dano causado: {dano_final} (após defesa do inimigo)")
                else:
                    escrever(f"Dano causado: {dano_final}")

            # --- Ataque 2 ---
            case "2":
                escrever(f"\nVocê usou {ataque2}!")
                hit1 = random.randint(dano2_min, dano2_max)
                hit2 = random.randint(dano2_min, dano2_max)
                hit3 = random.randint(dano2_min, dano2_max)
                dano_total = hit1 + hit2 + hit3
                dano_total = max(0, dano_total - inimigo_defesa)
                vida_inimigo -= dano_total
                escrever(f"Acertos: {hit1} + {hit2} + {hit3}")
                escrever(f"Dano total: {dano_total}")

            # --- Defender ---
            case "3":
                escrever("\n🛡 Você assumiu posição defensiva!")
                dano_inimigo = random.randint(inimigo_atk_min, inimigo_atk_max)
                dano_recebido = max(0, dano_inimigo - defesa * 2)
                vida -= dano_recebido
                vida = max(0, vida)
                escrever(f"{inimigo_nome} tentou causar: {dano_inimigo}")
                escrever(f"Dano recebido (com bônus de defesa): {dano_recebido}")
                continue

            # --- Poção ---
            case "4":
                if pocoes > 0:
                    cura = random.randint(40, 70)
                    vida = min(vida_max, vida + cura)
                    pocoes -= 1
                    escrever(f"\n🧪 Você usou uma poção e recuperou {cura} de vida!")
                    escrever(f"Vida atual: {vida}/{vida_max}")
                else:
                    escrever("\nVocê não tem mais poções!")
                    continue

            case _:
                escrever("Opção inválida!")
                continue

        # ------ ATAQUE DO INIMIGO ------
        if vida_inimigo > 0:
            if vida_inimigo < inimigo_dados[1] * 0.3 and random.randint(1, 100) <= 20:
                escrever(f"\n{inimigo_nome} se preparou para defender no próximo turno!")
                inimigo_defendendo = True
            else:
                dano_inimigo = random.randint(inimigo_atk_min, inimigo_atk_max)
                critico_inimigo = random.randint(1, 100) <= 10
                if critico_inimigo:
                    dano_inimigo = int(dano_inimigo * 1.5)
                    escrever(f"\n💥 {inimigo_nome} fez um ataque crítico!", velocidade=0.05)
                else:
                    escrever(f"\n{inimigo_nome} atacou!")
                vida -= dano_inimigo
                vida = max(0, vida)
                escrever(f"Você recebeu {dano_inimigo} de dano! Vida: {vida}/{vida_max}")

    # ------ RESULTADO DA BATALHA ------
    if vida <= 0:
        print("\n╔══════════════════════╗")
        escrever("  VOCÊ FOI DERROTADO...", velocidade=0.07)
        print("╚══════════════════════╝")
        escrever(f"Você chegou até o {inimigo_nome} e caiu em batalha.")
        escrever(f"Nível final: {nivel} | XP: {xp}")
        print("╔══════════════════════╗")
        print("║      GAME OVER       ║")
        print("╚══════════════════════╝")
        exit()

    # Vitória na batalha
    escrever(f"\n✅ Você derrotou o {inimigo_nome}!")
    escrever(f"+{inimigo_xp} XP!")
    xp += inimigo_xp

    # Verifica subida de nível
    while xp >= xp_proximo_nivel:
        nivel += 1
        xp -= xp_proximo_nivel
        xp_proximo_nivel = int(xp_proximo_nivel * 1.4)
        vida_max += 20
        vida = min(vida_max, vida + 30)
        defesa += 2
        dano1_min += 3
        dano1_max += 3
        dano2_min += 2
        dano2_max += 2
        escrever(f"\n🌟 SUBIU PARA NÍVEL {nivel}!", velocidade=0.05)
        escrever(f"   Vida máx: +20 | Defesa: +2 | Dano: +3")

    # Ganha poção a cada vitória (máx 3)
    if pocoes < 3:
        pocoes += 1
        escrever(f"🧪 Você encontrou uma poção! ({pocoes}/3)")

    input("\nENTER para continuar...")

# ==========================================
#          VITÓRIA TOTAL
# ==========================================

print("\n╔══════════════════════════════════════╗")
escrever("  🏆 VOCÊ VENCEU A ARENA! 🏆", velocidade=0.06)
print("╚══════════════════════════════════════╝")
escrever(f"  Herói:         {nome} [{classe_nome}]")
escrever(f"  Nível final:   {nivel}")
escrever(f"  Vida restante: {vida}/{vida_max}")
escrever(f"  XP total:      {xp}")
print("╔══════════════════════════════════════╗")
print("║         OBRIGADO POR JOGAR!          ║")
<<<<<<< HEAD
print("╚══════════════════════════════════════╝")
=======
print("╚══════════════════════════════════════╝")
>>>>>>> a4403d2bcd46949576c0afa46c89e6a9fc4f7f78
