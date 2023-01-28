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
image money_icon = "icons/money.png"
define focus_location = ""
label start:
    $ quick_menu = False
    jump input_player_name
    # jump input_player_name
    # call start_time_variables
    # jump enter_map
    # call deactive_quick
    # jump age_check
    "testing"
return
