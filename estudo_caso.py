from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

#Definicao da estrutura do modelo. Vinculos 
model = BayesianModel([('H', 'D'), ('D', 'S'), ('D', 'E')])

#Criação das tabelas de probabilidade condicional
#variable_card define o número de valores possíveis que a variável pode assumir
#evidence_card faz a mesma coisa mas para a evidência (a quem a variavel depende)

cpd_h = TabularCPD(variable='H', variable_card=2, values=[[0.2], [0.8]])

cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.1, 0.01],[0.9, 0.99]], evidence=['H'], evidence_card=[2])

cpd_s = TabularCPD(variable='S', variable_card=2, values=[[0.8, 0.1],[0.2, 0.9]], evidence=['D'], evidence_card=[2])

cpd_e = TabularCPD(variable='E', variable_card=2, values=[[0.9, 0.05],[0.1, 0.95]], evidence=['D'], evidence_card=[2])

#Associando CPD ao modelo
model.add_cpds(cpd_h, cpd_d, cpd_s, cpd_e)

model.check_model()
