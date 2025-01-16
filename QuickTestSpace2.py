import random
tabela = []
for i in range(1000):
    tabela.append(random.randint(1,100))
print(max(tabela))
print(min(tabela))