import streamlit as st
import pandas as pd

#FUNCIÓNES
def saludar(nombre:str) -> str:
    return  st.write(f"Hola {nombre}") 

def sumar (a, b):
    suma= a + b
    return st.write(f"La suma de {a} + {b} es {suma}")

def calcular_area_triangulo(base, altura):
    area= (1/2)*base*altura
    return st.write(f"El área del triangulo es: {area}")

def calcular_precio_final(precio, descuento, impuesto):
    desc= descuento/100
    impues= impuesto/100
    pre_des= precio*desc
    pre_imp= precio*impues
    pref= (precio - pre_des) + pre_imp
    return st.write(f"El precio final es {pref}")

def sumar_lista(n):
    suma=sum(n)
    return st.write(f"La suma es {suma}")

def producto(nombre,cantidad, precio):
    precio_total = precio*cantidad
    return st.write(f"El precio total del artículo {nombre} de costo ${precio} con la cantidad de {cantidad} es: {precio_total}")

def numeros_pares_e_impares (n_list):    
    par=[]
    impar=[]
    for lst in n_list:
        if lst % 2 == 0:
            par.append(lst)
        else:
            impar.append(lst)   
    st.write(f"Los números pares son: {par}")
    st.write(f"Los números impares son: {impar}")      

def multiplicar_todos(*list_ars):
    mult= 1
    for n in list_ars:
        mult *= n
    st.write(f"La multiplicación de los números es: {mult}")   

def informacion_personal(**kwargs):  
    for clave, valor in kwargs.items():
     st.write (f"- {clave}: {valor}")

def calculadora_flexible(operacion,n1, n2):
    if operacion > 4:
        st.write("Error, ese número no se encuentra")
    else:    
     match operacion:
        case  1:
            sum= n1+n2
            return st.write(f"El resultado de la suma es: {sum}")
        case 2:
            rest=n1-n2
            return st.write(f"El resultado de la resta es: {rest}")
        case 3:
            mult=n1*n2
            return st.write(f"El resultado de la multiplicación es: {mult}")
        case 4:
            div= n1/n2
            return st.write(f"El resultado de la divición es: {div}")        

menu= ["Inicio", "Saludo", "Sumar dos numeros","Obtener el área de un triángulo", "Calcular descuento", "Sumar lista de números", "Función para productos", "Par e impar de una lista", "Multiplicación de varios números", "Información personal", "Calculadora flexible"]
selec_op= st.sidebar.selectbox("Opciones",menu)
match selec_op:
    case "Inicio":
        st.subheader("Bienvenidos a la página de ICI.")
    case "Saludo":
        st.title("Saludo simple")
        nombre = st.text_input("Ingrese su nombre:") 
        saludar(nombre) 
        
    case "Sumar dos numeros":
        st.title("Suma de dos Números")
        a= st.number_input("Ingrese el primer número:",min_value=1.0, step=0.5, format="%.2f")
        b= st.number_input("Ingrese el segundo número:",min_value=1.0, step=0.5, format="%.2f")
        sumar(a,b)

    case "Obtener el área de un triángulo":
        st.title("Calcular área de un triángulo.")
        base= st.number_input("Ingrese la medida de la base del triangulo",min_value=1.0, step=0.2, format="%.2f")
        altura= st.number_input("Ingrese la altura del triangulo",min_value=1.0, step=0.2, format="%.2f")
        calcular_area_triangulo(base,altura)
    
    case "Calcular descuento":
        st.title("Calculadora de descuento.")
        precio= st.number_input("Ingrese el precio:",min_value=10.0, step=0.5, format="%.2f")
        descuento= st.number_input("Ingrese el descuento que desea hacer:",min_value=10, step=1, format="%d")
        impuesto=st.number_input("Ingrese la cantidad de impuestos:",min_value=16, step=1, format="%d")   
        calcular_precio_final(precio,descuento,impuesto)

    case "Sumar lista de números":
        st.title("Suma de una lista de números.")
        n= st.text_area("Ingresa los números separados por comas o espacios:")
        if n:
         lista_numeros = [float(num) for num in n.replace(',', ' ').split()]
         sumar_lista(lista_numeros)

    case "Función para productos":
        st.title("Cálculo de productos.")
        nombre= st.text_input("Ingrese el nombre del objeto:") 
        cantidad= st.number_input("Ingrese la cantidad de artículos a llevar:",min_value=1, step=1, format="%d")
        precio= st.number_input("Ingrese el precio:",min_value=10.0, step=0.5, format="%.2f")
        producto(nombre,cantidad,precio)

    case "Par e impar de una lista":
        st.title("Obtener números pares e impares de una lista.")
        num_l= st.text_area("Ingresa los números separados por comas o espacios:")
        if num_l:
         lista_numeros = [float(num) for num in num_l.replace(',', ' ').split()]
         numeros_pares_e_impares(lista_numeros)

    case "Multiplicación de varios números":
        st.title("Multiplicación de varios números.")
        args= st.text_area("Ingresa los números separados por comas o espacios:")
        if args:
         list_num = [float(num) for num in args.replace(',', ' ').split()]
         multiplicar_todos(*list_num)

    case "Información personal":
        st.title("Información personal:")
        nomb= st.text_input("Escriba su nombre:")
        ed= st.text_input("Escriba su edad:")
        e_civ= st.text_input("Escriba su estado civil:")
        direc= st.text_input("Escriba su dirección:")
        nac= st.text_input("Escriba su nacionalidad:")
        prof= st.text_input("Escriba su profesión:")
        tel= st.text_input("Escriba su numero de telefono:")
        informacion_personal(Nombre= nomb, Edad= ed, Estado_Civil= e_civ, Dirección= direc, Nacionalidad= nac, Profesión= prof, Telefono= tel)

    case "Calculadora flexible":
        st.title("Calculadora flexible.")   
        st.write("Opciones:",
                 "[1] Suma",
                 "[2] Resta",
                 "[3] Multiplicacíon",
                 "[4] División")
        operacion= st.number_input("Ingrese el número que se muestra en el menú según la operación que desea resalizar.",min_value=1, step=1, format="%d")  
        n1= st.number_input("Ingrese el primer número",min_value=1.0, step=0.5, format="%.2f")
        n2= st.number_input("Ingrese el segundo número",min_value=1.0, step=0.5, format="%.2f")
        calculadora_flexible(operacion,n1,n2)                                         