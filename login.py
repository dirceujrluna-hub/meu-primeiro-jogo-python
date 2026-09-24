# 🏁 MEU PRIMEIRO JOGO - Simulador de Corrida
# Feito por você em 2 dias!

garagem = [
    {"nome": "camargo", "vel_max": 300},
    {"nome": "ferrado", "vel_max": 200},
    {"nome": "citrus", "vel_max": 100}
]

def corrida(carro):
    print(f"\n🏁 Largada com {carro['nome']} a {carro['vel_max']}km/h!")
    multas = 0
    for km in range(50, 501, 50):
        if carro['vel_max'] > 100:
            multas += 1
            print(f"{km}km - {carro['vel_max']}km/h 🚨 MULTA!")
        else:
            print(f"{km}km - {carro['vel_max']}km/h ✅ Safe")
    return multas

# Menu
print("=== MINHA GARAGEM ===")
for i, c in enumerate(garagem):
    print(f"{i} - {c['nome']} ({c['vel_max']}km/h)")

escolha = int(input("\nEscolha seu carro: "))
carro = garagem[escolha]

total_multas = corrida(carro)
print(f"\n🏁 Fim! {carro['nome']} tomou {total_multas} multas")
print(f"💰 Prejuízo: R${total_multas * 200}")
