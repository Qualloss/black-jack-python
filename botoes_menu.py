from msilib.schema import Class
import os
import webbrowser
import pyglet
import pyglet.shapes
import sys


class Widget:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clica(self, x, y):
        if self.contem_ponto(x, y):
            self.on_click()

    def on_click(self):
        print("Clicou em " + str(self))

    def digita(self, symbol):
        pass

    def contem_ponto(self, x, y):
        return x >= self.x and x <= self.x + self.width \
            and y >= self.y and y <= self.y + self.height

    def draw(self):
        pass

class BotaoSair(Widget):
    def __init__(self, x, y, width, height, texto):
        super().__init__(x, y, width, height)
        self.texto = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(128,0,0), border_color=(255, 255, 255))
        self.label = pyglet.text.Label(self.texto,
                font_name='Arial',
                font_size=32,
                anchor_x='center', anchor_y='center',
                x = self.x + self.width // 2,
                y = self.y + self.height // 2)
    def draw(self):
        self.moldura.draw()
        self.label.draw()
    def on_click(self):
        os._exit(0)
    def __repr__(self):
        return f"Botão '{self.texto}'"


class BotaoAjuda(Widget):
    def __init__(self, x, y, width, height, texto):
        super().__init__(x, y, width, height)
        self.texto = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(0,0,255), border_color=(255, 255, 255))
        self.label = pyglet.text.Label(self.texto,
                font_name='Arial',
                font_size=32,
                anchor_x='center', anchor_y='center',
                x = self.x + self.width // 2,
                y = self.y + self.height // 2)
    def draw(self):
        self.moldura.draw()
        self.label.draw()
    def on_click(self):
        webbrowser.open("https://www.pokerstars.com/pt-BR/casino/how-to-play/blackjack/rules/")
    def __repr__(self):
        return f"Botão '{self.texto}'"

class QuantiaInicial(Widget):
    def __init__(self, x, y, width, height, texto=""):
        super().__init__(x, y, width, height)
        self.selecionado = False
        self.texto = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(0,128,0), border_color=(255, 255, 255))
        self.linha = pyglet.shapes.Line(x, y + 5, x + width, y + 5)
        self.label = pyglet.text.Label(self.texto,
                font_name='Arial',
                font_size=32,
                anchor_x='center', anchor_y='center',
                x = self.x + self.width // 2,
                y = self.y + self.height // 2)
    def draw(self):
        if self.selecionado:
            self.moldura.draw()
        self.linha.draw()
        self.label.draw()
    def clica(self, x, y):
        self.selecionado = False
        super().clica(x, y)
    def on_click(self):
        self.selecionado = True
        self.label.text = ""
        

    def digita(self, symbol):
        if not self.selecionado:
            return

        if symbol == "BACKSPACE":
            self.label.text = self.label.text[0:-1]
        else:
            self.label.text += symbol

    def __repr__(self):
        return f"Input '{self.texto}'"

class BotaoComecar(Widget):
    def __init__(self, x, y, width, height, texto):
        super().__init__(x, y, width, height)
        self.texto = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(0,75,0), border_color=(255, 255, 255))
        self.label = pyglet.text.Label(self.texto,
                font_name='Arial',
                font_size=32,
                anchor_x='center', anchor_y='center',
                x = self.x + self.width // 2,
                y = self.y + self.height // 2)
    def draw(self):
        self.moldura.draw()
        self.label.draw()
    def on_click(self):
        print("Agora o jogo começa !")
    def __repr__(self):
        return f"Botão '{self.texto}'"