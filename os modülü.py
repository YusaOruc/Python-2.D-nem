#os mod�l�n� incele internetten 
import os   


print os.getcwd()
print os.chdir("/") #k�k dizimine g�t�r�r
print os.getcwd()

for i in os.listdir(os.getcwd()):
    if os.path.isfile(i):
        print "Dosya=>",i
    else:
        print "Klosor=>",i


