from datetime import datetime, date, timedelta

def day_counter(start_day):
    """ Function that will print out every work day from certain date
    excluding weekend (Saturday and Sunday). """

    day = datetime.strptime(start_day, '%m/%d/%Y').date()
    tomorrow = date.today() + timedelta(days=1)
    while day != tomorrow:
        if day.weekday() not in {5, 6}:
            yield day.strftime('%m/%d/%Y')
        day += timedelta(days=1)
i = 0
for day in day_counter('04/01/2020'):
    print(day)
    i +=1
print(i)
