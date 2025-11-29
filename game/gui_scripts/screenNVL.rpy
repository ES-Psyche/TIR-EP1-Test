## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    key "b" action ShowMenu('history')
    #key "mousedown_4" action ShowMenu('history')
    key "s" action ShowMenu('save')
    key "l" action ShowMenu('load')
    key "m" action MainMenu(confirm=True)

    window:
        yalign .14
        style "ending_window"

        has vbox:
            spacing 30

        use credits_dialogue(dialogue)

screen credits_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit None is None
                text d.what:
                    xalign .5
                    id d.what_id
                    style "nvl_thought"


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit None is None

                if d.who is not None:

                    if varAdvNameUppercase == True:
                        text d.who.upper() + ".  ":
                            id d.who_id

                    else:
                        text d.who:
                            id d.who_id

                if d.who is None:
                    text d.what:
                        id d.what_id
                        style "nvl_thought"

                else:
                    text d.what:
                        id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 8

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_window:
    xfill True
    yfill True
    text_align .5
    background "gui_overlay"

style ending_window:
    xfill True
    yfill True
    xalign .5
    top_margin 0
    bottom_margin 0
    left_margin 0
    right_margin 0

style nvl_entry:
    xfill True
    ysize None

style nvl_label:
    ypos 1
    text_align .5

style nvl_dialogue:
    xsize 1400
    text_align 0.5
    color "#bdb2a4"

style nvl_thought:
    xsize 1400
    text_align 0.5
    color "#bdb2a4"

style nvl_qm_button:
    font gui.advname_font_face
    size gui.advname_font_size * 0.8
    color gui.advname_font_color
    kerning gui.advname_font_kerning

    text_align 0.5
    xalign 0.5
