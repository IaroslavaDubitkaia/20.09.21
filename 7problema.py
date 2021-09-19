v = [9755,5593,1301,3348,4035,6938,1630]
print('venitul saptamanal al intreprinderii', sum(v))
print('media venitul zilnic', sum(v)/7)
if v.index(max(v))==0:
    print('ziua cu cel mai mare venit este luni')
elif v.index(max(v))==1:
    print('ziua cu cel mai mare venit este marti')
elif v.index(max(v))==2:
    print('ziua cu cel mai mare venit este miercuri')
elif v.index(max(v))==3:
    print('ziua cu cel mai mare venit este joi')
elif v.index(max(v))==4:
    print('ziua cu cel mai mare venit este vineri')
elif v.index(max(v))==5:
    print('ziua cu cel mai mare venit este sambata')
elif v.index(max(v))==6:
    print('ziua cu cel mai mare venit este duminica')
if v.index(min(v))==0:
    print('ziua cu cel mai mic venit este luni')
elif v.index(min(v))==1:
    print('ziua cu cel mai mic venit este marti')
elif v.index(min(v))==2:
    print('ziua cu cel mai mic venit este miercuri')
elif v.index(min(v))==3:
    print('ziua cu cel mai mic venit este joi')
elif v.index(min(v))==4:
    print('ziua cu cel mai mic venit este vineri')
elif v.index(min(v))==5:
    print('ziua cu cel mai mic venit este sambata')
elif v.index(min(v))==6:
    print('ziua cu cel mai mic venit este duminica')