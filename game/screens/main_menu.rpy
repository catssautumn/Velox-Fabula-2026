
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
image main_menu_background = HBox(
    Solid("#292835", xsize=350),
    Solid("#21212d")
)

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    style_prefix "main_menu"
    add "main_menu_background"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 6
        frame:
            background None
            xalign 0.5
            textbutton _("Start")  action Start()

        
        frame:
            background None
            xalign 0.5
            textbutton _("Load") action ShowMenu("load")

        
        frame:
            background None
            xalign 0.5
            textbutton _("Preferences") action ShowMenu("preferences")

        
        frame:
            background None
            xalign 0.5
            textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
                
            frame:
                background None
                xalign 0.5
                textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
                
            frame:
                background None
                xalign 0.5
                textbutton _("Quit") action Quit(confirm=not main_menu)
# IF ITS STUPID AND IT WORKS ITS NOT STUPID #WORKDUMBERNOTHARDER

style game_menu_label_text:
    size 45
    selected_color "#fff" 
    idle_color "#997F6E"
    hover_color "#D0B29E"

    text_align 0.5
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
image main_menu_background = HBox(
    Solid("#292835", xsize=350),
    Solid("#21212d")
)

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_background"

    vbox:
        xpos 60
        yalign 0.5
        spacing 6

        textbutton _("Start") action Start()

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

