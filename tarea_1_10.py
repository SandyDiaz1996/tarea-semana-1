class Ejercicios:
    def __init__(self):
        pass

    def superficie_de_circulo1(self):
        s, r = 0, 0
        r = float(input('Radio del círculo: '))
        s = 3.1416 * r ** 2
        s = round(s, 2)
        print('\nLa superficie del círculo es:', s)
        print('-'*30 + '-' * len(str(s)))
    
    def descuento_compra2(self):
        cp, tc, d = 0, 0, 0
        tc = float(input('Ingrese su compra: '))
        d = tc * 0.15
        cp = tc - d
        print('\nEl total a pagar es:', cp)
        print('-'*21 + '-' * len(str(cp)))
    
    def comision_compra3(self):
        tr, sb, v1, v2, v3, c = 0, 0, 0, 0, 0, 0
        sb = float(input('Ingrese el sueldo: '))
        v1 = float(input('Ingrese la venta #1: '))
        v2 = float(input('Ingrese la venta #2: '))
        v3 = float(input('Ingrese la venta #3: '))
        tv = v1 + v2 + v3
        c = tv * 0.1
        tr = sb + c
        tr = round(tr, 2)
        print('\nEl total a recibir es:', tr)
        print('-'*23 + '-' * len(str(tr)))

    def aprueba_calificacion4(self):
        cal = float(input('Ingrese la calificación: '))
        if cal >= 7:
            print('Aprobado')
        print('-'*23 + '-' * len(str(cal)))

    def ap_des_calificacion5(self):
        cal = float(input('Ingrese la calificación: '))
        if cal >= 7:
            print('Aprobado')
        else:
            print('Reprobado')
        print('-'*23 + '-' * len(str(cal)))

    def sueldo6(self):
        si, ns = 0, 0
        si = float(input('Ingrese su sueldo: '))
        if si <= 600:
            ns = si + si * 0.1
        else:
            ns = si
        ns = round(ns, 2)
        print('Sueldo $' + str(ns))
        print('-'*19 + '-' * len(str(ns)))

    def pago_trabajo7(self):
        ht, ph, he, het, phe = 0, 0, 0, 0, 0
        ht = int(input('Ingrese horas trabajadas: '))
        ph = int(input('Pago por hora: '))
        if ht > 40:
            he = ht - 40
            if he > 8:
                het = he - 8
                phe = ph * 2 * 8 + ph *3 * het
            else:
                phe = ph * 2 * he
            pt = ph * 40 + phe
        else:
            pt = ph * ht
        print('El pago total de horas trabajadas es: ' + str(pt))
        print('-'*38 + '-' * len(str(pt)))
    
    def num_mayor8(self):
        n1, n2, n3, nm = 0, 0, 0, 0
        n1 = int(input('Ingrese un número: '))
        n2 = int(input('Ingrese un número: '))
        n3 = int(input('Ingrese un número: '))
        if (n1 > n2) and (n1 > n3):
            nm = n1
        elif (n2 > n3):
            nm = n2
        else:
            nm = n3
        print('El número mayor es:', nm)
        print('-'*14 + '-' * len(str(nm)))

    def mecanismo_switch9(self):
        num, v, resp = 0, 0, 0
        num = int(input('Ingrese un número: '))
        v = float(input('Ingrese otro número: '))
        if (num == 1):
            resp = 100 * v
        elif (num == 2):
            resp = 100 ** v
        elif (num == 3):
            resp = 100 / v
        else:
            resp = 0
        resp = round(resp, 2)
        print('Resultado:', resp)
        print('-'*11 + '-' * len(str(resp)))

    def uso_and10(self):
        c1 = float(input('Ingrese primer nota: '))
        c2 = float(input('Ingrese segunda nota: '))
        if (c1 >= 80) and (c2 >= 80):
            print('Aceptado')
        else:
            print('Rechazado')
        print('-'*20 + '-' * len(str(c2)))

    def uso_or10(self):
        c1 = float(input('Ingrese primer nota: '))
        c2 = float(input('Ingrese segunda nota: '))
        if (c1 >= 90) or (c2 >= 90):
            print('Aceptado')
        else:
            print('Rechazado')
        print('-'*20 + '-' * len(str(c2)))

tarea = Ejercicios()
# tarea.superficie_de_circulo1()
# tarea.descuento_compra2()
# tarea.comision_compra3()
# tarea.aprueba_calificacion4()
# tarea.ap_des_calificacion5()
# tarea.sueldo6()
# tarea.pago_trabajo7()
# tarea.num_mayor8()
# tarea.mecanismo_switch9()
# tarea.uso_and10()
# tarea.uso_or10()
