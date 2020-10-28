from TAS import *

def main():
    gram = Gram()
    my_TAS = TAS(gram, analizadorLexico)
    while True:
        print("Ingrese su linea de codigo")
        line = input()
        my_TAS.check_if_correct(line)
    # s = input()
    # print(reconocerAgrupacion(s, 0))


if __name__ == "__main__":
    main()
