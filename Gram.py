from AL import *

class Produccion:
    def __init__(self, izq, der):
        self.izq = izq
        self.der = der

class Gram:
    def __init__(self):
        noterm_operadores = ["+", "-", "*", "/"]
        self.Producciones = []
        self.terminales = {}
        self.noterminales = {}
        #Terminales
        self.terminales["String"] = "String"
        self.terminales["id"] = "id"
        self.terminales["Numero"] = "Numero"
        self.terminales["="] = "="
        self.terminales["("] = "("
        self.terminales[")"] = ")"
        self.terminales["$"] = "$"
        self.terminales[","] = ","
        self.terminales["."] = "."
        #No Terminales
        self.noterminales["E"] = "E"
        self.noterminales["Ep"] = "Ep"
        self.noterminales["As"] = "As"
        self.noterminales["Idt"] = "Idt"
        self.noterminales["St"] = "St"
        self.noterminales["Fn"] = "Fn"
        self.noterminales["MAs"] = "MAs"
        self.noterminales["MAsp"] = "MAs"
        self.noterminales["SAs"] = "SAs"
        self.noterminales["T"]= "T"

        #Producciones
        #E
        self.Producciones.append(Produccion("E", ["id", "Ep"]))
        #Ep
        self.Producciones.append(Produccion("Ep", ["As"]))
        self.Producciones.append(Produccion("Ep", ["Fn"]))
        #As
        self.Producciones.append(Produccion("As", ["=", "Idt"]))
        #Idt
        self.Producciones.append(Produccion("Idt", ["id", "St"]))
        self.Producciones.append(Produccion("Idt", ["T"]))
        #St
        self.Producciones.append(Produccion("St", ["(", "MAs", ")", "Fn"]))
        self.Producciones.append(Produccion("St", ["Fn"]))
        #Fn
        self.Producciones.append(Produccion("Fn", [".", "id", "(", "MAs", ")", "Fn"]))
        self.Producciones.append(Produccion("Fn", ["$"]))
        #MAs
        self.Producciones.append(Produccion("MAs", ["T", "MAsp"]))
        self.Producciones.append(Produccion("MAs", ["id", "SAs", "MAsp"]))
        #MAsp
        self.Producciones.append(Produccion("MAsp", [",", "MAs"]))
        self.Producciones.append(Produccion("MAsp", ["$"]))
        #SAs
        self.Producciones.append(Produccion("SAs", ["As"]))
        self.Producciones.append(Produccion("SAs", ["$"]))
        #T
        self.Producciones.append(Produccion("T", ["Numero"]))
        self.Producciones.append(Produccion("T", ["String"]))


    def get_item(self, noterminal):
        answer = []
        for i in self.Producciones:
            if i.izq == noterminal:
                answer.append(i.der)
        return answer
