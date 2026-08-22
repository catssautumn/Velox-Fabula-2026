## ~ Backgrounds ~ ##
image forest day = "images/bgs/forest day.webp"
image forest night = "images/bgs/forest night.webp"
image interior day = "images/bgs/interior day.webp"
image interior night = "images/bgs/interior night.webp"

## BG Effects
image red haze = "images/bgs/red haze.webp"
image bloodstain = "images/bgs/bloodstain.webp"
image darken:
    "images/bgs/blackout.png"
    alpha 0.5 blend "multiply"

## Note: CGs are declared in gallery screen 

## Tints
transform forest_night:
    matrixcolor TintMatrix("#cecee2")*SaturationMatrix(1.0000)*ContrastMatrix(1.0000)

## ~ Transforms ~ ##
transform jump:
    linear .1 yoffset 20
    linear .1 yoffset -20
    linear .1 yoffset 0 

transform shake:
    linear .1 xoffset 5
    linear .1 xoffset -5
    repeat