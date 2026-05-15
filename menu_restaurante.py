#  Gestión de precios de menú con promociones

# Matriz del menú: [Nombre del Producto, Categoría, Precio Base]
menu = [
    ["Lomo Saltado",       "Plato Principal", 32000],
    ["Ensalada César",     "Entrada",         18000],
    ["Costillas BBQ",      "Plato Principal", 45000],
    ["Limonada de Coco",   "Bebida",          12000],
    ["Tiramisú",           "Postre",          22000],
    ["Pechuga a la Parrilla", "Plato Principal", 28000],
]

# Parámetros de la promoción
CATEGORIA_OBJETIVO = "Plato Principal"
UMBRAL_PRECIO      = 30000   # Solo aplica si el precio base supera este valor
DESCUENTO          = 0.15    # 15 % de descuento


# Módulo (función): calcula el precio final según la promoción
def calcular_precio_final(nombre, categoria, precio_base,
                            categoria_objetivo, umbral, descuento):
    """
    Retorna el precio final aplicando un descuento si el producto
    pertenece a la categoría objetivo Y su precio base supera el umbral.
    En caso contrario, retorna el precio base sin cambios.
    """
    if categoria == categoria_objetivo and precio_base > umbral:
        precio_final = precio_base * (1 - descuento)
    else:
        precio_final = precio_base

    return precio_final


# Salida: encabezado de la tabla
ancho = 70
print("=" * ancho)
print(" MENÚ DEL RESTAURANTE — PROMOCIÓN 15 % EN PLATOS PRINCIPALES > $30 000")
print("=" * ancho)
print(f"{'Producto':<25} {'Categoría':<18} {'Precio Base':>12} {'Precio Final':>12}")
print("-" * ancho)

# Recorrido de la matriz y aplicación del módulo
for producto in menu:
    nombre      = producto[0]
    categoria   = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(
        nombre, categoria, precio_base,
        CATEGORIA_OBJETIVO, UMBRAL_PRECIO, DESCUENTO
    )

    # Indicador visual cuando se aplica descuento
    indicador = " ✓" if precio_final < precio_base else ""

    print(
        f"{nombre:<25} {categoria:<18} "
        f"${precio_base:>10,.0f} ${precio_final:>10,.0f}{indicador}"
    )

# Pie de tabla
print("-" * ancho)
print(f"  ✓ = Descuento del {int(DESCUENTO*100)}% aplicado")
print("=" * ancho)