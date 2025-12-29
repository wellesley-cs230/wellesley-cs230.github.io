import datetime


CLASS_DAYS = ['Monday', 'Tuesday', 'Thursday']
DISPLAY_DAYS = ['Monday', 'Tuesday', 'Thursday']
LECTURE_DAYS = ['Monday', 'Thursday']


# Spring
SPECIAL_DATES = [
    (datetime.datetime(2026, 1, 19), 'Martin Luther King Jr. Day: no classes'),
    (datetime.datetime(2026, 2, 16), 'President\'s Day: no classes'),
    (datetime.datetime(2026, 2, 17), 'Substitute Day: Monday Schedule'),
    (datetime.datetime(2026, 3, 16), 'Spring Break: no classes'),
    (datetime.datetime(2026, 3, 17), 'Spring Break: no classes'),
    (datetime.datetime(2026, 3, 18), 'Spring Break: no classes'),
    (datetime.datetime(2026, 3, 19), 'Spring Break: no classes'),
    (datetime.datetime(2026, 3, 20), 'Spring Break: no classes'),
    (datetime.datetime(2026, 4, 15), 'Ruhlman Conference: no classes'),
    (datetime.datetime(2026, 4, 20), 'Patriot\'s Day: no classes'),
    (datetime.datetime(2026, 4, 30), 'Substitute Day: Monday Schedule'),
    (datetime.datetime(2026, 5, 1), 'Reading Period Begins.'),
    (datetime.datetime(2026, 5, 5), 'Final Exam Period Begins.'),
]
'''
# Fall
SPECIAL_DATES = [
    (datetime.datetime(2026, 9, 1), 'Labor Day: no classes.'),
    (datetime.datetime(2026, 10, 13), 'Indigenous Peoples\' Day: no classes.'),
    (datetime.datetime(2026, 10, 14), 'Fall Break: no classes.'),
    (datetime.datetime(2026, 10, 28), 'Tanner Conference: no classes.'),
    (datetime.datetime(2026, 11, 26), 'Thanksgiving Break: no classes.'),    
    (datetime.datetime(2026, 11, 27), 'Thanksgiving Break: no classes.'),    
    (datetime.datetime(2026, 11, 28), 'Thanksgiving Break: no classes.'),    
    (datetime.datetime(2026, 12, 11), 'Reading Period Begins.'),    
    (datetime.datetime(2026, 12, 15), 'Final Exam Period Begins.'),    
]
'''


READING_PERIOD_START = datetime.datetime(2026, 5, 1)


def is_date_special(current):
    for d, desc in SPECIAL_DATES:
        if d == current:
            return desc

    return None


def generate_yml_calendar():
    course_start = datetime.datetime(2026, 1, 19)
    course_end = datetime.datetime(2026, 5, 8)

    start = course_start - datetime.timedelta(days=course_start.weekday())
    end = course_end + datetime.timedelta(days=6 - course_end.weekday())

    print('events:')

    current = start
    while current <= end:
        day = current.strftime('%A')

        if day in CLASS_DAYS:        
            print('  - month: "{}"'.format(current.strftime('%B')))
            print('    day: "{}"'.format(current.strftime('%d')))
            print('    day-of-week: "{}"'.format(day))

            desc = is_date_special(current)
            if desc is not None:
                print('    special: "{}"'.format(desc))

            if day in CLASS_DAYS:
                print('    topic:')

            print('    due:')
            print('    released:')
            print('    pre-class:')

            if current >= READING_PERIOD_START:
                print('    class-meetings-over: true')
                
            print('')

        current = current + datetime.timedelta(days=1)



def main():    
    generate_yml_calendar()

    
if __name__ == '__main__':
    main()
