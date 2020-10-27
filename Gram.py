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
        self.terminales["$"] = "$"
        self.terminales[","] = ","
        self.terminales["."] = "."
        #No Terminales
        self.noterminales["E"] = "E"
        self.noterminales["As"] = "As"
        self.noterminales["C"] = "C"
        self.noterminales["St"] = "St"
        self.noterminales["Fn"] = "Fn"
        self.noterminales["Fnp"] = "Fnp"
        self.noterminales["MAs"] = "MAs"
        self.noterminales["MAsp"] = "MAs"
        self.noterminales("T") = "T"

        #Producciones
        self.Producciones.append(Produccion("E", ["As"]))
        self.Producciones.append(Produccion("E", ["St"]))
        self.Producciones.append(Produccion("As", ["id", "=", "C"]))
        self.Producciones.append(Produccion("As", ["id", "=", St]))
        self.Producciones.append(Produccion("As", ["id", "=", "T"]))
        self.Producciones.append(Produccion("C", ["id", "(", "MAs", ")", "Fn"]))
        self.Producciones.append(Produccion("St", ["id", "Fn"]))
        self.Producciones.append(Produccion("Fn", [".", "id", "(", "MAs", ")", "Fnp"]))
        self.Producciones.append(Produccion("Fnp", ["Fn"]))
        self.Producciones.append(Produccion("Fnp", ["$"]))
        self.Producciones.append(Produccion("MAs", ["T", "MAsp"]))
        self.Producciones.append(Produccion("MAs", ["As", "MAsp"]))
        self.Producciones.append(Produccion("MAsp", [",", "MAs"]))
        self.Producciones.append(Produccion("MAsp", ["$"]))
        self.Producciones.append(Produccion("T", ["id"]))
        self.Producciones.append(Produccion("T", ["Numero"]))
        self.Producciones.append(Produccion("T", ["String"]))

    def get_item(self, noterminal):
        answer = []
        for i in self.Producciones:
            if i.izq == noterminal:
                answer.append(i.der)
        return answer
