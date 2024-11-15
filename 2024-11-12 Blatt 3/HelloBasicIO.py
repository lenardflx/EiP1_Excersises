from jguvc_eip import basic_io as bio

if __name__ == "__main__":
    bio.start()

    # Größenangaben
    text_size = (110, 16)  # Geschätzt
    screen_size = (640, 240)  # Geschätzt
    center = (  # Bildschirmmitte (Abzüglich der Textgröße, da Position des Textes die obere linke Ecke ist)
        (screen_size[0] - text_size[0]) // 2,
        (screen_size[1] - text_size[1]) // 2
    )
    padding = 10  # Zusätzlicher Abstand um den Text

    # Text zeichnen und umrahmen
    bio.draw_text(center[0], center[1], "Hello World")
    bio.draw_rectangle(center[0] - padding,
                       center[1] - padding,
                       text_size[0] + 2 * padding,
                       text_size[1] + 2 * padding,
                       border_color=(255, 0, 0), border_thickness=2, fill_color=None)

    bio.wait_close()
