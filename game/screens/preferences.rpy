
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

default hint_flowers_showing = True
screen preferences():

    add "gui/game_menu/background.png"
    tag menu


    use game_menu(_(""))
    add "gui/game_menu/label_settings.png"

    frame:
        style_prefix 'game_menu'
        xsize 1000 ysize 906
        yalign 1.0 xanchor 0.5 xpos 0.6
        background None
        vbox:

            hbox:
                box_wrap False

                if renpy.variant("pc") or renpy.variant("web"):
                    # Only need fullscreen/windowed on desktop and web builds

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window"):
                            # Ensures this button is selected when
                            # not in fullscreen.
                            selected not preferences.fullscreen
                            action Preference("display", "window")
                        textbutton _("Fullscreen"):
                            action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text"):
                        action Preference("skip", "toggle")
                    textbutton _("After Choices"):
                        action Preference("after choices", "toggle")
                    textbutton _("Transitions"):
                        action InvertSelected(Preference("transitions", "toggle"))
                vbox:
                    
                    style_prefix "radio"
                    label _("Hints")
                    
                    textbutton _("On"):
                        action SetVariable("hint_flowers_showing", True)
                    textbutton _("Off"):
                        action SetVariable("hint_flowers_showing", False)
                        
            hbox:
                style_prefix "slider"
                box_wrap False

                vbox:

                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    style_prefix "radio"
                    label _("Font")
                    textbutton _("Default") action [gui.SetPreference("font", "gui/fonts/EBGaramond.ttf"),
                    gui.SetPreference("interface_font", "gui/fonts/EBGaramond.ttf"),  SetVariable("name_ypos", -0.5), gui.SetPreference("name_font", "gui/fonts/Morris.ttf")]
                    textbutton _("Atkinson Hyperlegible") action [gui.SetPreference("font", "gui/fonts/Atkinson.ttf"), SetVariable("name_ypos", -0.9125),
                    gui.SetPreference("interface_font", "gui/fonts/Atkinson.ttf"), gui.SetPreference("name_font", "gui/fonts/Atkinson.ttf")]
                
            

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            hbox:
                style_prefix "slider"
                box_wrap False
                vbox:

                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height 15
                        textbutton _("Mute All"):
                            style_prefix "check"
                            action Preference("all mute", "toggle")

### PREF
style pref_label:
    top_margin 15
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_button_text:
    idle_color '#A27C6F'
    hover_color '#D0633C'
    selected_idle_color '#000'


style pref_vbox:
    xsize 338

## RADIO
style radio_label:
    is pref_label

style radio_label_text:
    is pref_label_text
style radio_button_text:
    is pref_button_text

style radio_vbox:
    is pref_vbox
    spacing 0

style radio_button:
    foreground "gui/button/radio_[prefix_]foreground.png"
    padding (50, 0, 6 , 6)
## CHECK
style check_label:
    is pref_label
style check_label_text:
    is pref_label_text

style check_button_text:
    is pref_button_text
style check_vbox:
    is pref_vbox
    spacing 0

style check_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding (50, 0, 6, 6)

## SLIDER
style slider_label:
    is pref_label
style slider_label_text:
    is pref_label_text

style slider_slider:
    xsize 525
    thumb_offset 13

style slider_button:
    yalign 0.5
    left_margin 15

style slider_vbox:
    is pref_vbox
    xsize 675

style slider_button_text:
    is pref_button_text
