image picture_1 = im.Scale("bg cave.jpg", 1920, 1080)
image ball_blue = "icons/ball_blue.png"
image ball_white = "icons/ball_white.png"
image morning = "icons/morning.png"
image afternoon = "icons/afternoon.png"
image evening = "icons/evening.png"
image dawn = "icons/dawn.png"
image temp_bed = "coolbedroom"
define show_calendar = False
image button_hover = Frame ("gui/hover.png",40,40,40,40, tile=True)
image money_icon = "icons/hover.png"
define focus_location = ""


default player = Player("Almir", 0, 0)
default places = []
default location_object = Place(-1, "", 0, 0, False, False, 0, False, False, "" )


default places0 = Place( 0, "Martha Room", 700, 500, True, True, 0, False, True, "Martha Room" )
default places1 = Place( 1, "Your Room", 910, 410, True, True, 1, True, True, "Your Room" )
default places3 = Place( 3, "Agatha Room", 710, 820, False, True, 1, False, True, "Agatha Room" )
default places4 = Place( 4, "Mandy Room", 710, 820, False, True, 1, False, True, "Mandy Room" )
default places5 = Place( 5, "Bedroom 5", 710, 820, False, True, 1, False, True, "Bedroom 5" )
default places6 = Place( 6, "Living_room", 1200, 100, False, False, 1, False, True, "Living Room" )
default places7 = Place( 7, "Laundry Room", 1200, 100, False, False, 1, False, True, "Laundry Room" )
default places8 = Place( 8, "Hallway", 1200, 100, False, False, 1, False, True, "Laundry Room" )
default places9 = Place( 9, "Bathroom", 1200, 100, False, False, 1, False, True, "Bathroom" )
default places10 = Place( 10, "Front Door", 1200, 100, False, False, 1, False, True, "Front Door" )
default places11 = Place( 11, "Licue Realm", 1200, 100, False, False, 1, False, True, "Licue Realm" )
default places12 = Place( 12, "Hospital Room", 1200, 100, False, False, 1, True, True, "Hospital Room" )

label start:
    camera:
        perspective True
    window auto hide
    $ quick_menu = False
    $ ui_show_top_screen = True
    $ ui_show_foward_time = False
    $ ui_show_time =  True
    $ ui_show_money = True
    $ ui_show_location = True
    $ ui_show_maps = True
    $ ui_can_change_map = False
    $ ui_can_inventory = False

    scene black with Dissolve(0.5)
    centered "This game contains content of adult nature and is not suited to audiences below the age of 18. If you are easily offended or are under the age of 18, close the game now."

    $ map_dissolve_black_default = 1
    $ map_dissolve_time_default = 1

    call age_check
    if _return == False:
        return

    jump input_player_name
return

transform sub_licue_suck:
        "bg/licue sub2.jpg"
        subpixel True 
        zoom 1.0 
        linear 0.41 zoom 1.06 
        linear 0.41 zoom 1.0
        repeat