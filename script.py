# 1. Entrada de dados com validação básica
equipamento = input("Digite o nome ou ID do equipamento: ").strip()

try:
    consumo_kwh = float(input("Digite o consumo mensal do aparelho (em kWh): "))
    if consumo_kwh < 0:
        print("\n❌ Erro: O consumo não pode ser um valor negativo.")
        return
except ValueError:
    print("\n❌ Erro: Por favor, insira um valor numérico válido para o consumo.")
    return

# 2. Constante de Tarifa e Processamento Matemático
TARIFA_POR_KWH = 0.75
custo_total = consumo_kwh * TARIFA_POR_KWH

# 3. Regra de Negócio (Estrutura Condicional)
LIMITE_EFICIENCIA = 150.0
if consumo_kwh <= LIMITE_EFICIENCIA:
    status_eficiencia = "🌿 EFICIENTE (Consumo dentro da meta)"
else:
    status_eficiencia = "🚨 ALTO CONSUMO (Requer manutenção ou troca)"

# 4. Exibição do relatório final formatado
print("\n" + "-" * 45)
print(f" RELATÓRIO DO EQUIPAMENTO: {equipamento.upper()}")
print("-" * 45)
print(f" Consumo medido:    {consumo_kwh:.2f} kWh")
print(f" Custo financeiro:  R$ {custo_total:.2f}")
print(f" Classificação:     {status_eficiencia}")
print("-" * 45)
print(" Análise de dados concluída com sucesso!\n")
