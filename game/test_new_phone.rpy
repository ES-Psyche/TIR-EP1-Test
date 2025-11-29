label test_new_phone:
    # Setup contacts
    $ phone.add_contact("rose", "Rose", None) # None = Placeholder icon
    $ phone.add_contact("unknown", "Unknown", None)

    # Add some history
    $ phone.message("rose", "Hey! How are you?", date_time="10:00 AM")
    $ phone.message("rose", "Are we still on for tonight?", date_time="10:05 AM")

    # Open phone home screen
    "Opening phone..."
    show screen phone_home
    "You can click on 'Rose' to see the conversation."
    
    # Simulate receiving a message while phone is open
    $ phone.message("rose", "Hello??", date_time="Now")
    "Received a new message from Rose."

    # Simulate a choice
    "Jumping to choice test..."
    jump phone_choice_test

label phone_choice_test:
    # Ensure we are in the conversation
    $ phone.active_contact_id = "rose"
    show screen phone_conversation
    
    $ phone.message("rose", "Well?", date_time="Now")
    
    $ phone.set_choices([
        ("I'm coming.", "choice_coming"),
        ("I can't make it.", "choice_cant")
    ])
    
    "Waiting for choice..."
    pause

label choice_coming:
    $ phone.message("rose", "I'm coming.", sender="Me")
    $ phone.message("rose", "Great! See you soon.")
    jump phone_image_test

label choice_cant:
    $ phone.message("rose", "I can't make it.", sender="Me")
    $ phone.message("rose", "Oh... that's too bad.")
    jump phone_image_test

label phone_image_test:
    "Testing image message..."
    # Using existing assets for test
    $ phone.image_message("rose", "images/phone.png", "images/phone.png")
    "You should see an image now. Click it to view full screen."
    
    "End of test."
    return
