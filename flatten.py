eski_liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
yeni_liste = list()

def flatten(a):
    for i in a:
        if type(i) == list:
            flatten(i)
        else:
            yeni_liste.append(i)

print(eski_liste)
flatten(eski_liste)
print(yeni_liste)
