lista_productos = {lista_productos}

def extraer(data):
    productos = []
    for item in data:
        if not isinstance(item, list) or not item:
            continue
        
        texto = item[0].get('text', '')
        lineas = [l.strip() for l in texto.split('\n') if l.strip()]
        
        nombre = next((l for l in lineas if len(l) > 10 and 'Gs.' not in l and 'Desde' not in l), None)
        precio = next((l.replace('Gs.', '').replace('\xa0', '').strip() for l in lineas if 'Gs.' in l), None)
        
        url = [None]
        def buscar(elem):
            if isinstance(elem, dict):
                if 'href' in elem:
                    url[0] = elem['href']
                else:
                    for v in elem.values():
                        buscar(v)
            elif isinstance(elem, list):
                for v in elem:
                    buscar(v)
        buscar(item)
        
        if nombre or precio:
            productos.append({'nombre': nombre, 'precio': precio, 'url': url[0]})
    return productos

# Extraemos todos los productos de una vez
productos_finales = extraer(lista_productos)

# Guardamos la lista completa en una sola variable de Rocketbot
SetVar("productos_finales", productos_finales)

# Opcional: Imprimir en consola para verificar
for i, prod in enumerate(productos_finales, 1):
    print(f"Producto {i}: {prod['nombre']} - {prod['precio']} - {prod['url']}")