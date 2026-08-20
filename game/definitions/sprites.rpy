## meow ##

layeredimage atticus:
    zoom 0.37 #bc the sprite is insanely huge
    xalign 0.53 #bc the tail makes him off-center

    always "base" # the body

    group tail auto:
        attribute tneutral default
    
    group eyes auto:
        attribute eneutral_o default:
            "blink_eneutral_o"

    group mouth auto:
        attribute mhappy_c default
    
    group brows auto:
        attribute bneutral default

    group ears auto:
        attribute mid default
    
    group blush auto

    group acc auto:
        attribute glasses default

## If you have a better way to do blink, please be my guest!
## If not, you can just copy paste this... Like 6 more times

image blink_eneutral_o:
    "atticus_eyes_eneutral_o"
    choice:
        6.0
    choice:
        .3
    choice:
        3.0
    choice:
        4.5
    "atticus_eyes_eneutral_c"
    .2
    repeat