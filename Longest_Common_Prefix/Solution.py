class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        # zip, ele serve para juntar elementos de várias listas ou strings na mesma posição.
        for letras in zip(*strs):
            conjunto = set(letras)
            if len(conjunto) == 1:
                output+= letras[0]
            else:
                break
        return output



        
        
