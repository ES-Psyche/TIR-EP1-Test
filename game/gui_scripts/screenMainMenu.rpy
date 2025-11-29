## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu


init python:
    import random
    mm_imgs = ["CBH","CDI"]
    mm_index = 0
    mm_img = mm_imgs[0]

    def mm_img_next():
        global mm_index
        rnd = mm_index
        while rnd == mm_index:
            rnd = random.randrange(len(mm_imgs))
        mm_index = rnd
        return mm_imgs[mm_index]

    

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    
    
    add gui.mm_background 

    add "gui/mm_title.png" xalign -0.050 ypos 100
    
    fixed:
        xsize 470 ysize 1080
        xalign 0.0 yalign 0.0

        add "gui/mm_overlay.png" xpos 0.0 ypos 0.5

        vbox:
            spacing 10
            xsize 470 yalign 0.5

            button:
                style "mm_button"
                at gui_buttonfade

                hovered [Play("system",guisfx_button_hover),
                        Show("qm_tooltip",ttcontent="{font=fonts/Autography.otf}{color=#F4FCFF}{/color}{/font}",ttxpos=90, ttypos=335)]
                unhovered Hide("qm_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("qm_tooltip"),
                        Start()]
                
                text _("{font=fonts/Neon-Medium.otf}{size=+5}Start{/font}") style "mm_button_text"
            

            button:
                style "mm_button"
                at gui_buttonfade

                hovered [Play("system",guisfx_button_hover),
                        Show("qm_tooltip",ttcontent="{font=fonts/Autography.otf}{size=-5}{color=#FBFFFF}{/color}{/font}{/size}",ttxpos=110,ttypos=450)]
                unhovered Hide("qm_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("qm_tooltip"),
                        ShowMenu('load',fromMain=True)]

                #add "gui/mm_load_idle.png" at mm_button_line
                text _("{font=fonts/Neon-Medium.otf}{size=+5}Load{/font}") style "mm_button_text"

            button:
                style "mm_button"
                at gui_buttonfade

                hovered [Play("system",guisfx_button_hover),
                        Show("qm_tooltip",ttcontent="{font=fonts/Autography.otf}{color=#FBFFFF}{/color}{/font}",ttxpos=75,ttypos=565)]
                unhovered Hide("qm_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("qm_tooltip"),
                        ShowMenu('settings',fromMain=True)]

                #add "gui/mm_settings_idle.png" at mm_button_line
                text _("{font=fonts/Neon-Medium.otf}{size=+5}Settings{/font}") style "mm_button_text"

            button:
                style "mm_button"
                at gui_buttonfade

                hovered [Play("system",guisfx_button_hover),
                        Show("qm_tooltip",ttcontent="{font=fonts/Autography.otf}{color=#FBFFFF}{/color}{/font}",ttxpos=80, ttypos=680)]
                unhovered Hide("qm_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("qm_tooltip"),
                        ShowMenu('credits',fromMain=False)]
                
                text _("{font=fonts/Neon-Medium.otf}{size=+5}Credits{/font}") style "mm_button_text"

            button:
                style "mm_button"
                at gui_buttonfade

                hovered [Play("system",guisfx_button_hover),
                        Show("qm_tooltip",ttcontent="{font=fonts/Autography.otf}{color=#FBFFFF}{/color}{/font}",ttxpos=80, ttypos=680)]
                unhovered Hide("qm_tooltip")
                action [Play("system",guisfx_button_click),
                        Hide("qm_tooltip"),
                        ShowMenu('extras',fromMain=False)]
                
                text _("{font=fonts/Neon-Medium.otf}{size=+5}Gallery{/font}") style "mm_button_text"

            button:
                style "mm_button"
                at gui_buttonfade

                hovered [Play("system",guisfx_button_hover),
                        Show("qm_tooltip",ttcontent="{font=fonts/Autography.otf}{color=#FBFFFF}{/color}{/font}",ttxpos=125,ttypos=790)]
                unhovered Hide("qm_tooltip")
                action [Play("system",guisfx_button_click),
                        Quit()]

                #add "gui/mm_quit_idle.png" at mm_button_line
                text _("{font=fonts/Neon-Medium.otf}{size=+5}Exit{/font}") style "mm_button_text"


    vbox:
        pos (1270, 982)
        spacing 35
        button:

            xsize 200 ysize 200
            xpos 0
            at gui_buttonfade

            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_warn), OpenURL(gui.developer_site)]

            add "gui/pat.png"
        #text "{font=fonts/Cinzel-Regular.ttf}Support US{/font}" style "mm_button_text" size 27 xpos 82

    vbox:
        pos (1575, 980)
        spacing 35
        button:

            xsize 200 ysize 100
            xpos 0
            at gui_buttonfade

            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_warn), OpenURL(gui.developer_site2)]

            add "gui/discord.png"
        #text "{font=fonts/Cinzel-Regular.ttf}Join Our Discord{/font}" style "mm_button_text" size 27 xpos 175 ypos -25


style mm_button:
    align (.5,.5)
    xsize 420  ysize 90
    background "gui/mm_button_idle.png"
    #hover_background "gui/mm_button_hover.png"

style mm_button_text:
    font gui.adv_font_face
    size gui.adv_font_size
    color "#bdb2a4"
    hover_color "#B30E08"
    bold False

    text_align 0.0
    xalign 0.5

transform mm_button_line:
    xalign 0.0 yoffset 10
