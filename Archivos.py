import random as rnd
import csv
#crear archivo
def creararchivo():
    listacreaturas= ["ave","perro","gato","gallina","caballo","delfin","pez","vaca","buey","siervo","gallo","mono","pato","ganzo","ardilla","panda","camello","loro","buffalo","colibri","cabra","oveja","castor","iguana","koala","conejo","tortuga","armadillo","llama","halcon","zombie","bruja","gigante","dinosaurio","quimera","troll","ogro","oso","gorila","mago","avestruz","leon","rinoceronte","cobra","tigre de bengala","babuino","jaguar","piraña","tiburon","aguila","lagarto","escorpion gigante","robot","cangrejo","toro","lobo","ciclope","hiena","murcielago"]
    listatipos = ["Amigo","Enemigo","Neutro"]
    with open("archivocreaturas.csv","w") as archivo:
        
        archivo.write('')
    with open("archivocreaturas.csv","a", newline="") as archivo:
        escritor = csv.writer(archivo,delimiter=",")
        for linea in range(0,100):
            filarandom =  []
            for elemento in range(0,6):
                if elemento == 1:
                    filarandom.append(rnd.choice(listatipos))
                else:
                    filarandom.append(rnd.choice(listacreaturas))
                
            escritor.writerow(filarandom)

