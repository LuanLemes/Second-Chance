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
            self.add_to_list()
        @property
        def avatar(self):
            icon = "locations/" + self.name.lower() + ".png"
            return(icon)
        def add_to_list(self):
            for place in places:
                if place.ID == self.ID:
                    return
            places.append(self)
    t = 0

