login = str(input("Introduce tu Matricula: "))
list(login)
if len(list(login)) != 8 and len(list(login)) != "abcdefghijklmnopqrstuvwxyz":
    print("Tu matricula es Incorrecta")
elif len(list(login)) == 8:
    print("Tu matricula es:",login)
