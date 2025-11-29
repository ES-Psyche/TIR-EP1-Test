## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen settings(fromPause=False,fromMain=False):

    tag menu
    key "game_menu" action Return()

    python:
        xy = renpy.get_physical_size()

    if fromMain:
        add gui.slm_background

    fixed:
        if fromPause == False:
            at gui_fade_inout
        else:
            at gui_fade_out
        add "gui_overlay"

        use exit_button

        add "gui/log_decor_top.png" at gui_overlaydecor_top

        frame:
            background None
            xsize 1200
            at gui_overlaydecor_bottom

            add "gui/settings_decor_bottom.png":
                alpha 0.3

            text "{color=#F2F7FF}SETTINGS{/color}":
                style "gui_overlay_title"
        vbox:
            xsize 1200
            xalign 0.5 yalign 0.45
            spacing 60
            at gui_fade(1.0)

            hbox:
                xsize 1200 ysize 200

                grid 2 2:
                    xalign 0.0
                    spacing 10

                    text "{color=#F2F7FF}Display{/color}" style "settings_header"

                    null height 1

                    button:
                        style "settings_button"
                        at gui_buttonfade

                        hovered Play("system",guisfx_button_hover)
                        action [Play("system",guisfx_button_click),
                                Preference("display", "window")]

                        text "{color=#F2F7FF}WINDOWED{/color}" style "settings_button_text"

                    button:
                        style "settings_button"
                        at gui_buttonfade

                        hovered Play("system",guisfx_button_hover)
                        action [Play("system",guisfx_button_click),
                                Preference("display", "fullscreen")]

                        text "{color=#F2F7FF}FULLSCREEN{/color}" style "settings_button_text"

                grid 2 2:
                    xalign 0.0
                    spacing 10

                    text "{color=#F2F7FF}Skip{/color}" style "settings_header"

                    null height 1

                    button:
                        style "settings_button"
                        at gui_buttonfade

                        hovered Play("system",guisfx_button_hover)
                        action [Play("system",guisfx_button_click),
                                Preference("skip", "seen")]

                        text "{color=#F2F7FF}READ TEXT{/color}" style "settings_button_text"

                    button:
                        style "settings_button"
                        at gui_buttonfade

                        hovered Play("system",guisfx_button_hover)
                        action [Play("system",guisfx_button_click),
                                Preference("skip", "all")]

                        text  "{color=#F2F7FF}ALL TEXT{/color}" style "settings_button_text"

            vbox:
                xsize 1200 ysize 200
                yoffset -40
                spacing 40
                xalign .5

                vbox:
                    xsize 1200 ysize 70
                    xalign 0.5

                    text "{color=#F2F7FF}Text Speed{/color}" style "settings_header" xalign 0.5

                    hbox:
                        xsize 1200 xalign 0.5
                        spacing 13

                        text "{color=#F2F7FF}SLOW{/color}":
                            xsize 85 xalign 1.0
                            style "caption_med"
                            kerning gui.advname_font_kerning

                        bar:
                            hovered Play("system",guisfx_button_hover)
                            value Preference("text speed")
                            base_bar "gui/settings_text_bar.png"
                            thumb "gui/settings_text_thumb.png"

                            xsize 987 ysize 22
                            xalign 0.5 yoffset 3
                            at gui_buttonfade

                        text "{color=#F2F7FF}FAST{/color}":
                            xsize 85 xalign 0.0 xoffset 4
                            style "caption_med"
                            kerning gui.advname_font_kerning

                vbox:
                    xsize 1200
                    xalign 0.5 ysize 70
                    text "{color=#F2F7FF}Auto Forward Pause{/color}" style "settings_header" xalign 0.5

                    hbox:
                        xsize 1200 xalign 0.5
                        spacing 13

                        text "{color=#F2F7FF}SHORT{/color}":
                            xsize 85 xalign 1.0
                            style "caption_med"
                            kerning gui.advname_font_kerning

                        bar:
                            hovered Play("system",guisfx_button_hover)
                            value Preference("auto-forward time")
                            base_bar "gui/settings_text_bar.png"
                            thumb "gui/settings_text_thumb.png"

                            xsize 987 ysize 22
                            xalign 0.5 yoffset 3
                            at gui_buttonfade

                        text "{color=#F2F7FF}LONG{/color}":
                            xsize 85 xalign 0.0 xoffset 4
                            style "caption_med"
                            kerning gui.advname_font_kerning

            grid 2 2:
                xsize 1200 xfill True ysize 140
                spacing 30
                xalign .5

                hbox:
                    xsize 505 ysize 30
                    xalign 0.0

                    text "{color=#F2F7FF}Music{/color}" style "settings_header" xsize 150 ysize 30

                    bar:
                        hovered Play("system",guisfx_button_hover)
                        value Preference("music volume")
                        style "settings_bar_volume"
                        at gui_buttonfade

                hbox:
                    xsize 505 ysize 30
                    xalign 1.0

                    text "{color=#F2F7FF}System{/color}" style "settings_header" xsize 150 ysize 30

                    bar:
                        hovered Play("system",guisfx_button_hover)
                        value MixerValue("systemMixer")
                        style "settings_bar_volume"
                        at gui_buttonfade

                hbox:
                    xsize 505 ysize 30
                    xalign 0.0

                    text "{color=#F2F7FF}Sound{/color}" style "settings_header" xsize 150 ysize 30

                    bar:
                        hovered Play("system",guisfx_button_hover)
                        value Preference("sound volume")
                        style "settings_bar_volume"
                        at gui_buttonfade

                hbox:
                    xsize 505 ysize 30
                    xalign 1.0

                    if config.has_voice:
                        text "{color=#F2F7FF}Voice{/color}" style "settings_header" xsize 150 ysize 30

                        bar:
                            hovered Play("system",guisfx_button_hover)
                            value Preference("voice volume")
                            style "settings_bar_volume"
                            at gui_buttonfade
                    else:
                        null height 1


style settings_button:
    xalign 1.0
    xsize 360 ysize 80
    background "gui/settings_button_idle.png"
    hover_background "gui/settings_button_hover.png"
    selected_hover_background "gui/settings_button_hover.png"
    selected_idle_background "gui/settings_button_hover.png"

style settings_header:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.advname_font_color

style settings_button_text:
    font gui.adv_font_face
    size gui.adv_font_size * 0.8
    color gui.advname_font_color
    selected_hover_color gui.adv_font_color
    hover_color gui.adv_font_color
    align (.5,.6)
    kerning gui.advname_font_kerning
    bold True

style settings_bar_volume:
    xsize 346 ysize 15
    xalign 1.0 yalign 0.5
    left_bar "gui/settings_volume_full.png"
    right_bar "gui/settings_volume_empty.png"

