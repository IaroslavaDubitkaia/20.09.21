t = [19,16,13,8,6,9,4,7,5,16,11,13,10,12,15,17,21,18,25,20,22,28,24,21]
print('temperatura medie',)
print('minimul temperaturei', min(t),', iar maximul temperaturei', max(t))
for i in t:
    if i==max(t):
        print('ora/orele la care este temperatura maxima este', t.index(i)+1)
for i in t:
    if i==min(t):
        print('ora/orele la care este temperatura minima este', t.index(i)+1)