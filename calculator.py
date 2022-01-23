from colorama import Fore
import time
Magenta = Fore.MAGENTA
print(Fore.GREEN + "'  .██████╗.█████╗.██╗......██████╗██╗...██╗██╗......█████╗.████████╗.██████╗.██████╗.")
print(Fore.RED + "'  ██╔════╝██╔══██╗██║.....██╔════╝██║...██║██║.....██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
print(Fore.BLUE + "'  ██║.....███████║██║.....██║.....██║...██║██║.....███████║...██║...██║...██║██████╔╝")
print(Fore.YELLOW + "'  ██║.....██╔══██║██║.....██║.....██║...██║██║.....██╔══██║...██║...██║...██║██╔══██╗")
print(Fore.MAGENTA + "'  ╚██████╗██║..██║███████╗╚██████╗╚██████╔╝███████╗██║..██║...██║...╚██████╔╝██║..██║")
print(Fore.GREEN + "'  .╚═════╝╚═╝..╚═╝╚══════╝.╚═════╝.╚═════╝.╚══════╝╚═╝..╚═╝...╚═╝....╚═════╝.╚═╝..╚═╝")
print(Fore.RED + "'  ...................................................................................")
print(Fore.LIGHTYELLOW_EX + "                                     By Crepsoo#1034"                                )

print(Fore.LIGHTGREEN_EX + "[1] Sumar")
print("[2] Restar")
print("[3] Multiplicar")
print("[4] Dividir")
print("[5] Par o Impar")
print("[6] Salir")
print(" ")
x = int(input(f"{Magenta}[+] Escoge el tipo de operación que quieres hacer [1-6]: "))

if x == 1:
    a = int(input("[+] Escribe el primer número: "))
    b = int(input("[+] Escribe el segundo número: "))
    y = (a + b)
    print("[+] El resultado de la operación es: ",y)
elif x == 2:
    a = int(input("[+] Escribe el primer número: "))
    b = int(input("[+] Escribe el segundo número: "))
    y = (a - b) 
    print("[+] El resultado de la operación es: ",y)
elif x == 3:
    a = int(input("[+] Introduce el primer número: "))
    b = int(input("[+] Introduce el segundo número: "))
    c = a * b
    print("[+] El resultado de la operación es: ",c)
elif x == 4:
    a = int(input("[+] Introduce el primer número: "))
    b = int(input("[+] Introduce el segundo número: "))
    c = a / b
    print("[+] El resultado de la operación es: ",c)
elif x == 5:
    a = int(input("[+] Introuce el número: "))
    b = a%2
    if b == 0:
        print("[+] El número introducido es par")
    else:
        print("[+] El número introducido es impar")
elif x == 6:
    print("[+] Exiting...")
    time.sleep(2)
else:
    print("[+] Número introducido no válido")
    print("[+] Saliendo...")



