# -*- encoding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar()


class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self):
        self.pilas.fondos.FondoMozaico('imagenes/limbo.png')
        actor_texto = self.pilas.actores.Actor()
        actor_texto.imagen = "imagenes/play.png"
        self._aplicar_animacion(actor_texto)
        self.pilas.eventos.click_de_mouse.conectar(self._iniciar_el_juego)
        self._crear_el_titulo_del_juego()
        self._crear_indicador_creditos()

    def _aplicar_animacion(self, texto):
        texto.y = -150
        texto.escala = 5
        texto.escala = [0.8], 1.1
        
    def _iniciar_el_juego(self, evento):
        self.pilas.escenas.EscenaJuego()

    def _crear_el_titulo_del_juego(self):
        titulo = self.pilas.actores.Actor()
        titulo.imagen = "imagenes/Lost.png"
        titulo.escala = 0.5
        titulo.y = 150
        titulo.x = 0
        titulo.rotacion = 30
        titulo.rotacion = [0], 1.2

    def _crear_indicador_creditos(self):
        actor = self.pilas.actores.Actor()
        actor.imagen = "imagenes/credits.png"
        actor.x = 300
        actor.y = -200
        actor.escala = 0.5
        actor.x = [400, 400, 270], 0.5

## Vinculamos todas las escenas.
pilas.escenas.vincular(EscenaMenu)


# Se inicia la escena principal.
pilas.escenas.EscenaMenu()

pilas.ejecutar()
