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
        attribute eangry:
            "blink_eangry"
        attribute econfused:
            "blink_econfused"
        attribute ehappy:
            "blink_ehappy"
        attribute eneutral_la:
            "blink_eneutral_la"
        attribute esad:
            "blink_esad"
        attribute esad_la:
            "blink_esad_la"
        attribute eshocked:
            "blink_eshocked"
        
    group mouth auto:
        attribute mhappy_c default
    
    group brows auto:
        attribute bneutral default

    group ears auto:
        attribute mid default
    
    group blush auto

    group cry auto

    group acc auto:
        attribute glasses default

## ~ Blinking ~ ##

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

image blink_eangry:
    
    "atticus_eyes_eangry"
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

image blink_econfused:
    "atticus_eyes_econfused"
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

image blink_ehappy:
    "atticus_eyes_ehappy"
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

image blink_eneutral_la:
    "atticus_eyes_eneutral_la"
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

image blink_esad:
    "atticus_eyes_esad"
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

image blink_esad_la:
    "atticus_eyes_esad_la"
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

image blink_eshocked:
    "atticus_eyes_eshocked"
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