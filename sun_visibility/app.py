from datetime import timedelta
import csv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

def timeframe(value):
    hours, minutes, seconds = [int(component) for component in value.split(":")]
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

sun_by_day: dict[str, list] = {}
with open(args.file) as data:
    for line in data:
        line_array = line.split()
        if len(line_array) < 2:
            continue
        date = line_array[0]
        time = line_array[1]
        value = sun_by_day.get(date)
        if value:
            value.append(time)
        else:
            sun_by_day[date] = [time]

with open('output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    print("file output.csv in creazione")

    # write the header
    writer.writerow(["date", "start time", "end time", "duration"])

    for key, values in sun_by_day.items():
        values.sort()
        time_start = timeframe(values[0])
        time_end = timeframe(values[-1])
        duration = time_end - time_start
        # print(key)
        # print(time_start)
        # print(time_end)
        # print(duration)

        # write the data
        writer.writerow([key, time_start, time_end, duration])

print("file output.csv creato nella cartella dalla quale è stato eseguito lo script")