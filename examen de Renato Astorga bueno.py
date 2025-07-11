#prueba
opc = 1

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'], 
            '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'], 
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'], 
            'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'], 
            'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'], 
            '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'], 
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'], 
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],  
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7], 
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

while True:
        
        print("---Menu principal---")
        print("1)stock marca")
        print("2)busqueda por precio")
        print("3)eliminar producto")
        print("4)salir")

        opc = int(input("ingrese su opcion "))

        if opc == 1:
            try:
                marca = input("ingrese su marca a buscar ")
                if marca.lower() == "hp":
                    total = (stock['8475HD'][1]) + (stock['fgdxFHD'][1]) 
                    print(f"el total de es {total}")
                elif marca.lower() == "acer" :
                    total = (stock["2175HD"][1]) + (stock['123FHD'][1]) + (stock['342FHD'][1]) 
                    print(f"el total de HP es {total}")
                elif marca.lower() == "asus" :
                    total = (stock['JjfFHD'][1]) + (stock['GF75HD'][1]) 
                    print(f"el total de  es {total}")
                elif marca.lower() == "dell" :
                    total = (stock['UWU131HD'][1])
                    print(f"el total de es {total}")
                else :
                    print("ingreso mal la marca ")
            except ValueError:
                print("ingrese valores validos")
        elif opc == 2:
            try:
                mayor = int(input("ingrese el maximo de precio"))
                menor = int(input("ingrese el minimo de precio"))
                if mayor < menor:
                    print("ingreso mal los valores")
                if mayor> menor:
                    if mayor >= 300000 and menor <= 200000:
                        muertra = [stock["123FHD"]]
                        print(f"aser{muertra}")
                    elif mayor >= 400000 and menor <= 300000:
                        muertra = [stock["8475HD"]]
                        muertra2 = [stock['2175HD']]
                        muertra3 = [stock['UWU131HD']]
                        print(f"acer{muertra2}  hp {muertra}  dell{muertra3}" )
                    elif mayor >= 500000 and menor <= 400000:
                        muertra = [stock["342FHD"]]
                        muertra2 = [stock['JjfFHD']]
                        print(f"asus{muertra2}  acer {muertra} " )
                    elif mayor >= 600000 and menor <= 500000:
                        muertra = [stock["fgdxFHD"]]            
                        print(f"HP{muertra}   " )
                    elif mayor >= 700000 and menor <= 600000:
                        muertra = [stock['GF75HD']]
                        print(f"HP{muertra}   " )
                    else :
                        print("no hay en esos limites")
            except ValueError:
                print("ingrese numeros enteros")
        

        elif opc ==3 :
            while True:
                    elimina = input("ingrese producto a eliminar ")
                    if elimina == "8475HD":
                        del stock ['8475HD']
                        del productos ['8475HD']
                        print("se elimino el producto")
                        respuerta = input("quiere eliminar otro producto S/N")
                        if respuerta == "si":
                            print("gracias")
                        elif respuerta == "no":
                            break
                    elif elimina == "2175HD":
                        del stock ['2175HD']
                        del productos ['2175HD']
                        print("se elimino el producto")
                        respuerta = input("quiere eliminar otro producto S/N")
                        if respuerta == "si":
                            print("gracias")
                        elif respuerta == "no":
                            break
                    elif elimina == "JjfFHD":
                        del stock ['JjfFHD']
                        del productos ['JjfFHD']
                        print("se elimino el producto")
                        respuerta = input("quiere eliminar otro producto S/N")
                        if respuerta == "si":
                            print("gracias")
                        elif respuerta == "no":
                            break
                    elif elimina == "fgdxFHD":
                        del stock ['fgdxFHD']
                        del productos ['fgdxFHD']
                        print("se elimino el producto")
                        respuerta = input("quiere eliminar otro producto S/N")
                        if respuerta == "si":
                            print("gracias")
                        elif respuerta == "no":
                            break
                    elif elimina == "123FHD":
                        del stock ['123FHD']
                        del productos ['123FHD']
                        print("se elimino el producto")
                        respuerta = input("quiere eliminar otro producto S/N")
                        if respuerta == "si":
                            print("gracias")
                        elif respuerta == "no":
                            break
                    elif elimina == "342FHD":
                        del stock ['342FHD']
                        del productos ['342FHD']
                        print("se elimino el producto")
                        respuerta = input("quiere eliminar otro producto S/N")
                        if respuerta == "si":
                            print("gracias")
                        elif respuerta == "no":
                            break
                    elif elimina == "GF75HD":
                        del stock ['GF75HD']
                        del productos ['GF75HD']
                        print("se elimino el producto")
                        respuerta = input("quiere eliminar otro producto S/N")
                        if respuerta == "si":
                            print("gracias")
                        elif respuerta == "no":
                            break
                    elif elimina == "UWU131HD":
                        del stock ['UWU131HD']
                        del productos ['UWU131HD']
                        print("se elimino el producto")
                        respuerta = input("quiere eliminar otro producto S/N")
                        if respuerta == "si":
                            print("gracias")
                        elif respuerta == "no":
                            break
                    elif elimina == "FS1230HD":
                        del stock ['FS1230HD']
                        del productos ['FS1230HD']
                        print("se elimino el producto")
                        respuerta = input("quiere eliminar otro producto S/N")
                        if respuerta == "si":
                            print("gracias")
                        elif respuerta == "no":
                            break
                    else:
                        print("ingreso mal el productos")

        elif opc == 4:
            print("programa finalisado ")
            break

        