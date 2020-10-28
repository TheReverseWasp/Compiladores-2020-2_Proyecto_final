from Gram import *

class TAS:
    def __init__(self, gram, funAL):
        self.gram = gram
        self.funAL = funAL
        #Modificar para otras gramaticas a paartir de aqui
        self.start = "E"
        self.TAS = {}
        #E
        self.TAS["E"] = {}
        self.TAS["E"]["id"] = Produccion("E", ["id", "Ep"])
        #Ep
        self.TAS["Ep"] = {}
        self.TAS["Ep"]["="] = Produccion("Ep", ["As"])
        self.TAS["Ep"]["."] = Produccion("Ep", ["Fn"])
        self.TAS["Ep"]["$"] = Produccion("Ep", ["Fn"])
        #As
        self.TAS["As"] = {}
        self.TAS["As"]["="] = Produccion("As", ["=", "Idt"])
        #Idt
        self.TAS["Idt"] = {}
        self.TAS["Idt"]["id"] = Produccion("Idt", ["id", "St"])
        self.TAS["Idt"]["Numero"] = Produccion("Idt", ["T"])
        self.TAS["Idt"]["String"] = Produccion("Idt", ["T"])
        #St
        self.TAS["St"] = {}
        self.TAS["St"]["("] = Produccion("St", ["(", "MAs", ")", "Fn"])
        self.TAS["St"]["."] = Produccion("St", ["Fn"])
        self.TAS["St"]["$"] = Produccion("St", ["Fn"])
        #Fn
        self.TAS["Fn"] = {}
        self.TAS["Fn"]["."] = Produccion("Fn", [".", "id", "(", "MAs", ")", "Fn"])
        self.TAS["Fn"]["$"] = Produccion("Fn", ["$"])
        #MAs
        self.TAS["MAs"] = {}
        self.TAS["MAs"]["Numero"] = Produccion("MAs", ["T", "MAsp"])
        self.TAS["MAs"]["String"] = Produccion("MAs", ["T", "MAsp"])
        self.TAS["MAs"]["id"] = Produccion("MAs", ["id", "SAs", "MAsp"])
        #MAsp
        self.TAS["MAsp"] = {}
        self.TAS["MAsp"][","] = Produccion("MAsp", [",", "MAs"])
        self.TAS["MAsp"]["$"] = Produccion("MAsp", ["$"])
        #SAs
        self.TAS["SAs"] = {}
        self.TAS["SAs"]["="] = Produccion("SAs", ["As"])
        self.TAS["SAs"]["$"] = Produccion("SAs", ["$"])
        #T
        self.TAS["T"] = {}
        self.TAS["T"]["Numero"] = Produccion("T", ["Numero"])
        self.TAS["T"]["String"] = Produccion("T", ["String"])


    def check_if_correct(self, texto):
        tokens = self.funAL(texto)
        for i in tokens:
            if i.tipo in byTipo:
                print(i.tipo, end=" ")
            else:
                print(i.palabra, end=" ")
        print()
        if tokens != False:
            #then check
            it = 0
            nsit = 0
            ns = self.start
            q = []
            while nsit < len(tokens):
                print(it, "E -> ",  end="")
                if tokens[nsit].tipo in byTipo:
                    val = tokens[nsit].tipo
                else:
                    val = tokens[nsit].palabra
                if len(q) == 0:
                    if val in self.TAS[ns]:
                        #replace
                        q.append(self.TAS[ns][val].der)
                        q = flatten(q)
                    else:
                        if "$" in self.TAS[ns]:
                            q.append(self.TAS[ns]["$"].der)
                            q = flatten(q)
                        else:
                            print("Error en la gramatica")
                            return False
                elif q[nsit] in self.gram.noterminales:
                    if val in self.TAS[ns]:
                        #replace
                        q[nsit] = self.TAS[ns][val].der
                        q = flatten(q)
                    else:
                        if "$" in self.TAS[ns]:
                            q[nsit] = self.TAS[ns]["$"].der
                            q = flatten(q)
                        else:
                            print("Error en la gramatica")
                            return False
                if q[nsit] in self.gram.terminales:
                    #Go Ahead
                    if q[nsit] == "$":
                        q[nsit] = []
                        q = flatten(q)
                        nsit -= 1
                    nsit += 1
                if nsit < len(q):
                    ns = q[nsit]
                print(str(q))
                it += 1
            val = "$"
            while len(q) != len(tokens):
                ns = q[nsit]
                print(it, "E -> ", end="")
                if val in self.TAS[ns]:
                    if self.TAS[ns][val].der[0] != "$":
                        q[nsit] = self.TAS[ns][val].der
                    else:
                        q[nsit] = []
                    q = flatten(q)
                else:
                    print("Error en la gramatica")
                    return False
                print(str(q))
                it += 1
        else:
            print("Error al identificar tokens")
            return False
        print("Gramatica Correcta")
        return True
