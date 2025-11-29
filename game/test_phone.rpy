label test_phone_system:
    
    # Initialize phone
    call phone_start
    
    # Test incoming message
    call message("Unknown", "Hello? Is this working?")
    
    # Test outgoing message (me)
    call message("Me", "Yeah, I can see this.")
    
    # Test reply menu
    call reply_message("Who is this?")
    
    menu:
        "Who is this?":
            call message("Me", "Who is this?")
            call message("Unknown", "It's a test script, obviously.")
            
        "Wrong number.":
            call message("Me", "I think you have the wrong number.")
            call message("Unknown", "Oh, sorry about that.")

    # Test image message (using a placeholder or existing image)
    # Using 'phone.png' as a test image since we know it exists
    call message("Unknown", "Here is an image test.")
    call message_img("Unknown", "Check this out.", "images/phone.png")
    
    # End phone call
    call phone_end
    
    "Phone test complete."
    return
