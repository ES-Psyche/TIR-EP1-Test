# New Phone System UI

# Styles
style phone_frame:
    background Solid("#000000")
    xsize 400
    ysize 800
    align (0.5, 0.5)

style phone_header:
    background Solid("#000000")
    ysize 80
    xfill True

style phone_header_text:
    color "#FFFFFF"
    size 28
    bold True
    align (0.0, 0.5)
    xoffset 20

style contact_button:
    background Solid("#000000")
    hover_background Solid("#1C1C1E")
    xfill True
    ysize 90
    ypadding 10
    xpadding 10

style contact_name:
    color "#FFFFFF"
    size 22
    bold True
    xalign 0.0

style contact_last_msg:
    color "#8E8E93"
    size 16
    xalign 0.0

style message_bubble_me:
    background Solid("#007AFF")
    padding (15, 10)
    xalign 1.0
    xmaximum 280

style message_bubble_them:
    background Solid("#2C2C2E")
    padding (15, 10)
    xalign 0.0
    xmaximum 280

style message_text_me:
    color "#FFFFFF"
    size 18

style message_text_them:
    color "#FFFFFF"
    size 18

style timestamp_text:
    color "#8E8E93"
    size 12
    xalign 0.5

# Screens

screen phone_home():
    modal True
    tag phone
    
    frame:
        style "phone_frame"
        
        vbox:
            # Header
            frame:
                style "phone_header"
                hbox:
                    align (0.0, 0.5)
                    text "Messages" style "phone_header_text"
                
                hbox:
                    align (1.0, 0.5)
                    spacing 20
                    xoffset -20
                    text "..." color "#007AFF" size 30 bold True
                    text "New" color "#007AFF" size 18 bold True yalign 0.5

            # Contact List
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                
                vbox:
                    for id, contact in phone.contacts.items():
                        button:
                            style "contact_button"
                            action [SetField(phone, "active_contact_id", id), Show("phone_conversation")]
                            
                            hbox:
                                spacing 15
                                # Unread Indicator
                                if contact.unread:
                                    add Solid("#0A84FF", size=(10, 10)) yalign 0.5
                                else:
                                    null width 10
                                
                                # Icon (Placeholder if None)
                                if contact.icon:
                                    add contact.icon size (60, 60)
                                else:
                                    add Solid("#3A3A3C", size=(60, 60))
                                
                                vbox:
                                    yalign 0.5
                                    text contact.name style "contact_name"
                                    text contact.last_message style "contact_last_msg"

            # Close Button (Bottom)
            textbutton "Close":
                xalign 0.5
                yalign 1.0
                text_color "#007AFF"
                action Hide("phone_home")

screen phone_conversation():
    modal True
    tag phone
    
    default current_contact = phone.get_contact(phone.active_contact_id)
    
    if current_contact:
        frame:
            style "phone_frame"
            
            vbox:
                # Header with Back Button
                frame:
                    style "phone_header"
                    hbox:
                        xfill True
                        yalign 0.5
                        textbutton "<" action [SetField(current_contact, "unread", False), Show("phone_home")] text_color "#007AFF" text_size 30 xoffset 10
                        
                        vbox:
                            xalign 0.5
                            if current_contact.icon:
                                add current_contact.icon size (40, 40) xalign 0.5
                            else:
                                add Solid("#3A3A3C", size=(40, 40)) xalign 0.5
                            text current_contact.name color "#FFFFFF" size 16 xalign 0.5
                        
                        null width 50 # Spacer for balance

                # Message History
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    yinitial 1.0 # Scroll to bottom
                    
                    vbox:
                        spacing 10
                        xfill True
                        first_spacing 20
                        
                        for msg in current_contact.history:
                            # Timestamp (Optional: Show only if time changed)
                            if msg.date_time:
                                text msg.date_time style "timestamp_text"
                            
                            if msg.sender == "Me":
                                hbox:
                                    xalign 1.0
                                    if msg.image:
                                        imagebutton:
                                            idle Transform(msg.image, size=(150, 150))
                                            action Show("phone_image_view", img=msg.full_image)
                                    else:
                                        frame:
                                            style "message_bubble_me"
                                            text msg.content style "message_text_me"
                            else:
                                hbox:
                                    xalign 0.0
                                    # Optional: Small avatar next to message
                                    if msg.image:
                                        imagebutton:
                                            idle Transform(msg.image, size=(150, 150))
                                            action Show("phone_image_view", img=msg.full_image)
                                    else:
                                        frame:
                                            style "message_bubble_them"
                                            text msg.content style "message_text_them"

                # Choice Menu (if active)
                if phone.choices:
                    vbox:
                        style_prefix "choice"
                        spacing 10
                        yalign 1.0
                        for i in phone.choices:
                            textbutton i[0]:
                                action [Function(phone.clear_choices), Jump(i[1])]
                                xfill True
                                background Solid("#1C1C1E")
                                hover_background Solid("#2C2C2E")
                                text_color "#0A84FF"
                                text_align 0.5

screen phone_image_view(img):
    modal True
    zorder 100
    
    add Solid("#000000") alpha 0.9
    
    add img align (0.5, 0.5)
    
    textbutton "Close":
        align (0.9, 0.1)
        text_color "#FFFFFF"
        text_size 30
        action Hide("phone_image_view")

