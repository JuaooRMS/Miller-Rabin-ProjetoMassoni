# 🔐 Teste de Primalidade de Miller-Rabin

Projeto desenvolvido para a disciplina de **Fundamentos de Matemática para Ciência da Computação II (FMCC2)**.

O objetivo do projeto é implementar e analisar o **Teste de Miller-Rabin**, um algoritmo probabilístico utilizado para verificar se um número inteiro é primo.

---

# 📚 Introdução

O **Teste de Miller-Rabin**, desenvolvido pelos matemáticos **Gary Miller** e **Michael Rabin**, é um dos algoritmos mais eficientes para testar a primalidade de números inteiros muito grandes.

Diferentemente dos testes determinísticos tradicionais, como a divisão por todos os possíveis divisores até √n, o Miller-Rabin utiliza propriedades da aritmética modular para realizar a verificação de maneira eficiente.

O algoritmo é amplamente utilizado em aplicações de criptografia, como o processo de geração de chaves no sistema RSA.

---

# 🔎 Confiabilidade do Teste

O Miller-Rabin é um teste **probabilístico**, pois existe uma pequena possibilidade de classificar incorretamente um número composto como primo.

Para um número composto `n`, a probabilidade de uma única rodada do teste retornar um resultado incorreto é limitada por:

$$
P(\text{erro}) \leq \frac{1}{4}
$$

Ao realizar o teste utilizando diferentes bases (testemunhas), a probabilidade de erro diminui exponencialmente:

$$
P(\text{erro após } k \text{ rodadas}) \leq \left(\frac{1}{4}\right)^k
$$

Assim, aumentando o número de rodadas, a chance de erro torna-se extremamente pequena.

Exemplo:

**5 rodadas:**

$$
\left(\frac{1}{4}\right)^5 = \frac{1}{1024}
$$

**10 rodadas:**

$$
\left(\frac{1}{4}\right)^{10} = \frac{1}{1048576}
$$

---

# 🧮 Fundamentação Matemática

O funcionamento do Miller-Rabin é baseado em propriedades dos números primos e da aritmética modular.

Pelo **Pequeno Teorema de Fermat**, se `n` é primo e `a` é um inteiro coprimo com `n`, então:

$$
a^{n-1} \equiv 1 \pmod n
$$

O Miller-Rabin aprimora essa ideia escrevendo:

$$
n-1 = 2^s \cdot d
$$

onde:

- `s` é um inteiro não negativo;
- `d` é um número ímpar.

A partir disso, para uma base `a`, o número `n` é considerado provavelmente primo se uma das condições for satisfeita:

$$
a^d \equiv 1 \pmod n
$$

ou

$$
a^{2^r d} \equiv -1 \pmod n
$$

para algum:

$$
0 \leq r < s
$$

Caso nenhuma dessas condições seja satisfeita, `a` é considerada uma **testemunha de composição**, indicando que:

$$
n \text{ é composto}
$$

---

# ⚙️ Funcionamento do Algoritmo

O algoritmo segue os seguintes passos:

1. Recebe um número inteiro `n`.
2. Escreve `n - 1` na forma:

$$
n-1 = 2^s \cdot d
$$

3. Escolhe uma base aleatória `a`.
4. Calcula:

$$
x = a^d \mod n
$$

5. Verifica se:

- `x = 1`, ou
- algum valor sucessivo de `x² mod n` é igual a `n-1`.

6. Repete o processo por `k` rodadas para aumentar a confiabilidade.

---

# 🚀 Complexidade

O custo do algoritmo depende da quantidade de rodadas realizadas.

Para cada rodada são realizadas operações de exponenciação modular, que possuem complexidade:

$$
O(\log n)
$$

Portanto, para `k` rodadas:

$$
O(k \log n)
$$

Como normalmente `k` é pequeno, o algoritmo consegue verificar números com centenas de dígitos de forma eficiente.

---

# 📌 Aplicações

O teste de Miller-Rabin possui diversas aplicações, principalmente em:

- 🔑 Geração de chaves criptográficas (RSA);
- 🔐 Sistemas de segurança digital;
- 📡 Protocolos de comunicação segura;
- 🔢 Verificação de grandes números primos.

---

# 👥 Integrantes

- Thalles Gabriel Saraiva
- João Raphanelly
- Hilbert Machado
- Mateus Rocha
- Eva Braga