style mytextbutton:
    color "#f00"
    hover_color "#ff0"

screen magister_store():
    # modal False
    # add background Solid("0000")

    vbox:
        for item in player_inventory.items:
            textbutton "[item.name]":
                text_style "mytextbutton"
                action NullAction()
