from pynput import keyboard

def on_press(key):
    return_value = ''
    try:
        match key:
            case keyboard.Key.esc:
                return_value = 'Esc'
            case keyboard.Key.home:
                return_value = 'Home'
            case keyboard.Key.end:
                return_value = 'End'
            case keyboard.Key.page_up:
                return_value = 'PgUp'
            case keyboard.Key.page_down:
                return_value = 'PgDn'
            case keyboard.Key.f1:
                return_value = 'F1'
            case keyboard.Key.f2:
                return_value = 'F2'
            case keyboard.Key.f3:
                return_value = 'F3'
            case keyboard.Key.f4:
                return_value = 'F4'
            case keyboard.Key.f5:
                return_value = 'F5'
            case keyboard.Key.f6:
                return_value = 'F6'
            case keyboard.Key.f7:
                return_value = 'F7'
            case keyboard.Key.f8:
                return_value = 'F8'
            case keyboard.Key.f9:
                return_value = 'F9'
            case keyboard.Key.f10:
                return_value = 'F10'
            case keyboard.Key.f11:
                return_value = 'F11'
            case keyboard.Key.f12:
                return_value = 'F12'
            case keyboard.Key.up:
                return_value = 'Up'
            case keyboard.Key.down:
                return_value = 'Down'
            case keyboard.Key.right:
                return_value = 'Right'
            case keyboard.Key.left:
                return_value = 'Left'
            case default:
                ...
    except AttributeError:
        pass
    return return_value

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()