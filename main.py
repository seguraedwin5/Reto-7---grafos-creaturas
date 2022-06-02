import Archivos as ar
import grafos as gf
        

ar.creararchivo()
grafocreado =gf.CrearGrafo()
creat1 = str(input("digite el nombre de la creatura 1 para obtener información:\n"))
creat2 = str(input("digite el nombre de la creatura 2 para obtener información:\n"))
print("\n estas son todas las relaciones que tiene la creatura 1: "+creat1+"\n")
gf.verNodosConectados(grafocreado,creat1)
print("\n estas son todas las relaciones que tiene la creatura 1: "+creat2+"\n")
gf.verNodosConectados(grafocreado,creat2)
print(f"\n esta es la ruta mas corta que conecta a las creaturas: {creat1} y {creat2}")
gf.rutamascorta(grafocreado,creat1,creat2)
print("\n Estas son las creaturas mas importantes(centrales) en el mundo\n")
gf.listarNodosimportantes(grafocreado)
gf.mostrarGrafo(grafocreado)
