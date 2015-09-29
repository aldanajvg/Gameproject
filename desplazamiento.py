import pilasengine

pilas = pilasengine.iniciar()

fondo = pilas.fondos.DesplazamientoHorizontal()

fondo.agregar("ayuda.jpg", velocidad=0.2)
fondo.agregar("SwampTree.png", y=300, velocidad=0.5)
fondo.agregar("tallgrass.png", y=100, velocidad=0.9)
fondo.agregar("pasto.png", y=200, velocidad=2)
fondo.agregar("grass.png", y=200, velocidad=2)

p = pilas.actores.Shaolin(y=-200, x=0)

def cambiar_posicion_camara():
    pilas.camara.x += (p.x - pilas.camara.x) /5
    return True

pilas.tareas.agregar(1/80.0, cambiar_posicion_camara)
pilas.avisar("escapa hacia un mundo libre.")
pilas.ejecutar()
