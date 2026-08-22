
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    style_prefix "main_menu"
    add "gui/main_menu/" + persistent.main_menu_background + ".webp"

    vbox:
        xalign 0.5
        yanchor 0.5 ypos 0.632
        spacing -20
        frame:
            background None
            xalign 0.5
            textbutton _("Start")  action Start()

        
        frame:
            background None
            xalign 0.5
            textbutton _("Load") action [ShowMenu("load"), SetVariable("menu_use", "load")]

        
        frame:
            background None
            xalign 0.5
            textbutton _("Settings") action [ShowMenu("preferences"), SetVariable("menu_use", "settings")]

        
        frame:
            background None
            xalign 0.5
            textbutton _("Gallery") action ShowMenu("gallery") # REPLACE WITH GALLERY LATER

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            #Help isn't necessary or relevant to mobile devices.
                
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

style main_menu_label_text:
    size 45
    selected_color "#fff" 
    idle_color "#997F6E"
    hover_color "#D0B29E"

    text_align 0.5

style main_menu_button_text:
    hover_color "#F8DFD5"
    idle_color "#5D3231"
    outlines [ (absolute(10), "#F8DFD5", absolute(0), absolute(0)) ]
    hover_outlines [ (absolute(10), "#5D3231", absolute(0), absolute(0)) ]
    bold True
    
