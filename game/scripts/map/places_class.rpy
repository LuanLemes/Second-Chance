init python:

    class Place(object):
        def __init__(self, ID, name, x, y, is_active, is_inside, map_to_show, can_foward_time, can_map, show_name):
            self.ID = ID
            self.is_active = is_active
            self.name = name
            self.x = x
            self.y = y
            self.is_inside = is_inside
            self.map_to_show = map_to_show
            self.can_foward_time = can_foward_time
            self.can_map = can_map
            self.show_name = show_name
        @property
        def avatar(self):
            icon = "locations/" + self.name.lower() + ".png"
            return(icon)

    places = []
    t = 0
    while t < 500:
        t += 1
        places.append(Place(-1, "", 0, 0, False, False, 0, False, False, ""))

    places[0] = Place( 0, "Bedroom 1", 700, 500, True, True, 0, False, True, "Bedroom 1" )
    places[1] = Place( 1, "Bedroom 2", 910, 410, True, True, 1, True, True, "Bedroom 2" )
    places[3] = Place( 3, "Bedroom 3", 710, 820, False, True, 1, False, True, "Bedroom 3" )
    places[4] = Place( 4, "Bedroom 4", 710, 820, False, True, 1, False, True, "Bedroom 4" )
    places[5] = Place( 5, "Bedroom 5", 710, 820, False, True, 1, False, True, "Bedroom 5" )
    places[6] = Place( 6, "Living_room", 1200, 100, False, False, 1, False, True, "Living Room" )
    places[7] = Place( 7, "Laundry Room", 1200, 100, False, False, 1, False, True, "Laundry Room" )
    places[7] = Place( 7, "Hallway", 1200, 100, False, False, 1, False, True, "Laundry Room" )



    location_object = Place(-1, "", 0, 0, False, False, 0, False, False, "" )
