from jguvc_eip import basic_io as bio

if __name__ == "__main__":
    bio.start()

    # Größenangaben
    text_size = (110, 16) # Händisch gemessen
    screen_size = (640, 240) # Geschätzt
    center_size = ( # Bildschirmmitte
            (screen_size[0] - text_size[0]) // 2,
            (screen_size[1] - text_size[1]) // 2
        )

    # Schreiben des Textes
    bio.draw_text(center_size[0], center_size[1], "Hello World")

    # Rahmen um den Text
    padding = 10 # Abstand um den Text
    bio.draw_rectangle(center_size[0] - padding,
                       center_size[1] - padding,
                       text_size[0] + 2 * padding,
                       text_size[1] + 2 * padding,
                       border_color=(255,0,0), border_thickness=2, fill_color=None)

    bio.wait_close()
