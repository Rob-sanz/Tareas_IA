##Cantiodades por producto

ventas = {
    "Producto": ["A", "B", "A", "C", "B", "A"],
    "Cantidad": [10, 5, 7, 3, 2, 8]
}
resultado = {}

for producto, cantidad in zip(ventas["Producto"], ventas["Cantidad"]):
    if producto in resultado:
        resultado[producto] += cantidad
    else:
        resultado[producto] = cantidad

print(resultado)
