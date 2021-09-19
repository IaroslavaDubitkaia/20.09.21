x = [18,5,28,2,30]
y = [5,16,27,12,3]
print('suma primelor 3 componente ale variabilei x', sum(x[0:3]))
print('suma tuturor componentelor varibelei y', sum(y))
z=1
for i in range(0,len(x)):
    z=z*x[i]
    i+=1
print('produsul tuturor componentelor variabilei x', z)
print('valoarea absoluta a componentei a 3 a variabilei y', abs(y[2]))
print('suma primelor componente ale variabilelor x si y', x[0]+y[0])