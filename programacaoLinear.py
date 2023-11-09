from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus

# Dias da semana
dias = list(range(1, 8))

# Número necessário de funcionários em cada dia
necessarios = {1: 17, 2: 13, 3: 15, 4: 19, 5: 14, 6: 16, 7: 11}

# Criação do problema de minimização
problema = LpProblem("Minimizacao_Funcionarios", LpMinimize)

# Criação das variáveis de decisão
variaveis = LpVariable.dicts("Funcionarios", dias, cat='Integer')

# Função objetivo
problema += lpSum(variaveis[i] for i in dias), "Minimizar_Funcionarios"

# Restrições
for i in dias:
    # Ajuste para evitar KeyErrors
    j_range = range(i, min(i + 5, 8))
    problema += lpSum(variaveis[j] for j in j_range) >= necessarios[i], f"Restricao_{i}"

# Resolvendo o problema
problema.solve()

# Exibindo os resultados
print(f"Status: {LpStatus[problema.status]}")
print(f"Número mínimo de funcionários contratados: {int(problema.objective.value())}")

for i in dias:
    print(f"x{i} = {int(variaveis[i].value())}")


# Status: Optimal
# Número mínimo de funcionários contratados: 33
# x1 = 9
# x2 = 9
# x3 = -4
# x4 = 5
# x5 = -2
# x6 = 5
# x7 = 11