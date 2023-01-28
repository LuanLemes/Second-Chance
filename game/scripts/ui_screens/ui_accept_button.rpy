screen example_button:
    frame:
        background Solid("0000")
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        # text "this is in the middle" xalign 0.5  yalign 0.5
        imagebutton:
            hover im.Scale("gui/idle.png", 300, 70)
            idle im.Scale("gui/hover.png", 300, 70)
            action NullAction()
            xalign 0.5  yalign 0.5
        textbutton "test" xalign 0.5  yalign 0.5 action NullAction()
