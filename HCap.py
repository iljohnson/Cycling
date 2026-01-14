
import pandas as pd
from datetime import datetime, timedelta
import getpass
import itertools

Username = getpass.getuser()
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 300)


def handicap(grades=('Limit', 'D', 'C', 'B', 'Scratch'), speed=(31.0, 33.0, 35.0, 37.0, 39.0),
             start_time="10:00:00", race_dist=37.7, merge_dist=1.0):

    start_time = datetime.strptime(start_time, '%H:%M:%S')
    racetime = list(itertools.repeat(0, len(grades)))  # create a list of zeros equal to the number of grades
    tot_racetime = list(itertools.repeat(0, len(grades)))
    handicap_time = list(itertools.repeat(0, len(grades)))
    handicap_delta = list(itertools.repeat(0, len(grades)))
    gap_distance = list(itertools.repeat(0, len(grades)))
    race_distance = list(itertools.repeat(0, len(grades)))
    merge_point = list(itertools.repeat(0, len(grades)))
    group_label = list(itertools.repeat(0, len(grades)))
    start_label = list(itertools.repeat(0, len(grades)))
    limit_time = (race_dist-merge_dist) / (speed[0] / 3600)

    for x in range(0, len(grades)):
        handicap_time[x] = str(timedelta(hours=start_time.hour, minutes=start_time.minute,
                                         seconds=round((limit_time - (race_dist-merge_dist) / (speed[x] / 3600))/15)*15))
        racetime[x] = str(timedelta(
            seconds=round(((race_dist - merge_dist)/ (speed[x] / 3600))/15)*15))
        tot_racetime[x] = str(timedelta(
            seconds=round((race_dist / (speed[x] / 3600))/15)*15))
        group_label[x] = str(timedelta(
            seconds=round(((race_dist-merge_dist) / (speed[0] / 3600))/15)*15) - timedelta(
            seconds=round(((race_dist-merge_dist) / (speed[x] / 3600))/15)*15))

        race_distance[x] = race_dist
        merge_point[x] = race_dist-merge_dist

        if x > 0:

            handicap_delta[x] = str(datetime.strptime(handicap_time[x], "%H:%M:%S") -
                                    datetime.strptime(handicap_time[x - 1], "%H:%M:%S"))
            str_to_time = datetime.strptime(handicap_delta[x], "%H:%M:%S")
            gap_distance[x] = round((timedelta(hours=str_to_time.hour, minutes=str_to_time.minute,
                                               seconds=str_to_time.second).total_seconds()) *
                                    (speed[x - 1] * 1000) / 3600) / 1000

    for x in range(0, len(group_label)):
        start_label[x] = str(datetime.strptime(group_label[-1], "%H:%M:%S") - datetime.strptime(group_label[x], "%H:%M:%S"))


    df = pd.DataFrame(
        list(zip(grades, start_label, handicap_time,
                 handicap_delta,
                 gap_distance, speed, racetime
                 , merge_point, tot_racetime, race_distance)),
        columns=['Grade', 'Lead (h:m:s)', 'Start (h:m:s)', 'Gaps (m:s)', 'Start (km)',
                 'Speed (km/h)', 'MP Time (h:m:s)', 'Dist to MP (km)', 'Race Time (h:m:s)'
                    , 'Race_Dist (km)']).iloc[::-1]


    # print(df)
    # print(z)


    return df
#handicap()
