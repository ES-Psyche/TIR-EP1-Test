init offset = -2

transform subtle4:
    easein 15 zoom 1.060
    easeout 5 zoom 1.010
    pause 2.5
    repeat
    
transform deathly:
    xalign 0.5 zoom 1 blur 0 alpha 1
    easein 2.5 zoom 1.05 blur 10 alpha 0.9
    easeout 2.5 zoom 1 blur 20 alpha 0.8
    easein 2.5 zoom 1.05 blur 30 alpha 0.7
    easeout 2.5 zoom 1 blur 40 alpha 0.6
    easein 2.5 zoom 1.05 blur 50 alpha 0.5
    easeout 2.5 zoom 1 blur 60 alpha 0.4
    easein 2.5 zoom 1 blur 70 alpha 0.3
    easeout 2.5 zoom 1.05 blur 80 alpha 0.3
    easein 2.5 zoom 1 blur 90 alpha 0.3
    block:
        easeout 2.5 zoom 1.05 blur 95 alpha 0.2
        easein 2.5 zoom 1 blur 90 alpha 0.3
        repeat

transform fade_in_new:
    subpixel True
    alpha 0.0
    parallel:
        easein 0.5 alpha 1.0

transform eject_pulse:
    alpha 1.0
    easeout_circ 0.4 alpha 0.0
    easein_circ 0.4 alpha 1.0
    repeat



transform blurry:
    xalign 0.5 zoom 1 blur 0 alpha 1
    linear 0.5 blur 0
    linear 0.1 blur 10
    linear 0.1 blur 20
    linear 0.1 blur 30
    linear 0.1 blur 40
    linear 0.25 blur 50
    linear 0.1 blur 40
    linear 0.1 blur 30
    linear 0.1 blur 20
    linear 0.1 blur 10
    linear 0.2 blur 0

transform alpha(alpha_value=0):
    alpha alpha_value

transform gui_buttonfade(beginalpha=.6):
    alpha beginalpha
    on idle:
        linear 0.15 alpha beginalpha
    on selected_idle:
        linear 0.15 alpha 1.0
    on hover:
        linear 0.15 alpha 1.0
    on selected_hover:
        linear 0.15 alpha 1.0

transform gui_buttonfade_enter(delaytimer=0.0,duration=0.5,beginalpha=0.8):
    alpha 0.0
    pause delaytimer
    linear duration alpha beginalpha
    on idle:
        linear 0.15 alpha beginalpha
    on hover:
        linear 0.15 alpha 1.0

transform gui_saveempty(beginalpha=0.3):
    linear 0.3 alpha beginalpha
    on idle:
        linear 0.3 alpha beginalpha
    on selected_idle:
        linear 0.3 alpha beginalpha
    on hover:
        linear 0.3 alpha 1.0
    on selected_hover:
        linear 0.3 alpha 1.0

transform gui_savefull:
    on idle:
        linear 0.3 alpha 1.0
    on selected_idle:
        linear 0.3 alpha 1.0
    on hover:
        linear 0.3 alpha 0.5
    on selected_hover:
        linear 0.3 alpha 0.5

transform gui_savedelete(beginalpha=0.3):
    on idle:
        linear 0.3 alpha beginalpha
    on selected_idle:
        linear 0.3 alpha beginalpha
    on hover:
        linear 0.3 alpha 1.0
    on selected_hover:
        linear 0.3 alpha 1.0

transform gui_cgbutton:
    alpha 1.0
    on idle:
        linear 0.3 alpha 1.0
    on hover:
        linear 0.3 alpha 0.3

transform gui_cgview:
    alpha 1.0 size(1920,1080)
    xalign 0.5 yalign 0.5

transform gui_fade(delaytimer=0.0, duration=0.5,beginalpha=1.0):
    alpha 0.0
    pause delaytimer
    linear duration alpha beginalpha

transform gui_fade_inout(delaytimer=0.0, duration=0.3):
    alpha 0.0
    pause delaytimer
    linear duration alpha 1.0
    on hide:
        linear duration alpha 0.0

transform gui_fade_inout_gui_large(delaytimer=0.0, duration=0.3):
    zoom 1.2
    align (.5,.4)
    alpha 0.0
    pause delaytimer
    linear duration alpha 1.0
    on hide:
        linear duration alpha 0.0

transform gui_fade_out(duration=0.5):
    alpha 1.0
    on hide:
        linear duration alpha 0.0

###########
# OVERLAY #
###########

image gui_overlay:
    "gui/choice_overlay.png"
    alpha gui.overlay_opacity

transform gui_overlaydecor_top:
    alpha 0.0
    xalign 0.5 ypos 104
    xoffset -200 yoffset 400
    parallel:
        linear 0.15 alpha 0.3
    parallel:
        easein 0.15 xoffset 0
    pause 0.2
    easein 0.5 yoffset 0

transform gui_overlaydecor_bottom:
    alpha 0.0
    xalign 0.5 ypos 967
    xoffset 200 yoffset -400
    parallel:
        linear 0.15 alpha 1.0
    parallel:
        easein 0.15 xoffset 0
    pause 0.2
    easein 0.5 yoffset 0

define gui_exit_xpos = 1830
define gui_exit_ypos = 25
define gui_exit_parameters = 0.8
