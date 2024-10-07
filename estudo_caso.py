from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# define da estrutura do modelo com as novas relações
model = BayesianNetwork([('H', 'D'), ('H', 'E'), ('D', 'S'), ('E', 'S')])

# cria das tabelas de probabilidade condicional (CPDs)
# tabela de probabilidade pra H
cpd_h = TabularCPD(variable='H', variable_card=2, values=[[0.2], [0.8]])

# tabela de probabilidade condicional D dado H
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.1, 0.01], [0.9, 0.99]],
                   evidence=['H'], evidence_card=[2])

# tabela de probabilidade condicional E dado H
cpd_e = TabularCPD(variable='E', variable_card=2, values=[[0.9, 0.05], [0.1, 0.95]],
                   evidence=['H'], evidence_card=[2])

# tabela de probabilidade condicional S dado D e E
cpd_s = TabularCPD(variable='S', variable_card=2, values=[[0.8, 0.1, 0.2, 0.05],
                                                          [0.2, 0.9, 0.8, 0.95]],
                   evidence=['D', 'E'], evidence_card=[2, 2])

# associa as CPDs ao modelo
model.add_cpds(cpd_h, cpd_d, cpd_e, cpd_s)

# verifica se todas as CPDs estão associadas certo
print("Modelo é válido: ", model.check_model())

# exibi tabelas geradas
print("\nTabela de Probabilidade Condicional para H:\n", cpd_h)
print("\nTabela de Probabilidade Condicional para D dado H:\n", cpd_d)
print("\nTabela de Probabilidade Condicional para E dado H:\n", cpd_e)
print("\nTabela de Probabilidade Condicional para S dado D e E:\n", cpd_s)
