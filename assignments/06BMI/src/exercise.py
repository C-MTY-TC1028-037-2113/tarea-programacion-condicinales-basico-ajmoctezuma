def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))

    if peso<=0 or altura<=0:
        print('Revisa tus datos, alguno de ellos es erróneo.')
    else:
        bmi= (peso/(altura**2))
        if bmi<20:
            print('PESO BAJO')
        elif bmi <= 25:
            print ('NORMAL')
        elif bmi < 30:
            print ('SOBREPESO')
        elif 30<= bmi and bmi < 40:
            print ('OBESIDAD')
        else:
            print ('OBESIDAD MORBIDA')
        
if __name__=='__main__':
    main()
