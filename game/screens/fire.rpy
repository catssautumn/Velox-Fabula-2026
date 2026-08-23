image big_fire:
    "screens/fire.png"
    blend "add"
        
    zoom 0.25
    
        
image med_fire:
    "screens/fire.png"
    blend "add"
    zoom 0.15

image small_fire:
    "screens/fire.png"
    blend "add"
    zoom 0.1
image bfire_anim:
    "big_fire"
    choice:
        1.0
    choice:
        .3
    choice:
        2.0
    choice:
        1.5
    xzoom -1
    choice:
        1.0
    choice:
        .3
    choice:
        2.0
    choice:
        1.5
    xzoom 1
    
    repeat

image mfire_anim:
    "med_fire"
    choice:
        1.0
    choice:
        .3
    choice:
        2.0
    choice:
        1.5
    xzoom -1
    choice:
        1.0
    choice:
        .3
    choice:
        2.0
    choice:
        1.5
    xzoom 1
    
    repeat

image sfire_anim:
    "small_fire"
    choice:
        1.0
    choice:
        .3
    choice:
        2.0
    choice:
        1.5
    xzoom -1
    choice:
        1.0
    choice:
        .3
    choice:
        2.0
    choice:
        1.5
    xzoom 1
    
    repeat
image fire_bad:
    contains:
        "darken"
    contains:
        "bfire_anim" 
        xalign 0.0 yalign 1.0 
    contains:
        "bfire_anim" 
        xalign 1.0 yalign 1.0 
        
    contains:
        "mfire_anim"
        xanchor 0.5 xpos 0.8 yalign 1.0
    contains:
        "mfire_anim"
        xanchor 0.5 xpos 0.05 yalign 1.0
    contains:
        "mfire_anim"
        xanchor 0.5 xpos 0.2 yalign 1.0
    contains:
        "mfire_anim"
        xanchor 0.5 xpos 0.3 yanchor 1.0 ypos 0.8
    contains:
        "bfire_anim"
        xanchor 0.5 xpos 0.5 yanchor 1.0 ypos 0.98
    contains:
        "mfire_anim"
        xanchor 0.5 xpos 0.4 yanchor 1.0 ypos 0.98
    contains:
        "mfire_anim"
        xanchor 0.5 xpos 0.6 yanchor 1.0 ypos 0.98
    contains:
        "sfire_anim"
        xanchor 0.5 xpos 0.5 yanchor 1.0 ypos 0.7
    contains:
        "sfire_anim"
        xanchor 0.5 xpos 0.65 yanchor 1.0 ypos 0.7
