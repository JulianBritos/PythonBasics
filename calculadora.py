def calculadora(num1: float, num2: float, symbol: str): 

    if symbol == '+':
            
        print(num1 + num2)
        
    elif symbol == '*':
            
        print(num1 * num2)

    elif symbol == '/':
            
        print(num1 / num2)
        
    elif symbol == '-':

        print(num1 - num2)
        
    else:
            
        print("Operación Inválida")
