 
init -1 python:
    class Flowers():
        def __init__ (self, minimum, bud_image, bloomed_image, xpos, ypos):
            self.minimum = minimum
            self.bud_image = bud_image
            self.bloomed_image = bloomed_image
            self.xpos = xpos
            self.ypos = ypos

image default_flower:
    "gui/flower_bud.png"
    # replace with final image file
image bloomed_flower: 
    "gui/bloomed_flower.png"
    # replace with final image file
image bloomed_flower_2: 
    "images/profile images/icon momo.png"
    # replace with final image file

default Flower1 = Flowers(1, "pink_bud", "pink_flower", 0.125, 0.075)
default Flower2 = Flowers(2, "red_bud", "red_flower", 0.0575, 0.05)
default Flower3 = Flowers(3, "gold_bud", "gold_flower", 0.025, 0.145)
default Flower4 = Flowers(4, "dark_bud", "dark_flower", 0.035, 0.275)
default Flower5 = Flowers(5, "blue_bud", "blue_flower", 0.025, 0.425)
default Flower6 = Flowers(6, "white_bud", "white_flower", 0.025, 0.575)
default Flower7 = Flowers(7, "pink_bud_2", "pink_flower_2", 0.875, 0.075)
default Flower8 = Flowers(8, "red_bud_2", "red_flower_2", 0.9525, 0.05)
default Flower9 = Flowers(9, "gold_bud_2", "gold_flower_2", 0.975, 0.145)
default Flower10 = Flowers(10, "dark_bud_2", "dark_flower_2", 0.965, 0.275)
default Flower11 = Flowers(11, "blue_bud_2", "blue_flower_2", 0.975, 0.425)
default Flower12 = Flowers(12, "white_bud_2", "white_flower_2", 0.975, 0.575)

image pink_bud:
    "gui/flowers/pink_bud.png"
image pink_bud_2:
    "gui/flowers/pink_bud.png"
    xzoom -1
image pink_flower:
    "gui/flowers/pink_flower.png"
image pink_flower_2:
    "gui/flowers/pink_flower.png"
    xzoom -1
image red_bud:
    "gui/flowers/red_bud.png"  
image red_bud_2:
    "gui/flowers/red_bud.png"
    xzoom -1
image red_flower:
    "gui/flowers/red_flower.png"
image red_flower_2:
    "gui/flowers/red_flower.png"
    xzoom -1
image dark_bud:
    "gui/flowers/dark_bud.png"
image dark_bud_2:
    "gui/flowers/dark_bud.png"
    xzoom -1
image dark_flower:
    "gui/flowers/dark_flower.png"
image dark_flower_2:
    "gui/flowers/dark_flower.png"
    xzoom -1
image gold_bud:
    "gui/flowers/gold_bud.png"
image gold_bud_2:
    "gui/flowers/gold_bud.png"
    xzoom -1
image gold_flower:
    "gui/flowers/gold_flower.png"
image gold_flower_2:
    "gui/flowers/gold_flower.png"
    xzoom -1
image blue_bud:
    "gui/flowers/blue_bud.png"
image blue_bud_2:
    "gui/flowers/blue_bud.png"
    xzoom -1
image blue_flower:
    "gui/flowers/blue_flower.png"
image blue_flower_2:
    "gui/flowers/blue_flower.png"
    xzoom -1
image white_bud:
    "gui/flowers/white_bud.png"
image white_bud_2:
    "gui/flowers/white_bud.png"
    xzoom -1
image white_flower:
    "gui/flowers/white_flower.png"
image white_flower_2:
    "gui/flowers/white_flower.png"
    xzoom -1







default left_flowers = [Flower1, Flower2, Flower3, Flower4, Flower5, Flower6]
default right_flowers = [Flower7, Flower8, Flower9, Flower10, Flower11, Flower12]

screen flower_frame():
    frame:
        background None
        add "gui/border.png" xalign 0.5 yalign 0.5
        # replace the background with None and add an image when we have the image
        
        
        if hint_flowers_showing:
            for i in left_flowers:
                if at_aff >= i.minimum:
                    add i.bloomed_image xanchor 0.5 yanchor 0.5 xpos i.xpos ypos i.ypos
                else:
                    add i.bud_image xanchor 0.5 yanchor 0.5 xpos i.xpos ypos i.ypos
        else:
            for i in left_flowers:
                add i.bloomed_image xanchor 0.5 yanchor 0.5 xpos i.xpos ypos i.ypos


    
        if hint_flowers_showing:
            for i in right_flowers:
                if at_aff >= i.minimum:
                    add i.bloomed_image xanchor 0.5 yanchor 0.5 xpos i.xpos ypos i.ypos
                else:
                    add i.bud_image xanchor 0.5 yanchor 0.5 xpos i.xpos ypos i.ypos
        else:
            for i in right_flowers:
                add i.bloomed_image xanchor 0.5 yanchor 0.5 xpos i.xpos ypos i.ypos


