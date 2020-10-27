from Gram import *

class leaf:
    def __init__(self, val, nt = False):
        self.val = val
        self.nt = nt
        self.sons = []

    def recorrer(self, pos):
        while pos > 0
            if self.nt == False:
                return pos - 1
            else:
                for i in range(len(self.sons)):
                    pos = self.sons[i].recorrer(pos)

        if pos == 0:
            if self.nt == False:
                return this
            else:
                if len(self.sons) == 0:
                    return this
                else:
                    return self.sons[0].recorrer(0)

class STRee:
    def __init__(self, gram, funAL, start):
        self.gram = gram
        self.funAL = funAL
        #Modificar para otras gramaticas a paartir de aqui
        self.start = start

    def build_tree(self, linea):
        tokens = self.funAL(linea)
        if not tokens:
            print("No se pudo reconocer la linea")
        answer = [leaf("E", nt = True)]
        backup = []
        pos = 0
        for i in tokens:
            toConsider = returnByTipo(i)
            if len(backup) == 0:
                temp1 = answer[0].recorrer(pos)
                if temp1.nt == True:
                    tempDer = self.gram.get_item(temp.val)
                    for i in tempDer:
                        backup.append(cp.copy(answer[0]))
                        temp2 = backup[-1].recorrer(pos)
                        for j in i:
                            temp2.sons.append(leaf(j, j in self.gram.noterminales))
            if len(backup) == 1:
                answer = cp.copy(backup)
                backup = []
                
            pos += 1
