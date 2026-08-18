class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        combinacao = {")": "(", "]": "[", "}":"{"}
        for i in s:
            if i == "(" or i == "[" or  i == "{":
                pilha.append(i)
            elif i == ")" or i == "]" or i == "}":
                if(len(pilha) == 0):
                    return False
                elif pilha[-1] == combinacao[i]:
                    pilha.pop()
                else:
                    return False
        if len(pilha) == 0:
            return True
        else:
            return False
