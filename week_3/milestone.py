
# Importe as funções da biblioteca Draw 2-D 
# para que possam ser usadas neste programa. 
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def  main (): 
    scene_width = 800 
    scene_height = 500

    # Chame a função start_drawing 
    #na biblioteca draw2d.py # que abrirá uma janela e criará uma tela. 
    canvas = start_drawing( "Scene" , scene_width, scene_height)

    # Chame as funções draw_sky e draw_ground neste arquivo.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Chame a função finish_drawing 
    # na biblioteca draw2d.py.
    finish_drawing(canvas)


def  draw_sky ( canvas, scene_width, scene_height ): 
    """Desenhe o céu e todos os objetos no céu.""" 
    draw_rectangle(canvas, 0 , scene_height / 3 ,
        scene_width, scene_height, width= 0 , fill= "sky blue" )


def  draw_ground ( canvas, scene_width, scene_height ): 
    """Desenhe o chão e todos os objetos no chão.""" 
    draw_rectangle(canvas, 0 , 0 ,
        scene_width, scene_height / 3 , width= 0 , fill= "tan4" )

    # Desenhe um pinheiro. 
    tree_center_x = 170 
    tree_bottom = 100 
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Desenhe outro pinheiro. 
    tree_center_x = 90 
    tree_bottom = 70 
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)


def  draw_pine_tree ( canvas, center_x, bottom, height ): 
    """Desenhe um único pinheiro.
    Parâmetros
        canvas: A tela onde esta função
            desenhará um pinheiro.
        center_x, bottom: A localização x e y em pixels onde
            esta função irá desenhar a parte inferior de um pinheiro.
        altura: A altura em pixels do pinheiro que
            esta função irá desenhar.
    Retorno: nada
    """ 
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Desenhe o tronco do pinheiro.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Desenhe a coroa (também chamada de saia) do pinheiro.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")


# Chama a função main para que 
# este programa comece a ser executado. 
main()