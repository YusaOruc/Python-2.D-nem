liste=[1,5,1,1,1,3,7,8,9,41,25,65]
print liste.index(41)  #Ka��nc� s�rada oldu�unu yazd�r�r.

liste.insert(3, 74) # yeni eleman� belirtilen indise ekler
print liste

liste.sort()              # listeyi s�ralar
liste.reverse()           # listeyi ters �evirir
liste.pop()               # son eleman� siler
liste.append(5)           # sonuna yeni eleman ekler

liste.count(1)            # Bu eleman listede ka� tane var
del liste[2]                 # 2.indisteki eleman� listeden sil


print liste
