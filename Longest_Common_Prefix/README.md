# 14. Longest Common Prefix

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/longest-common-prefix/

## Descrição

Dado um array de strings, escreva uma função que encontre o **maior prefixo comum** entre todas as strings.

Caso não exista nenhum prefixo comum, a função deve retornar uma string vazia `""`.

## Exemplos

### Exemplo 1

**Entrada:**

```text
strs = ["flower", "flow", "flight"]
```

**Saída:**

```text
"fl"
```

### Exemplo 2

**Entrada:**

```text
strs = ["dog", "racecar", "car"]
```

**Saída:**

```text
""
```

**Explicação:** Não existe nenhum prefixo comum entre as strings.

## Restrições

* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`
* `strs[i]` contém apenas letras minúsculas do alfabeto inglês quando não está vazia.

## Objetivo

Implementar uma função que receba um array de strings e retorne o maior prefixo que aparece no início de **todas** as strings.

