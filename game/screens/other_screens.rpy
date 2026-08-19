
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


screen about():



    add "gui/game_menu/background.png"
    tag menu


    use game_menu(_(""))
    add "gui/game_menu/label_history.png"

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "about"

        label "{color=#ff4400}[config.name!t]"
        text _("Version [config.version!t]\n")

        if gui.about:
            text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label_text:
    size 36


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():


    default device = "keyboard"

    add "gui/game_menu/background.png"
    tag menu


    use game_menu(_(""))
    add "gui/game_menu/label_help.png"

    viewport:
        xsize 1000 ysize 906
        yalign 1.0 xanchor 0.5 xpos 0.75
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "help"
        spacing 20

        hbox:
            xalign 0.5
            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
            textbutton _("Mouse") action SetScreenVariable("device", "mouse")

            if GamepadExists():
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help


screen keyboard_help():

    hbox:
        label _("{color=#ff4400}Enter")
        text _("{color=#000}Advances dialogue and activates the interface.")

    hbox:
        label _("{color=#ff4400}Space")
        text _("{color=#000}Advances dialogue without selecting choices.")

    hbox:
        label _("{color=#ff4400}Arrow Keys")
        text _("{color=#000}Navigate the interface.")

    hbox:
        label _("{color=#ff4400}Escape")
        text _("{color=#000}Accesses the game menu.")

    hbox:
        label _("{color=#ff4400}Ctrl")
        text _("{color=#000}Skips dialogue while held down.")

    hbox:
        label _("{color=#ff4400}Tab")
        text _("{color=#000}Toggles dialogue skipping.")

    hbox:
        label _("{color=#ff4400}Page Up")
        text _("{color=#000}Rolls back to earlier dialogue.")

    hbox:
        label _("{color=#ff4400}Page Down")
        text _("{color=#000}Rolls forward to later dialogue.")

    hbox:
        label "{color=#ff4400}H"
        text _("{color=#000}Hides the user interface.")

    hbox:
        label "{color=#ff4400}S"
        text _("{color=#000}Takes a screenshot.")

    hbox:
        label "{color=#ff4400}V"
        text _("{color=#000}Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "{color=#ff4400}Shift+A"
        text _("{color=#000}Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("{color=#ff4400}Left Click")
        text _("{color=#000}Advances dialogue and activates the interface.")

    hbox:
        label _("{color=#ff4400}Middle Click")
        text _("{color=#000}Hides the user interface.")

    hbox:
        label _("{color=#ff4400}Right Click")
        text _("{color=#000}Accesses the game menu.")

    hbox:
        label _("{color=#ff4400}Mouse Wheel Up\nClick Rollback Side")
        text _("{color=#000}Rolls back to earlier dialogue.")

    hbox:
        label _("{color=#ff4400}Mouse Wheel Down")
        text _("{color=#000}Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("{color=#ff4400}Right Trigger\nA/Bottom Button")
        text _("{color=#000}Advances dialogue and activates the interface.")

    hbox:
        label _("{color=#ff4400}Left Trigger\nLeft Shoulder")
        text _("{color=#000}Rolls back to earlier dialogue.")

    hbox:
        label _("{color=#ff4400}Right Shoulder")
        text _("{color=#000}Rolls forward to later dialogue.")


    hbox:
        label _("{color=#ff4400}D-Pad, Sticks")
        text _("{color=#000}Navigate the interface.")

    hbox:
        label _("{color=#ff4400}Start, Guide, B/Right Button")
        text _("{color=#000}Accesses the game menu.")

    hbox:
        label _("{color=#ff4400}Y/Top Button")
        text _("{color=#000}Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button:
    xmargin 12

style help_label:
    xsize 375
    right_padding 30

style help_text:
    xalign 1.0
    textalign 1.0
    yalign 0.5
    idle_color "#000"
    hover_color "#ff4400"
    selected_idle_color '#ff4400'
style help_label_text:
    is help_text
style help_button_text:
    is help_text
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


screen about():

    tag menu

    add "#21212db2" # The background; can be whatever

    use game_menu(_("About"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "about"

        label "[config.name!t]"
        text _("Version [config.version!t]\n")

        if gui.about:
            text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label_text:
    size 36


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("Help"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "help"
        spacing 23

        hbox:

            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
            textbutton _("Mouse") action SetScreenVariable("device", "mouse")

            if GamepadExists():
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button:
    xmargin 12

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    xalign 1.0
    textalign 1.0
