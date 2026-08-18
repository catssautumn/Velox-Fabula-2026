 
init -1 python:
    class Flowers():
        def __init__ (self, minimum, bud_image, bloomed_image):
            self.minimum = minimum
            self.bud_image = bud_image
            self.bloomed_image = bloomed_image

image default_flower:
    "gui/flower_bud.png"
    # replace with final image file
image bloomed_flower: 
    "gui/bloomed_flower.png"
    # replace with final image file
image bloomed_flower_2: 
    "images/profile images/icon momo.png"
    # replace with final image file

default Flower1 = Flowers(1, "pink_bud", "pink_flower")
default Flower2 = Flowers(2, "red_bud", "red_flower")
default Flower3 = Flowers(3, "gold_bud", "gold_flower")
default Flower4 = Flowers(4, "dark_bud", "dark_flower")
default Flower5 = Flowers(5, "blue_bud", "blue_flower")
default Flower6 = Flowers(6, "white_bud", "white_flower")
default Flower7 = Flowers(7, "pink_bud_2", "pink_flower_2")
default Flower8 = Flowers(8, "red_bud_2", "red_flower_2")
default Flower9 = Flowers(9, "gold_bud_2", "gold_flower_2")
default Flower10 = Flowers(10, "dark_bud_2", "dark_flower_2")
default Flower11 = Flowers(11, "blue_bud_2", "blue_flower_2")
default Flower12 = Flowers(12, "white_bud_2", "white_flower_2")

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






image border_1:
 "border.png" # WHATEVER FOLDER IT'S IN
image border_2:
 "border.png"
 xzoom -1

default left_flowers = [Flower1, Flower2, Flower3, Flower4, Flower5, Flower6]
default right_flowers = [Flower7, Flower8, Flower9, Flower10, Flower11, Flower12]

screen flower_frame():
    frame:
        background None
        xsize 0.02 ysize 0.4 # cut this when we have an actual image
        xalign 0.0 yanchor 0.5 ypos 0.3
        add "border_1"
        # replace the background with None and add an image when we have the image
        if hint_flowers_showing:
          vbox:
              spacing 20
              for i in left_flowers:
                  if at_aff >= i.minimum:
                      add i.bloomed_image
                  else:
                      add i.bud_image


    frame:
        background None
        xsize 0.02 ysize 0.4 # cut this when we have an actual image
        xalign 1.0 yanchor 0.5 ypos 0.3
        add "border_2"
        # replace the background with None and add an image when we have the image
        if hint_flowers_showing:
         vbox:
             spacing 20
             for i in right_flowers:
                 if at_aff >= i.minimum:
                     add i.bloomed_image
                 else:
                     add i.bud_image

#     show screen flower_frame()
#     menu:
#         "Right Choice":
#             $ Flower1.RightChoice("bloomed_flower")
#         "Wrong Choice":
#             pass
        
#     menu:
#         "Right Choice":
#             $ Flower2.RightChoice("bloomed_flower_2")
#         "Wrong Choice":
#             pass
        # example of how to use this. we can add or remove flowers. use different strings for different images
