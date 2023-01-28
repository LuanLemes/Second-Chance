init python:
    class Calendar(object):
        def __init__(self, current_day, week_days, day_time, current_week_day, current_day_time):
            xxx = 0
            self.week_days = week_days
            self.day_time = day_time
            self.current_week_day = current_week_day
            self.current_day_time = current_day_time
            self.current_day = current_day
        @property
        def output(self):
            return   self.week_days[self.current_week_day] + " " + self.day_time[self.current_day_time] + " day " + str(self.current_day)

        def add_current_day(self, days):
            self.current_day += days
            self.current_day_time = 0
            if self.current_week_day == 6:
                self.current_week_day = 0
            else:
                self.current_week_day += 1

        def add_current_day_time(self, times):
            if self.current_day_time == 4:
                self.add_current_day(1)
                return
            self.current_day_time +=1

    class Event(object):
        def __init__(self, week_day, day_time, day, block, is_active):
            self.week_day = week_day
            self.day_time = day_time
            self.day = day
            self.block = block
            self.is_active = is_active

        def is_event(self, c):
            is_event = True
            if self.day != c.current_day and self.day != -1:
                is_event = False
                return is_event
            if self.week_day != c.current_week_day and self.week_day != -1:
                is_event = False
                return is_event
            if self.day_time != c.add_current_day_time and self.day_time != -1:
                is_event = False
                return is_event
            if self.is_active == False:
                is_event = False
            return is_event

    Inventory = []
    Events = []

    t = 0
    while t < 50:
        Inventory.append(Event(0,0,0, "", False))
        Events.append(Event(0,0,0, "", False))
        t += 1
