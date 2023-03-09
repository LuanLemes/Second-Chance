label start_time_variables:
    $ week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    $ day_time = ["Morning", "Afternoon", "Evening", "Dawn", "Late Down"]
    $ current_week_day = 3
    $ current_day_time = 3
    $ current_day = 0
    $ calendar = Calendar(0, week_days, day_time, 0, 0)
    $ event_one = Event(-1, -1, 10, "event_one", True)
    $ Events[0] = event_one
    $ c = 0
    $ show_calendar = True
    return

label time_next():
    $ calendar.add_current_day_time(1)
    window hide
    return

label time_skip_to_night():
    while calendar.current_day_time < 2:
        call time_next()
    return

label time_days_next(number_of_days):
    $ calendar.add_current_day(number_of_days)
    return

label time_one_day_next():
    $ calendar.add_current_day(1)
    return