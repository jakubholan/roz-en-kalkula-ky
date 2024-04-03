print ("Vítejte v programu kalkulačka, jestliže chcete program ukončit napište ‘konec‘ do operace.")
while True:
    cislo1 = float(input("Zadejte první číslo:"))
    cislo2 = float(input("Zadejte druhé číslo:"))
    operace = input("Zadejte operaci +, -, *, /, **, //")
    if operace == "+":
        print(cislo1 + cislo2)
    elif operace == "-":
        print(cislo1 - cislo2)
    elif operace == "*":
        print(cislo1 * cislo2)
    elif (cislo1 == 0 or cislo2 == 0) and operac == "/":
        print("Nulou nelze dělit")
    elif operace == "/":
        print(cislo1 / cislo2)
    elif operace == "**":
        print(cislo1 ** cislo2)
    elif operace == "//"
        print(cislo1 // cislo2)
    elif operace == "konec":
        print("Děkujeme za využití programu kalkulačka.")
        break
    else:
        print("Proč to tam vlastně píšeš")
