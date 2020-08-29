import math
import sys


#La funcion main tiene como argumentos.

#g = valor de gravedad
#l = longitud del péndulo
#t0 = tiempo inicial
#tf = tiempo final
#n = numero de particiones del método
#x0 = condicion inicial
#x00 = condicion inicial


def calcular(g,l,to,tf,n,x0,v0):
    h = (tf - to)/n
    w2 = g/l
    time, theta = RungeKutta_o4_pendulo(h,n,w2,x0,v0,to)
    #guardando listas
    guardar_lista(time,theta)

def guardar_lista(tiempo, distancia):
    path = "solucion.dat"
    f = open(path,'a+')
    for i,j in zip(tiempo,distancia):
        f.write("%f " % i)
        f.write("%f\n" % j)
    f.close()

def RungeKutta_o4_pendulo(h,n,w2,x0,v0,to):
    time = []
    theta = []
    print("Solución... \n")
    print("tiempo \t theta")
    for k in range(1,n):
        t = to + (k-1)*h
        k1 = h*v0
        l1 = h*f(w2,x0)
        k2 = h*(v0 + 0.5*l1)
        l2 = h*f(w2,x0 + 0.5*k1)
        k3 = h*(v0 + 0.5*l2)
        l3 = h*f(w2,x0 + 0.5*k2)
        k4 = h*(v0 + l3)
        l4 = h*f(w2,x0 + k3)
        v1 = v0 + (l1 + 2*l2 + 2*l3 + l4)/6
        x1 = x0 + (k1 + 2*k2 + 2*k3 + k4)/6
        print("%f \t %f" % (t,x1))
        time.append(t + h)
        theta.append(x1)
        v0 = v1
        x0 = x1
    return time,theta
   
#Funciones utiles para RungeKutta
def f(w2,x):
    return -w2*math.sin(x)  

    

if __name__ == "__main__":
    g = float(sys.argv[1])
    l = float(sys.argv[2])
    to = float(sys.argv[3])
    tf = float(sys.argv[4])
    n = int(sys.argv[5])
    x0 = float(sys.argv[6])
    v0 = float(sys.argv[7])
    calcular(g,l,to,tf,n,x0,v0)