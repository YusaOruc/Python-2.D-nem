liste=["elma","armut","karpuz","kavun","erik","�z�m"]
while True:
    try:
        s=raw_input("L�tfen meyve ad�n� giriniz:")
        p=liste.index(s)+1
        print s,"Listenizde",p,"no lu s�rada bulunuyor"
    except ValueError:
        pass
