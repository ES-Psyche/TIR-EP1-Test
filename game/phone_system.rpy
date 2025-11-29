
################# phone code stars ###################

image phone = "images/phone.png"


# Picking up the phone
transform phone_pickup:
    xalign 0.9
    yalign 0.5 
    alpha 0  
    on show:
        linear 0.3 alpha 1  # Smooth fade-in

transform phone_hide:
    xalign 0.9
    yalign 0.5  
    alpha 1
    on show:
        linear 0.3 alpha 0  # Smooth fade-out

transform phone_message_bubble_tip:
    xoffset 10
    yoffset 30  # Move it lower below the text field

transform phone_message_bubble_tip2:
    xoffset 165
    yoffset 30  # Move it lower below the text field

transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0
        
transform incoming_message:
    yoffset 100
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message
        
        
#### labels to shortcut stuff so you dont need to copypaste stuff repeatedly! #####

label phone_start:
    window hide
    show phone at phone_pickup 
    with dissolve
    $ renpy.pause(0.3)
    return

label phone_msg:
    $ renpy.pause()
    hide screen phone_message
    $ renpy.pause(0.1)
    return
        
label phone_msg2:
    $ renpy.pause()
    hide screen phone_message2
    $ renpy.pause(0.1)
    return
        
label phone_msgi:
    $ renpy.pause()
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return


label phone_after_menu:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return    
    
label phone_end:
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    show phone at phone_hide
    $ renpy.pause(0.2)
    return

label message(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "me":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    return
    
label reply_message(what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message3(what)
    return

label message_img(who, what,img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message_image(who, what,img)
    return


label message_start(who, what):
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "me":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    return    


    

    
######### phone code ends here ##########