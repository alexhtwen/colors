import keyboard

def on_key_event(event):
    if event.name == 'esc':
        print("Esc key pressed")
    elif event.name == 'home':
        print("Home key pressed")
    elif event.name == 'end':
        print("End key pressed")
    elif event.name == 'page up':
        print("Page Up key pressed")
    elif event.name == 'page down':
        print("Page Down key pressed")
    elif event.name == 'f1':
        print("F1 key pressed")
    elif event.name == 'f2':
        print("F2 key pressed")

keyboard.hook(on_key_event)

try:
    print("Press a key (Esc to stop):")
    keyboard.wait('esc')
finally:
    print("Exiting")
