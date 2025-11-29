init -1 python:
    import time

    class Message:
        def __init__(self, sender, content, image=None, full_image=None, date_time=None):
            self.sender = sender # "Me" or Contact Name
            self.content = content
            self.image = image # Path to thumbnail/small image
            self.full_image = full_image # Path to full screen image
            self.date_time = date_time if date_time else "Now" # Placeholder for timestamp

    class Contact:
        def __init__(self, id, name, icon):
            self.id = id
            self.name = name
            self.icon = icon
            self.history = [] # List of Message objects
            self.unread = False
            self.draft = "" # For future use if needed

        def add_message(self, sender, content, image=None, full_image=None, date_time=None):
            msg = Message(sender, content, image, full_image, date_time)
            self.history.append(msg)
            if sender != "Me":
                self.unread = True

        def mark_read(self):
            self.unread = False

        @property
        def last_message(self):
            if self.history:
                msg = self.history[-1]
                if msg.image:
                    return "[Image]"
                return msg.content
            return ""

    class Phone:
        def __init__(self):
            self.contacts = {} # id -> Contact object
            self.active_contact_id = None
            self.choices = [] # List of (text, label) tuples for the current choice menu

        def add_contact(self, id, name, icon):
            if id not in self.contacts:
                self.contacts[id] = Contact(id, name, icon)

        def get_contact(self, id):
            return self.contacts.get(id)

        def message(self, id, content, sender=None, delay=0, date_time=None):
            if id not in self.contacts:
                return
            
            contact = self.contacts[id]
            _sender = sender if sender else contact.name
            
            # If delay > 0, we could implement a "typing..." effect here in the future
            # For now, we just add it.
            contact.add_message(_sender, content, date_time=date_time)
            renpy.restart_interaction()

        def image_message(self, id, thumb, full, sender=None):
            if id not in self.contacts:
                return
            contact = self.contacts[id]
            _sender = sender if sender else contact.name
            contact.add_message(_sender, "", image=thumb, full_image=full)
            renpy.restart_interaction()

        def set_choices(self, items):
            # items is a list of tuples: [("Choice Text", "label_to_jump"), ...]
            self.choices = items
            renpy.restart_interaction()

        def clear_choices(self):
            self.choices = []
            renpy.restart_interaction()

    # Initialize the global phone object
    phone = Phone()

    def phone_msg(id, content, sender=None):
        phone.message(id, content, sender)

    def phone_img(id, thumb, full, sender=None):
        phone.image_message(id, thumb, full, sender)

    def phone_call(id):
        phone.active_contact_id = id
        renpy.show_screen("phone_conversation")
