def mult(a,b):
    if a % b == 0:
        return True
    else:
        return False
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print (mult(a,b))