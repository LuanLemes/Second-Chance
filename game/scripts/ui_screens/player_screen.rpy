screen player_screen:
    zorder 3
    frame:
        xsize 1920
        ysize 1080
        background Solid("#000000ff") 
        vbox:
            text "Courage = [courage]"
            text "Knowledge = [knowledge]"
            text "Understanding = [understanding]"
            text "Carism = [carism]"
        textbutton "X":
            action Hide("player_screen")
            xalign 0.9
            