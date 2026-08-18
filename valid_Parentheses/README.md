# Valid Parentheses

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/valid-parentheses/

## Descrição

Dada uma string `s` contendo apenas os caracteres `(`, `)`, `{`, `}`, `[` e `]`, determine se a string possui uma sequência de parênteses **válida**.

Uma string é considerada válida quando:

1. Cada parêntese aberto é fechado pelo parêntese do **mesmo tipo**.
2. Os parênteses são fechados na **ordem correta**.
3. Todo parêntese de fechamento possui um parêntese de abertura correspondente.

## Exemplos

### Exemplo 1

**Entrada:**

```text
s = "()"
```

**Saída:**

```text
true
```

### Exemplo 2

**Entrada:**

```text
s = "()[]{}"
```

**Saída:**

```text
true
```

### Exemplo 3

**Entrada:**

```text
s = "(]"
```

**Saída:**

```text
false
```

### Exemplo 4

**Entrada:**

```text
s = "([])"
```

**Saída:**

```text
true
```

### Exemplo 5

**Entrada:**

```text
s = "([)]"
```

**Saída:**

```text
false
```

## Restrições

* `1 <= s.length <= 10⁴`
* `s` contém apenas os caracteres `(`, `)`, `[`, `]`, `{` e `}`.

## Objetivo

Implementar uma função que determine se todos os parênteses presentes na string estão **corretamente abertos, fechados e aninhados**, retornando `true` caso a sequência seja válida e `false` caso contrário.

