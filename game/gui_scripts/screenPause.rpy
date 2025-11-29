init offset = -1

screen pause_menu(fromPause=False):

    tag menu
    key "game_menu" action Return()

    fixed:
        if not fromPause:
            at gui_fade_inout
        else:
            at gui_fade_out

        add "gui_overlay"

        add "gui/log_decor_top.png" at gui_overlaydecor_top

        use exit_button

        frame:
            background None
            xsize 1200
            at gui_overlaydecor_bottom

            add "gui/pause_decor_bottom.png":
                alpha 0.3
            text "PAUSE MENU":
                style "gui_overlay_title"

        grid 3 2:
            spacing 50
            xalign 0.5
            yalign 0.5

            at gui_fade(.5)

            imagebutton:
                auto "gui/pause_log_%s.png"
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Log",ttxpos=0.322,ttypos=510)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("pause_tooltip"),
                        ShowMenu('history',fromPause=True)]

                xalign .5
                at gui_buttonfade

            imagebutton:
                auto "gui/pause_save_%s.png"
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Save",ttxpos=0.496,ttypos=510)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("pause_tooltip"),
                        ShowMenu('save',fromPause=True)]

                xalign .5
                at gui_buttonfade


            imagebutton:
                auto "gui/pause_load_%s.png"
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Load",ttxpos=0.673,ttypos=510)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("pause_tooltip"),
                        ShowMenu('load',fromPause=True)]

                xalign .5
                at gui_buttonfade

            imagebutton:
                auto "gui/pause_settings_%s.png"
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Settings",ttxpos=0.322,ttypos=846)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("pause_tooltip"),
                        ShowMenu('settings',fromPause=True)]

                xalign .5
                at gui_buttonfade

            imagebutton:
                auto "gui/pause_mainmenu_%s.png"
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Main Menu",ttxpos=0.496,ttypos=846)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_warn),
                        Hide("pause_tooltip"),
                        MainMenu(confirm=True)]

                xalign .5
                at gui_buttonfade

            imagebutton:
                auto "gui/pause_quit_%s.png"
                hovered [Play("system",guisfx_button_hover),
                        Show("pause_tooltip",ttcontent="Quit",ttxpos=0.673,ttypos=846)]
                unhovered Hide("pause_tooltip")
                action [Play("system",guisfx_button_warn),
                        Hide("pause_tooltip"),
                        Quit(confirm=True)]

                xalign .5
                at gui_buttonfade

screen pause_tooltip(ttcontent,ttxpos,ttypos):
    zorder 9999
    text ttcontent:
        style "caption_pause"
        xcenter ttxpos ycenter ttypos
        at gui_fade_inout(0.0,0.3)

style caption_pause:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.advname_font_color


