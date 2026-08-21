 
init -1 python:
    class Flowers():
        def __init__ (self, minimum, image, bloomed_image, xpos, ypos, blooming_img, wither_img):
            self.minimum = minimum
            self.image = image
            self.bloomed_image = bloomed_image
            self.xpos = xpos
            self.ypos = ypos
            self.blooming_img = blooming_img
            self.wither_img = wither_img

    def add_aff(amount):
        global at_aff
        global hint_flowers_showing
        global total_flowers 
        at_aff += amount
        
        if hint_flowers_showing:
            for i in total_flowers:
                if at_aff >= i.minimum:
                    i.image = i.blooming_img
            renpy.sound.play("audio/sound/positive.mp3") #replace with whatever the raise affectionsound is
    def sub_aff(amount):
        global at_aff
        global hint_flowers_showing
        at_aff -= amount
        
        if hint_flowers_showing:
            for i in total_flowers:
                if at_aff <= i.minimum:
                    i.image = i.wither_img
        if hint_flowers_showing:
            renpy.sound.play("audio/soud/negative.mp3") #replace with whatever the lower affection sound is

image default_flower:
    "gui/flower_bud.png"
    # replace with final image file
image bloomed_flower: 
    "gui/bloomed_flower.png"
    # replace with final image file
image bloomed_flower_2: 
    "images/profile images/icon momo.png"
    # replace with final image file

default Flower1 = Flowers(1, "pink_bud", "pink_flower", 0.125, 0.075, "pink_blooming", "pink_wither")
default Flower2 = Flowers(2, "red_bud", "red_flower", 0.0575, 0.05, "red_blooming", "red_wither")
default Flower3 = Flowers(3, "gold_bud", "gold_flower", 0.025, 0.145, "gold_blooming", "gold_wither")
default Flower4 = Flowers(4, "dark_bud", "dark_flower", 0.035, 0.275, "dark_blooming", "dark_wither")
default Flower5 = Flowers(5, "blue_bud", "blue_flower", 0.025, 0.425, "blue_blooming", "blue_wither")
default Flower6 = Flowers(6, "white_bud", "white_flower", 0.025, 0.575, "white_blooming", "white_wither")
default Flower7 = Flowers(7, "pink_bud_2", "pink_flower_2", 0.875, 0.075, "pink_blooming_2", "pink_wither_2")
default Flower8 = Flowers(8, "red_bud_2", "red_flower_2", 0.9525, 0.05, "red_blooming_2", "red_wither_2")
default Flower9 = Flowers(9, "gold_bud_2", "gold_flower_2", 0.975, 0.145, "gold_blooming_2", "gold_wither_2")
default Flower10 = Flowers(10, "dark_bud_2", "dark_flower_2", 0.965, 0.275, "dark_blooming_2", "dark_wither_2")
default Flower11 = Flowers(11, "blue_bud_2", "blue_flower_2", 0.975, 0.425, "blue_blooming_2", "blue_wither_2")
default Flower12 = Flowers(12, "white_bud_2", "white_flower_2", 0.975, 0.575, "white_blooming_2", "white_wither_2")

image pink_blooming:
    "pink_bud"
    "pink_flower" with dissolve
image red_blooming:
    "red_bud"
    "red_flower" with dissolve
image gold_blooming:
    "gold_bud"
    "gold_flower" with dissolve
image dark_blooming:
    "dark_bud"
    "dark_flower" with dissolve
image blue_blooming:
    "blue_bud"
    "blue_flower" with dissolve
image white_blooming:
    "white_bud"
    "white_flower" with dissolve
image pink_blooming_2:
    "pink_bud_2"
    "pink_flower_2" with dissolve
image red_blooming_2:
    "red_bud_2"
    "red_flower_2" with dissolve
image gold_blooming_2:
    "gold_bud_2"
    "gold_flower_2" with dissolve
image dark_blooming_2:
    "dark_bud_2"
    "dark_flower_2" with dissolve
image blue_blooming_2:
    "blue_bud_2"
    "blue_flower_2" with dissolve
image white_blooming_2:
    "white_bud_2"
    "white_flower_2" with dissolve
image pink_wither:
    "pink_flower"
    "pink_bud" with dissolve
image red_wither:
    "red_flower"
    "red_bud" with dissolve
image gold_wither:
    "gold_flower"
    "gold_bud" with dissolve
image dark_wither:
    "dark_flower"
    "dark_bud" with dissolve
image blue_wither:
    "blue_flower"
    "blue_bud" with dissolve
image white_wither:
    "white_flower"
    "white_bud" with dissolve
image pink_wither_2:
    "pink_flower_2"
    "pink_bud_2" with dissolve
image red_wither_2:
    "red_flower_2"
    "red_bud_2" with dissolve
image gold_wither_2:
    "gold_flower_2"
    "gold_bud_2" with dissolve
image dark_wither_2:
    "dark_flower_2"
    "dark_bud_2" with dissolve
image blue_wither_2:
    "blue_flower_2"
    "blue_bud_2" with dissolve
image white_wither_2:
    "white_flower_2"
    "white_bud_2" with dissolve
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


# this is the most absolutely fucked way of doing this but it worked #WorkDumberNotHarder #IfItsStupidAndItWorksItsNotStupid




default left_flowers = [Flower1, Flower2, Flower3, Flower4, Flower5, Flower6]
default right_flowers = [Flower7, Flower8, Flower9, Flower10, Flower11, Flower12]
default total_flowers = [Flower1, Flower2, Flower3, Flower4, Flower5, Flower6, Flower7, Flower8, Flower9, Flower10, Flower11, Flower12]

screen flower_frame():
    frame:
        background None
        add "gui/border.png" xalign 0.5 yalign 0.5
        # replace the background with None and add an image when we have the image
        
        
        if hint_flowers_showing:
            for i in left_flowers:
                add i.image xanchor 0.5 yanchor 0.5 xpos i.xpos ypos i.ypos
        else:
            for i in left_flowers:
                add i.bloomed_image xanchor 0.5 yanchor 0.5 xpos i.xpos ypos i.ypos


    
        if hint_flowers_showing:
            for i in right_flowers:
                add i.image xanchor 0.5 yanchor 0.5 xpos i.xpos ypos i.ypos
        else:
            for i in right_flowers:
                add i.bloomed_image xanchor 0.5 yanchor 0.5 xpos i.xpos ypos i.ypos


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
