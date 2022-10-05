from botoes_menu import BotaoAjuda, BotaoSair, QuantiaInicial
import pyglet

window = pyglet.window.Window(1366,768,"BlackJack",fullscreen = False)

score_draw = False
menu = True

input_valor_inicial = QuantiaInicial(100,400,300,70,"Quantia Inicial:")
btn_regras = BotaoAjuda(100,200,200,70,"Regras")
btn_sair = BotaoSair(100,200,200,70,"Sair")

widgets = [input_valor_inicial,btn_regras,btn_sair]

mao_label = pyglet.text.Label()
aposta_label = pyglet.text.Label(anchor_x= 'right')
titulo_label = pyglet.text.Label('BlackJack',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

fundo = pyglet.resource.image('mesablackjack.jpg')

@window.event
def on_draw():
    window.clear()

    if menu:
        fundo.blit(0,0)
        t = titulo_label
        t.draw()
        for widdget in widgets:
            widdget.draw()


    else:
        m = mao_label
        m.text = f'Valor da sua Mão: '
        m.font_size = window.height//30
        m.draw()

        bet = aposta_label
        bet.text = f'Valor da aposta: '
        bet.font_size = window.height//30
        bet.x = window.width
        bet.draw()


pyglet.app.run()