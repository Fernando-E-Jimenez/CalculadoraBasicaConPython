def calculadora():
    while True:
        try:
            #obtener los valores de entrada del usuario
            num1=float(input("Ingrese un número: "))
            num2=float(input("Ingrese otro número: "))
            op=input("Ingres un operador (+, -, *, /): ")

            #realizar la operacion segun la entrada del usuario
            if op == "+":
                result=num1+num2
            elif op== "-":
                result = num1-num2
            elif op == "*":
                result = num1*num2
            elif op == "/":
                #comprobar si el divisor es cero
                if num2 == 0:
                    print("Error: no se puede dividir por cero.")
                    continue
                result = num1 / num2
            else:
                #si la entrada del usuario no es una operacion valida, imprimir un mensaje de error
                print("Error: operacion no reconocida.")
                continue

            #imprimir el resultado
            print(f"Resultado: {result}")

            #preguntar al usuario si desea realizar otra operacion
            repeat = input("Desea realizar otra operacion? (s/n)")
            if repeat.lower() != "s":
                break
        except ValueError:
            #si el usuario no ingresa un numero valido, imprimir un mensaje de error

            print("Error: por favor ingrese un numero valido.")

#ejecutar la funcion calculadora
calculadora()
