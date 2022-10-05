import os
from botoes_menu import BotaoAjuda, BotaoSair, QuantiaInicial, BotaoComecar
import pyglet

class MeuMenu(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height,
            caption="BlackJack")

        self.input_nome = QuantiaInicial(465, 200, 300, 70, "Quantia Inicial:")
        self.btn_ajuda = BotaoAjuda(100, 100, 200, 70, "Regras")
        self.btn_sair = BotaoSair(1000, 100, 200, 70, "Sair")
        self.btn_comecar = BotaoComecar(465,50,300,70,"Vamos Jogar")
        self.logo = pyglet.resource.image('reduxx.png')
        self.fundo = pyglet.resource.image('mesablackjack.jpg')
        self.widgets = [self.btn_ajuda, self.btn_sair, self.input_nome, self.btn_comecar]
        self.titulo_label = pyglet.text.Label('BlackJack',
                        color = (255,255,0,255),
                        font_name='Action Man',
                        font_size=72,
                        x=620, y=500,
                        anchor_x='center', anchor_y='center')

    def on_draw(self):
        self.clear()
        self.fundo.blit(0,0)
        #self.logo.blit(0,0)
        for widget in self.widgets:
            widget.draw()
        self.titulo_label.draw()
        
    def on_text(self, text):
        for widget in self.widgets:
            widget.digita(text)
        
    def on_key_press(self, symbol, modifiers):
        for widget in self.widgets:
            if symbol == pyglet.window.key.BACKSPACE:
                widget.digita("BACKSPACE")

    def on_mouse_press(self, x, y, button, modifiers):
        for widget in self.widgets:
            widget.clica(x, y)

    


window = MeuMenu(1280, 720)

pyglet.app.run()