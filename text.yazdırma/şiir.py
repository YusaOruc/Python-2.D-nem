dosya=open("�iir.txt","w")
dosya.write("B�t�n g�ne�ler batmadan,\nBi t�rk� daha s�yleyeyim bu yerde")
dosya.close
with open("�iir.txt","r")as dosya:
    a=dosya.read()
    print a

    #dosyay� basa sarma    
    dosya.seek(0)
    b=dosya.read()
    print b

    #dosyan�n bas�na veri ekleme
with open("�iir.txt","r+")as f:
    veri=f.read()
    f.seek(0)
    f.write("Selim �zden\t:0212 222 22\n"+veri)

    #�stedi�in sat�ra ekleme    
with open("�iir.txt","r+")as f:
    veri=f.read()
    f.insert("2","Sedat K�z\t:25051522525")
    f.writelines(veri)
