
## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

define config.history_length = 250

screen history():

    add "gui/game_menu/background.png"
    tag menu


    use game_menu(_(""))
    add "gui/game_menu/label_history.png"

    ## Avoid predicting this screen, as it can be very large.
    predict False


    use game_menu(_(""))
    frame:
        xsize 965 ysize 872
        xanchor 0.5 xpos 0.6
        yalign 0.7
        background None
        viewport:
            
            xysize (970, 872)
            xanchor 0.5 xpos 0.5
            yalign 1.0

            #style_prefix 'game_menu'
            mousewheel True draggable True pagekeys True
            scrollbars "vertical" 


            has vbox
            style_prefix "history"

            
            if not _history_list:
                label _("The dialogue history is empty.")
            else:
                for h in _history_list:
                    frame:
                        has vbox
                        if h.who:
                            label h.who style 'history_name':
                                substitute False
                                ## Take the color of the who text
                                ## from the Character, if set
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]
                                xsize 200   # this number and the null width
                                            # number should be the same
                        else:
                            null width 200

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False



## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_frame:
    xalign 0.0
    xminimum 100
    xmaximum 900
    yminimum 100
    background None
style history_hbox:
    spacing 20

style history_vbox:
    spacing 10

style history_name:
    xalign 0.0

style history_name_text:
    textalign 0.0
    align (1.0, 0.0)
    color '#5D3231'
    size 46

style history_text:
    textalign 0.0
    color "#000"
    size 32

style history_label:
    xfill False
style history_label_text:
    xalign 0.0
