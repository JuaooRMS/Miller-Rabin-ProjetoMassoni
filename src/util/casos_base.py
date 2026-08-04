# Função casos_base
# ---
# Classifica entradas triviais para o teste
#
# Entrada: n - Número inteiro maior que 1
# Retorno: 
# True - se n for primo
# False - se n for composto
# None - se n não puder ser classificado pelos casos base
# ---

def casos_base(n):
    if n < 2:
        return False
    
    PRIMOS_BASICOS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
 
    for p in PRIMOS_BASICOS:
        if n == p:
            return True
            
        if n % p == 0:
            return False
    
    return None
