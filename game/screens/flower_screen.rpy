 
init -1 python:
    class Flowers():
        def __init__ (self, image, correct):
            self.image = image
            self.correct = correct

        def RightChoice(self, newimage):
            self.correct = True
            self.image = newimage
            return
image default_flower:
    "gui/flower_bud.png"
    # replace with final image file
image bloomed_flower: 
    "gui/bloomed_flower.png"
    # replace with final image file
image bloomed_flower_2: 
    "images/profile images/icon momo.png"
    # replace with final image file

default Flower1 = Flowers("default_flower", False)
default Flower2 = Flowers("default_flower", False)
default Flower3 = Flowers("default_flower", False)
default Flower4 = Flowers("default_flower", False)
default Flower5 = Flowers("default_flower", False)
default Flower6 = Flowers("default_flower", False)
default Flower7 = Flowers("default_flower", False)
default Flower8 = Flowers("default_flower", False)

default left_flowers = [Flower1, Flower2, Flower3, Flower4]
default right_flowers = [Flower5, Flower6, Flower7, Flower8]

screen flower_frame():
    frame:
        background Solid("#00cb07")
        xsize 0.02 ysize 0.4 # cut this when we have an actual image
        xalign 0.0 yanchor 0.5 ypos 0.3
        # replace the background with None and add an image when we have the image
        vbox:
            spacing 20
            for i in left_flowers:
                add i.image zoom 0.25 # might remove the zoom depending on how big the final flowers are


    frame:
        background Solid("#00cb07")
        xsize 0.02 ysize 0.4 # cut this when we have an actual image
        xalign 1.0 yanchor 0.5 ypos 0.3
        # replace the background with None and add an image when we have the image
        vbox:
            spacing 20
            for i in right_flowers:
                add i.image zoom 0.25 # might remove the zoom depending on how big the final flowers are

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
