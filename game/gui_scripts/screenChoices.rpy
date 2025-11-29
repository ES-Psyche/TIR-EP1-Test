init offset = -1

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

style choice_button is default:
    background "gui/choice_option_button_idle.png"
    hover_background "gui/choice_option_button_hover.png"
    xsize 800  ysize 120

screen choice(items):
    modal False

    fixed:
        at gui_fade_inout
#        add "gui_overlay"

        vbox:
            xsize 800
            xalign 0.5 yalign 0.4
            spacing 14

            for i in items:
                button:
                    #add "gui/choice_option_button.png" yoffset -15
                    text i.caption style "choice_button_text" align (.5,.6)
                    hovered Play("system",guisfx_button_hover)
                    action [Play("system",guisfx_button_click),
                            i.action]

                    style "choice_button"
                    at gui_buttonfade_enter(0.1)

style choice_button_text is default:
    font gui.adv_font_face
    size gui.adv_font_size * 0.85
    color "#bdb2a4"
    hover_color "#FBFFFF"
    kerning gui.advname_font_kerning * 0.5

    text_align 0.5
    bold False
