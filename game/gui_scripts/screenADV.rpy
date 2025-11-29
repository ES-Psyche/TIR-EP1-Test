init offset = -1


## ADV screen ##################################################################

screen say(who, what):
    style_prefix "say"
    zorder 999

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                if varAdvNameUppercase == True:
                    text who.upper() id "who"
                else:
                    text who id "who"

        text what id "what" ypos 120


    use qm_button()

    ## Phone settings for side images. Not applicable, but kept for backwards
    ## compatibility.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ypos 1095
    ysize 278
    background Image("gui/adv_textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 298
    xanchor 0.0
    xsize 800
    ypos 60
    ysize 50

style say_label:
    font gui.advname_font_face
    size gui.advname_font_size
    color gui.advname_font_color
    kerning gui.advname_font_kerning

    xalign 0.0
    yalign 0.5

style say_dialogue:
    font gui.adv_font_face
    size gui.adv_font_size
    color gui.adv_font_color
    line_leading gui.adv_font_line

    xpos 300
    xsize 1190


define config.layers = [ 'black_background', 'master', 'transient', 'screens', 'overlay' ]

screen black_background:
    layer 'black_background'
    add Solid("#000",xysize=(config.screen_width,config.screen_height))


## ADV Quick Menu ##################################################################

screen qm_button():

    ## Shortcuts ###################################################################

    key "b" action ShowMenu('history')
    key "s" action ShowMenu('save')
    key "l" action ShowMenu('load')
    key "m" action MainMenu(confirm=True)

    ## Layout ######################################################################

    imagebutton auto "gui/qm_button_%s.png":
        align (1.0,1.01)
        hovered [Play("system",guisfx_button_hover),
                Show("qm_tooltip",ttcontent="MENU",ttxpos=1784,ttypos=866)]
        unhovered Hide("qm_tooltip")
        action [Play("system",guisfx_button_click),
                Hide("qm_tooltip"),
                ShowMenu('pause_menu')]
        at gui_buttonfade

style caption_small:
    font gui.adv_font_face
    size gui.adv_font_size * 0.45
    bold True
    color gui.adv_font_color
    kerning 2

style caption_med:
    font gui.adv_font_mm
    size gui.adv_font_size * .85
    bold False
    color gui.advname_font_color

image gui_indicator_skip:
    "gui/indicator_skip.png"
    alpha .8
    block:
        linear 0.7 alpha 0.0
        linear 0.7 alpha 1.0
        pause 0.2
        repeat

screen qm_tooltip(ttcontent,ttxpos,ttypos):
    zorder 9999
    text ttcontent:
        style "caption_med"
        xpos ttxpos ypos ttypos
        at gui_fade_inout(0.0,0.3)


## Indicators ######################################################################

screen indicator(_layer="top_layer"):

    zorder 100
    style_prefix "skip"

    if _rollback:
        if config.skipping == "slow" or config.skipping == "fast":
            add "gui_indicator_skip" xalign 0.5 yalign 0.5

init python:
    config.skip_indicator = None
    config.overlay_screens.append("indicator")

## Stats ###########################################################################
# for later


##Phone

screen phone_ui():
    # Add phone background
    add "rp1" xpos 1500 ypos 485  # Adjusted for 1920x1080 layout

    # Viewport for scrolling messages inside the phone screen
    viewport:
        xpos 1515  # Align within phone screen
        ypos 520   # Position inside the phone
        xsize 400  # Width inside phone UI
        ysize 310  # Adjust height to fit within phone
        draggable True
        mousewheel True

        vbox:
            spacing 10
            for msg in messages:
                if msg[2] == "left":  # NPC Messages
                    text msg[0] style "msg_left"
                else:  # Player Messages
                    text msg[0] style "msg_right"

    # Choice box for player response (appears after messages)
    if len(messages) % 2 == 1:  # Show choices only after NPC messages
        vbox:
            xpos 1520
            ypos 860
            xsize 390
            spacing 5
            textbutton "I'm good, you?" action [SetVariable("messages", messages + [("I'm good, you?", "You", "right")])]
            textbutton "Just tired, long day." action [SetVariable("messages", messages + [("Just tired, long day.", "You", "right")])]


## MISC #######


##################################################################
#screen pretitle(textmessage_title, textmessage_descr, labeljump):
    #modal True
    #vbox:
        #align (.5,.4)
        #spacing 80
        #text textmessage_title:
            #align (.5,.4)
            #size 180
            #color "#f3f3f3"
            #font gui.adv_font_face
        #text textmessage_descr:
            #align (.5,.4)
            #size 50
            #color "#f3f3f3"
            #font gui.adv_font_face
        #at trans_pretitle
    #timer 4.0 action [Hide("pretitle"), Jump(labeljump)]



#transform trans_pretitle:
    #on show:
        #alpha .0
        #zoom .8
        #parallel:
            #linear 3.0 alpha 1.0
        #parallel:
            #linear 5.0 zoom 1.0
    #on hide:
        #linear .5 alpha .0


screen support():
    tag credits
    hbox:
        align(.5,.84)
        imagebutton:
            auto "gui/patreon_banner_%s.png"
            action [Play("system",guisfx_button_warn), OpenURL(gui.developer_site)]
            at gui_buttonfade

screen credits(fromPause=False,fromMain=False):
    tag menu
    zorder 700
    key "game_menu" action Return()

    add Solid("000000")
    window: ## content
        at trans_credits
        xalign.5
        style "credits_window"
        vbox:
            xalign .5
            spacing 40
            vbox:
                xalign .5
                spacing 10
                text "{size=+5}{color=#FFC42E}Developers{/color}":
                    xalign .5
                    style "credits_header"
                text "{color=#F6F6F2}Psychedelic{/color}":
                    xalign .5
                    style "credits_content" 
                text "{color=#F6F6F2}Arisushi{/color}":
                    xalign .5
                    style "credits_content" 

            #vbox:
                #xalign .5
                #spacing 10
                #text "{size=-5}{color=#FFC42E}Former Team Members{/color}":
                    #xalign .5
                    #style "credits_header"
                #text "{size=+3}{color=#F6F6F2}Fappybeard{/color}":
                    #xalign .5
                #text "{color=#F6F6F2}Solcipher{/color}":
                    #xalign .5
                    #style "credits_content"    
            
            vbox:
                xalign .5
                spacing 10
                text "{color=#FFC42E}Patreon Supporters{/color}":
                    xalign .5
                    style "credits_header"

                text "{color=#FBFFFF}{i}{size=37}Rebelyon{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Fappybeard{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Dorn{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Rhuarc{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Manuel{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Winter{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Mos{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Wes{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Ben Donnelly{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Craig Rowley{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Devank{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Grog{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Groninc95{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Twisty Ninja{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Jill Valentine{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}Cocoabutter{/size}{/i}":
                    xalign .5
                text "{color=#FBFFFF}{i}{size=37}IDisagree{/size}{/i}":
                    xalign .5
                style "credits_content"
   

            vbox:
                xalign .5
                spacing 10
                text "{color=#FFC42E}Special Thanks To{/color}":
                    xalign .5
                    style "credits_header"
                text "{color=#FBFFFF}Evite Games, Deadpool, Darth Hiruma, Gery, Knight, Mr. Vargas, Hank Rockwell, The Naughty Captain, Wilson Wonka, Larry 2000, Dark Assassin, Puggy.{/color}":
                    xalign .5
                
                    style "credits_content"

            vbox:
                xalign .5
                spacing 10
                text "{color=#FFC42E}Proofreader{/color}":
                    xalign .5
                    style "credits_header"
                text "{color=#FBFFFF}Scooter{/color}":
                    xalign .5
                
                    style "credits_content"

            vbox:
                xalign .5
                spacing 10
                text "{color=#FFC42E}Engine{/color}":
                    xalign .5
                    style "credits_header"
                text "{color=#F6F6F2}Ren'Py by Tom \"PyTom\" Rothamel{/color}":
                    xalign .5
                    style "credits_content"
            #vbox:
                #xalign .5
                #spacing 10
                #text "{color=#FFC42E}Music{/color}":
                    #xalign .5
                    #style "credits_header"
                #text "{color=#F6F6F2}Left Alone By CO.AG Music{/color}":
                    #xalign .5
                    #style "credits_content"
                
            
    add "gui/overlay/credits.png"
    text "CREDITS":
        xalign .5 yalign .08
        size 70
        style "nvl_thought"
    use quick_menu(fromPause=False,fromMain=False)

screen quick_menu(fromPause=False,fromMain=False):
    zorder 900
    add "gui/nvl_qm.png":
        alpha 0.3
        xalign 0.5 ypos 1000

    hbox:
        xalign 0.5 ypos 977
        spacing 25

        if fromMain:
            textbutton "RETURN":
                hovered Play("system",guisfx_button_hover)
                action [Play("system",guisfx_button_click),
                        Return()]
                text_style "nvl_qm_button"
                at gui_buttonfade

        else:
            textbutton "MENU":
                hovered Play("system",guisfx_button_hover)
                action [Play("system",guisfx_button_click),
                        Return()]
                text_style "nvl_qm_button"
                at gui_buttonfade

        textbutton "LOAD":
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_click),
                    ShowMenu('load')]
            text_style "nvl_qm_button"
            at gui_buttonfade

        textbutton "QUIT":
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_click),
                    Quit()]
            text_style "nvl_qm_button"
            at gui_buttonfade


style window_message:
    text_align .5
    xalign .5
    xsize 1400

style credits_header:
    xsize 1400
    text_align 0.5
    size 40
    font gui.adv_font_face
    color "#bdb2a4"

style credits_content:
    xsize 1400
    text_align 0.5
    font gui.adv_font_face
    color "#5d5d5d"

style credits_window:
    background None
    xfill True
    yfill True
    xalign .5
    ypos 970
    ysize 770

transform trans_credits:
    yoffset 760
    linear 22.0 yoffset -1700
    yoffset 760
    repeat
