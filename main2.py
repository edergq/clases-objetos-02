from producto import Articulo

#a: str = str(input("Ingrese valor: "))    
#b: float = float(input("Ingrese valor: "))    
#lista: list= ["a","b"]
listaArticulos: Articulo = []


def crear_articulo():    
    nombres: str = str(input("Ingrese Nombres: "))    
    codigo: str = str(input("Ingrese Codigo: "))
    precio: float= float(input("Ingrese Precio: "))
    marca: str= str(input("Ingrese Marca: "))
    articulo : Articulo = Articulo( nombres, codigo, precio,marca)
    listaArticulos.append(articulo)


def listar_articulos():
    print(" | ", "PRODUCTO", " | ", "CODIGO", " | ", "PRECIO"," | ", "MARCA"," | ")
    for art in listaArticulos:
        Articulo.imprimir_cadena(art)


def buscar_articulo():
    codigo: str = str(input("Ingrese CODIGO para buscar: "))
    for art in listaArticulos:
        if art.codigo == codigo:
            Articulo.imprimir_cadena(art)

def eliminar_articulo():
    codigo: str = str(input("Ingrese CODIGO para Eliminar: "))
    for index, art in enumerate(listaArticulos):
        if art.codigo == codigo:
            listaArticulos.pop(index)

def editar_ARTICULO():
    codigo: str = str(input("Ingrese CODIGO para Editar: "))
    for art in listaArticulos:
        if art.codigo == codigo:
            art.nombres = str(input("Ingrese un nuevo nombre: "))

def main():
    continuar: bool = True
    while continuar:

        print("*****************************************")
        print("***********SISTEMA DE VENTAS*************")
        print("                                         ")
        print("===================MENÚ==================")
        print("**************INGRESE OPCIONES***********")
        print("       1: PARA AGREGAR producto")
        print("       2: PARA LISTAR producto")        
        print("       3: PARA BUSCAR producto")        
        print("       4: PARA ELIMINAR producto")        
        print("       5: PARA ACTUALIZAR producto")        
        print("       10: PARA SALIR")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                crear_articulo()
            case "2":
                listar_articulos()
            case "3":
                buscar_articulo()
            case "4":
                eliminar_articulo()
            case "5":
                editar_ARTICULO()
            case "10":
                continuar = False


if __name__ == '__main__':
    main()
