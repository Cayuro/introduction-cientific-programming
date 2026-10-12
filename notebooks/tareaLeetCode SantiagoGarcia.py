"""
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie 
that the child will be content with; and each cookie j has a size s[j]. 
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.

Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
"""
"""
La solución fue la siguiente:

Explicación del código:

1. i = 0 y j = 0: 
   Son nuestros "punteros" o índices que nos ayudan a recorrer la lista de los niños (g) y la de las galletas (s) desde el principio.

2. g.sort() y s.sort(): 
   Ordenan ambas listas de menor a mayor. Esto es clave para la estrategia ávida (greedy), ya que nos permite comparar siempre al niño menos exigente con la galleta más pequeña disponible.

3. while i < len(g) and j < len(s): 
   El ciclo se ejecuta únicamente mientras todavía queden niños por atender Y galletas por probar en la bandeja.

4. if s[j] >= g[i]: 
   Preguntamos si el tamaño de la galleta actual es mayor o igual a la exigencia del niño. Si es así, el niño queda contento y avanzamos al siguiente niño sumando i += 1.

5. j += 1: 
   Independientemente de si la galleta le sirvió al niño o si era muy pequeña y se descartó, esa galleta ya se usó, por lo que siempre avanzamos a la siguiente galleta.

6. return i: 
   Como la variable 'i' aumenta de uno en uno cada vez que un niño recibe su galleta, al final del ciclo su valor representa exactamente el número total de niños contentos.
"""
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        i = 0
        j = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1 
            j += 1
        return i
