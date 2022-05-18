import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    scene_width = 800
    scene_height = 500

    canvas = start_drawing("Scene", scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    """Here we draw the sky and the objects in the sky"""
    draw_rectangle(canvas, 0, scene_height / 3,
    scene_width, scene_height, width=0, fill="lightBlue1")

    #######  snow  #########
    diameter = 15
    space = 5
    interval = diameter + space
    half_height = round(scene_height / 2)
    min_diam = 5
    max_diam = 20
    for i in range(150):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, 480)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, 
                fill="snow1")

    ###### Sun #######
    diameter = 185
    x = -30
    y = 420  
    number = random.randint(1, 5)
    draw_oval(canvas, x, y,
         x + diameter, y + diameter, fill="yellow2")
    #######  cloud  #########
    diameter = 95
    x = 50
    y = 435  
    draw_oval(canvas, 700, y,
         x + diameter, y + diameter, fill="white")
    diameter = 185
    x = 100
    y = 420  
    draw_oval(canvas, 700, y,
         x + diameter, y + diameter, fill="white")
    diameter = 215
    x = 150
    y = 420  
    draw_oval(canvas, 800, y,
         x + diameter, y + diameter, fill="white")
    diameter = 105
    x = 10
    y = 460  
    draw_oval(canvas, 700, y,
         x + diameter, y + diameter, fill="white")


def  draw_ground ( canvas, scene_width, scene_height ): 
    """everything we put on the floor and the floor""" 
    draw_rectangle(canvas, 0 , 0 ,
        scene_width, scene_height / 5 , width= 0 , fill= "tan" )

    # Pine1 
    tree_center_x = 170 
    tree_bottom = 65 
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    #Pine2 
    
    tree_center_x = 490 
    tree_bottom = 70 
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
                tree_bottom, tree_height)
    
    # Pine3 
    tree_center_x = 60 
    tree_bottom = 35 
    tree_height = 240
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    # Pineo4 
    tree_center_x = 390 
    tree_bottom = 35 
    tree_height = 240
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    
    
    tree_center_x = 100 
    tree_bottom = 20 
    tree_height = 240
    for i in range(10):
        tree_center_x = random.randint(0, scene_width - tree_center_x)
        tree_height = random.randint(200, tree_height)
        draw_cut_trunk(canvas, tree_center_x,
            tree_bottom, tree_height)
    
    



def  draw_pine_tree ( canvas, center_x, bottom, height ): 
    """Pine
        Parâmetros
        canvas: where this function will draw a pine tree.
        center_x, bottom: The x and y location in pixels where this function will draw the bottom of a pine.
        height: The height in pixels of the pine tree that this function will draw.
    Return: none
    """ 
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_cut_trunk(canvas, center_x, bottom, height):
        """   cut_trunk
        Parâmetros
        canvas: where this function will draw a cut_trunk
        center_x, bottom: The x and y location in pixels where this function will draw the cut_trunk.
        height: The height in pixels of the cut_trunk  that this function will draw.
    Return: none
    
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
        skirt_top = bottom 

    

main()