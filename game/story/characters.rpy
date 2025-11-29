
#Characters

define mc = Character("[mcp]",who_color = "#FFC42E")
define mcn = Character("[mcp]", who_color="#FFC42E",what_size = 35, what_color="#FBFFFF",what_font="fonts/Elegant Lux Pro Mager.ttf", what_italic=True)


define n = Character("", who_color="#f3f3f3", what_color="#d2c4b4", what_italic=True)


define id = Character("BRAIN", who_color="#F72119",who_size = 35, who_font="fonts/ArtOfCreation_Regular.ttf", what_color="#F9FAFD", what_font="fonts/RetroSignature.otf", what_size = 85)

define ir = Character(_('Irene'),who_color="#db38be", who_font="fonts/Cinzel-Regular.ttf")

define UV = Character(_('Unknown Voice'),who_color="#F3E4DC")
define UVr = Character(_('Unknown Voice'),who_font="fonts/you.ttf",who_color="#F3E4DC",what_size = 35,what_color="#B30E08",what_font="fonts/TomatoGrotesk-Regular.otf")

define jn = Character(_('John'),who_color="#44E3FF")

define wl = Character(_('Will'),who_color="#44E3FF")

define fk = Character(_('Frank'),who_color="#44E3FF")

define dad = Character(_('Dad'),who_color="#44E3FF")

define sr = Character(_('Sarah'),who_color="#21F8F6")

define mar = Character(('Marilyn'),who_color="#F2B7C1")

define rs = Character(_('Rose'),who_color="#E4345A")

define joe = Character(_('Joe'),who_color="#44E3FF")

define lil = Character(_('Lilith'),who_color="#db38ba")

define rl = Character(('Riley'),who_color="#FF6044")

define ry = Character(_('Ryan'),who_color="#8d6ffc")

define tv = Character(_('TV'),who_color="#F3E4DC")

define nm = Character(_('Norman'),who_color="#B026FF")

define hk = Character(_('Hank'),who_color="#8644ff")



define anne = Character(('Anne'),who_color="#F2B7C1")

define uv2 = Character(_('Unknown Person'),who_color="#b30000")

define vn = Character(_('Vincent'),who_color="#b30000")
define nc = Character(_('Nico'),who_color="#b30000")

define uv3 = Character(_(''),who_color="#b30000")

define uv4 = Character(_('Unknown Person'),who_color="#b35310")

define uvg = Character(_('Unknown Person'),who_color="#00ffc3")

define amb = Character(_('Amber'),who_color="#b30000")

define lk = Character(_('Locke'),who_color="#8644ff")
define rt = Character(_('Rusty'),who_color="#8644ff")
define tn = Character(_('Tony'),who_color="#294bf9")

define gd = Character(_('Gordon'),who_color="#8644ff")

define fr = Character(_('Forelli'),who_color="#8644ff")

define dm = Character(_('Dmitry'),who_color="#8644ff")

define hel = Character(_('Helena'),who_color="#EA00FF")
define irs = Character(_('Iris'),who_color="#EF00FF")

define uv1 = Character(_('Unknown Person'),who_color="#8644ff")
define sec = Character(_('Secretary'),who_color="#8644ff")
define ja = Character(_('Jane'),who_color="#EA00FF")

define hal = Character(_('HAL'),who_color="#8644ff")

define e1 = Character(_('Employee 1'),who_color="#FF6EFF")
define e2 = Character(_('Employee 2'),who_color="#FF9900")
define cap = Character(_('Captain'),who_color="#FF6EFF")
define myr = Character(_('Mayor'),who_color="#609afe")


## Test Chars

define fb = Character(None, what_style="centered_text", window_style="centered_window", window_xfill=True, window_yfill=True, window_background="black", what_font="fonts/FMBolyarOrnatePro-100.ttf", what_size=56,what_color="#ddd", what_yalign=-2.5, what_xalign=0.5)
define fbt = Character(None, what_style="centered_text", window_style="centered_window", window_xfill=True, window_yfill=True, window_background="black", what_font="fonts/Elegant Lux Pro Mager.ttf", what_size=40,what_color="#ddd", what_yalign=-1.75, what_xalign=0.5)
define fbdisc = Character(None, what_style="centered_text", window_style="centered_window", window_xfill=True, window_yfill=True, window_background="black", what_font="fonts/Elegant Lux Pro Mager.ttf", what_size=45,what_color="#ddd", what_yalign=-1.7, what_xalign=0.5)


define fbs = Character(
    None, 
    what_style="centered_text", 
    window_style="centered_window", 
    window_xfill=True, 
    window_yfill=True, 
    window_background="black", 
    what_font="fonts/FMBolyarOrnatePro-100.ttf", 
    what_size=56, 
    what_color="#ddd", 
    #what_xalign=0.5,  # Centers text horizontally
    what_yalign=-2.0   # Centers text vertically
)



# Default name for MC
init python:

    def setReplay():
        global mc
        global mcp
        if persistent.mc:
            mc = persistent.mc
        else:
            mc = "Max"

style centered_text:
    xalign 0.5
    yalign 0.5