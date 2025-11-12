
def total_iva(precio: float, iva: float=16) -> float:
    """
    Calcula el precio total + el IVA.
    
    Args:
        precio (float): El precio base del producto sin IVA
        tasa_iva (float): La tasa de IVA a aplicar (por defecto 16%)
    
    Returns:
        float: El precio final con el IVA incluido
    """
    
    iva = precio * (iva / 100)
    precio_final = precio + iva
    
    return precio_final

print("Cálculo de IVA con tasa por defecto (16%) y personalizada.\n")
# Ejemplo 1: Producto con IVA por defecto
precio_base:float = 100.00
precio_con_iva:float = total_iva(precio_base)
print(f"Precio base: ${precio_base}")
print(f"Precio con IVA (16%): ${precio_con_iva:.2f}")
# Ejemplo 2: Producto con IVA personalizado
tasa_iva_personalizada:float = 18 
precio_con_iva_personalizado:float = total_iva(precio_base, tasa_iva_personalizada)
print(f"\nPrecio base: ${precio_base}")
print(f"Precio con IVA ({tasa_iva_personalizada}%): ${precio_con_iva_personalizado:.2f}")
# Ejemplo 3: usando iteración para varios productos
precios: list[float] = [50.25, 150.50, 250.75, 350.99]
print("\nCálculo de IVA para múltiples productos:")
for precio in precios:
    precio_final:float = total_iva(precio)
    print(f"Precio base: ${precio} -> Precio con IVA (16%): ${precio_final:.2f}")

