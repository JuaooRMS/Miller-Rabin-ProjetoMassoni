# Função Decomposição
# ---
# Rescreve n - 1 na forma 2^s * d 
#
# Entrada: n - Número inteiro maior que 2
# Retorno: (s,d), onde: 
# s - quantidade de fatores 2
# d - fator ímpar multiplicador
# --- 

def decomposicao(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    return s, d