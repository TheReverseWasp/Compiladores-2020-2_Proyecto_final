import re
import copy as cp
from extrafuns import *

n = r"^[0-9]*$(\.[0-9]*)?"
v = r"^[a-z|A-Z]([a-z|A-Z|0-9]*)$"
o = r"^\=$"
s = r'^"(?:[^\\]|(?:\\.))*"'
sep1 = r"^\,$"
sep2 = r"^\.$"
agrupacion = r"^[\(|\)]$"

byTipo = {"String": True, "id": True, "Numero": True}

class Token:
    def __init__(self, p, t, i = -1, f = -1):
        self.palabra = p
        self.inicio = i
        self.fin = f
        self.tipo = t

def returnByTipo(token):
    if token.tipo in byTipo:
        return token.tipo
    return token.palabra

def reconocerToken(r, linea, idx, tipo):
    f = cp.copy(idx)
    flag = False
    while r.match(linea[idx:f + 1]) and f < len(linea):
        f += 1
        flag = True
    if flag:
        print(idx, f)
        t = Token(linea[idx:f], tipo, i = idx, f = f)
        return t
    return False

def reconocerTokenString(r, linea, idx, tipo):
    f = cp.copy(idx)
    flag = False
    while not r.match(linea[idx:f + 1]) and f < len(linea):
        f += 1
    f += 1
    if r.match(linea[idx:f]):
        flag = True
    if flag:
        t = Token(linea[idx:f], tipo, i = idx, f = f)
        return t
    return False


def reconocerNumero(linea, idx):
    r = re.compile(n)
    return reconocerToken(r, linea, idx, "Numero")

def reconocerId(linea, idx):
    r = re.compile(v)
    return reconocerToken(r, linea, idx, "id")

def reconocerString(linea, idx):
    r = re.compile(s)
    return reconocerTokenString(r, linea, idx, "String")

def reconocerAsignacion(linea, idx):
    r = re.compile(o)
    return reconocerToken(r, linea, idx, "Asignacion")

def reconocerSeparador1(linea, idx):
    r = re.compile(sep1)
    return reconocerToken(r, linea, idx, "Separador1")

def reconocerSeparador2(linea, idx):
    r = re.compile(sep1)
    return reconocerToken(r, linea, idx, "Separador2")

def reconocerAgrupacion(linea, idx):
    r = re.compile(agrupacion)
    return reconocerToken(r, linea, idx, "Agrupacion")

def getToken(linea, idx):
    funs = [reconocerNumero, reconocerId, reconocerString,
    reconocerAsignacion, reconocerSeparador1, reconocerSeparador2, reconocerAgrupacion]
    for i in funs:
        t = i(linea, idx)
        if t != False:
            return t
    return False

def analizadorLexico(linea):
    idx = 0
    tokens = []
    while idx < len(linea):
        while linea[idx] == " " or linea[idx] == "\t":
            idx += 1
        t = getToken(linea, idx)
        try:
            idx = t.fin
        except:
            print("Error en la posición", idx, "Token invalido")
            return False
        tokens.append(cp.copy(t))
    return tokens
