import datetime
import os


OUTPUT_DIR = 'output'


CLASS_DAYS = ['Monday', 'Tuesday', 'Thursday']
MEETING_TIMES = ['14:20', None, '14:20'] # (military time)
SESSION_TYPE = ['Lecture', 'Lab', 'Lecture']
DISPLAY_DAYS = CLASS_DAYS


SPECIAL_DATES = [
    (datetime.datetime(2024, 9, 2), 'Labor Day: no classes.'),
    (datetime.datetime(2024, 10, 14), 'Indigenous Peoples’ Day: no classes.'),
    (datetime.datetime(2024, 10, 15), 'Fall Break: no classes.'),
    (datetime.datetime(2024, 10, 29), 'Tanner Conference: no classes.'),
    (datetime.datetime(2024, 11, 27), 'Thanksgiving Break: no classes.'),
    (datetime.datetime(2024, 11, 28), 'Thanksgiving Break: no classes.'),
    (datetime.datetime(2024, 11, 29), 'Thanksgiving Break: no classes.'),
    (datetime.datetime(2024, 12, 11), 'Substitute Day (Lake Day Makeup).'),
    (datetime.datetime(2024, 12, 12), 'Reading Period Begins.'),
    (datetime.datetime(2024, 12, 15), 'Reading Period Ends.'),
]

READING_PERIOD_START = datetime.datetime(2024, 12, 12)

EVENT_TEMPLATE = '''---
type: raw_event
name: {}
title: 
date: {}
description: 
tldr: 
hide_from_announcments: true
thumbnail:
links:
    - slides: 
      name: slides
---

**Before class:**
* 
'''

def is_date_special(current):
    for d, desc in SPECIAL_DATES:
        if d == current:
            return desc

    return None


def generate_md_calendar():
    course_start = datetime.datetime(2024, 9, 2)
    course_end = datetime.datetime(2024, 12, 17)

    start = course_start - datetime.timedelta(days=course_start.weekday())
    end = course_end + datetime.timedelta(days=6 - course_end.weekday())

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    current = start
    while current <= end:
        day = current.strftime('%A')

        if day in DISPLAY_DAYS:
            idx = DISPLAY_DAYS.index(day)
            mtg_time = MEETING_TIMES[idx]
            session_type = SESSION_TYPE[idx]
            
            date = current.strftime('%Y-%m-%d')
            fname = '{}_{}.md'.format(date, day)
            
            with open(os.path.join(OUTPUT_DIR, fname), 'w') as f:
                f.write(EVENT_TEMPLATE.format(
                    session_type,
                    '{}{}'.format(
                        date,
                        'T{}:00+3:30'.format(mtg_time) if mtg_time is not None else '',
                    ),
                ))

            '''
            if current >= READING_PERIOD_START:
                print('    class-meetings-over: true')
                
            print('')
            '''

        current = current + datetime.timedelta(days=1)



def main():    
    generate_md_calendar()

    
if __name__ == '__main__':
    main()
