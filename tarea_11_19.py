class Ejercicios:
    def __init__(self):
        pass

    def num_cuadrado11(self):
        suma = 0
        for i in range(1, 101):
            suma = suma + i * i
        print('Suma:', suma)
        print('-'*6 + '-'*len(str(suma)))

    def numero12(self):
        i = 1
        while i <= 100:
            print(i)
            i = i + 1
        print('---')

    def producto_num13(self):
        suma, prod, num, resp = 0, 1, 0, ''
        resp = input('Ingresa una letra: ')
        while (resp != 'N') and (resp != 'n'):
            num = int(input('Ingrese un número: '))
            suma = suma + num
            prod = prod * num
            print('Desea continuar (S/N)?')
            resp = input('Ingrese una letra: ')
        print('\nEl total de la suma es:', suma)
        print('El total del producto es:', prod)
        print('-'*26 + '-'*len(str(prod)))

    def producto_suma14(self):
        suma, prod, num = 0, 1, 0
        num = int(input('Ingrese un número: '))
        while (num != -1):
            suma = suma + num
            prod = prod * num
            num = int(input('Ingrese un número: '))
        print('\nEl total de la suma es:', suma)
        print('El total del producto es:', prod)
        print('-'*26 + '-'*len(str(prod)))
    
    def numero_primo15(self):
        primo, divisor, num, res, divisor = 'T', 0, 0, 0, 2
        num = int(input('Ingrese un número: '))
        while ((divisor < num) and (primo == 'T')):
            res = num % divisor
            if (res == 0):
                primo = 'F'
            divisor = divisor + 1
        if primo == 'T':
            print('Número', num, 'es primo.')
        else:
            print('Número', num, 'no es primo.')
        print('-'*20 + '-'*len(str(num)))

    def estructura_repeat16(self):
        i, n, serie, band = 1, 0, 0, 'T'
        n = int(input('Ingrese un número: '))
        while (i < n):
            if band == 'T':
                serie = serie + (1/i)
                band = 'F'
            else:
                serie = serie - (1/i)
                band = 'T'
            i = i + 1
        print('Serie:', serie)
        print('-'*7 + '-'*len(str(serie)))

    def factorial17(self):
        n = int(input('Numero de repeticiones: '))
        for _ in range(1, n+1):
            numero = int(input('Ingrese un número: '))
            fact = 1
            for j in range(1, numero+1):
                fact = fact * j
            print('El factorial del número', numero, 'es', fact)
        print('-'*30)

    def arrays18(self):
        num, a, b = [], [], []
        for i in range(1, 21):
            num.append(int(input('Ingrese el número {}: '.format(i))))
            if (num[i-1] > 0):
                a.append(num[i-1])
            else:
                b.append(num[i-1])
        print('Array: A')
        for i in a:
            print(i)
        print('Array: B')
        for i in b:
            print(i)
        print('-'*15)

    def calificaciones_30_alumnos19(self):
        notas_list, alumnos_list, promedio_exam = [], [], []
        for alum in range(1, 31):
            alumno = input('Nombre del alumno {}: '.format(alum))
            alumnos_list.append(alumno)
            for nota in range(1, 7):
                print('Escriba la calificación para el alumno {} en el exámen {}.'.format(alumno, nota))
                notas_temp = float(input('Nota #{}: '.format(nota)))
                if nota == 1:
                    notas_list.append([notas_temp])
                else:
                    notas_list[alum-1].append(notas_temp)
            print('')
        for num_examen in range(6):
            sum_notas = 0
            for nota in notas_list:
                sum_notas += nota[num_examen]
            promedio = (sum_notas/30)
            print('Promedio de exámen {}= {}'.format(num_examen+1, promedio))
        print('')
        for numero, alum in enumerate(alumnos_list):
            sum_notas = sum(notas_list[numero])
            promedio = (sum_notas/6)
            print('Promedio del alumno {}= {}'.format(alum, promedio))
        promedio_mayor = 0
        for num_examen in range(6):
            sum_notas = 0
            for nota in notas_list:
                sum_notas += nota[num_examen]
            promedio = (sum_notas/30)
            if promedio_mayor < promedio:
                promedio_mayor = promedio
            promedio_exam.append(promedio)
        print('\nEl exámen', promedio_exam.index(promedio_mayor)+1, 'obtuvo el mayor promedio:', promedio_mayor)
        print('-'*50)


tarea = Ejercicios()
# tarea.num_cuadrado11()
# tarea.numero12()
# tarea.producto_num13()
# tarea.producto_suma14()
# tarea.numero_primo15()
# tarea.estructura_repeat16()
# tarea.factorial17()
# tarea.arrays18()
tarea.calificaciones_30_alumnos19()
