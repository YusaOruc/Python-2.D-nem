dosya=open("dd.txt","r")
a=dosya.readlines()
t=a
for i in a:
    t=t+int(i)
print "Dosyadaki say�lar�n toplam�:",t

dosya.close()
