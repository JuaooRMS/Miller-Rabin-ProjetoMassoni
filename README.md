Projeto da Disciplina de FMCC2

## 📚 Teste de Miller-Rabin

O teste Miller-Rabin, desenvolvido pelos matemáticos Gary Miller e Michael Rabin, é um teste probabilístico aplicado para verificar a primalidade de um número $n$. Ao contrário dos testes determinísticos mais simples, ele consegue analisar números muito grandes de forma eficiente.

### 🔎 Confiabilidade

Para um número $n$ composto, a probabilidade $n$ ser taxado erroneamente como primo em uma única rodada de teste é de 25%.
Se n passa pelo $k$ vezes, a probabilidade de erro é reduzida de forma exponencial.

- Para $k$ rodadas de teste: $$P(\text{erro}) \le \left(\frac{1}{4}\right)^k$$

## 🧮 Fundamentação Algébrica

Se $n$ é um número primo com relação a base $a$ (testemunha), então:

- $a^d \equiv 1 \pmod{n}$

ou $\exists r  \in ℤ | 0 \le r < s$, tal que

- $a^{2^r \cdot d} \equiv -1 \pmod{n}$
