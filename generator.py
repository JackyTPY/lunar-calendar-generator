from zhdate import ZhDate
from datetime import datetime, timedelta
import pandas as pd

def generate_calendar(match, start, end, subject, output):
  schedule = []
  
  while start <= end:
    lunarDate =  ZhDate.from_datetime(start) 
    if match(lunarDate):
      schedule.append({
        "Subject": subject,
        "Start Date": start.strftime("%Y/%m/%d"),
        "Start Time": "00:00",
        "End Date": start.strftime("%Y/%m/%d"),
        "End Time": "23:59",
        "All Day Event": True
      })
    start += timedelta(days=1)

  df = pd.DataFrame(schedule)
  df.to_csv(output, index=False)

if __name__ == '__main__':
  start = datetime(year=2000, month=1, day=1)
  end = datetime(year=2100, month=12, day=31)

  def ten_day_veg_rule(lunar):
    try:
      ZhDate(lunar.lunar_year, lunar.lunar_month, 30)
      return lunar.lunar_day in [1, 8, 14, 15, 18, 23, 24, 28, 29, 30]
    except:
      return lunar.lunar_day in [1, 8, 14, 15, 18, 23, 24, 27, 28, 29]
    

  generate_calendar(ten_day_veg_rule, start, end, '十齋日', 'schedule/十齋日.csv')

  # def first_rule(lunar):
  #   return lunar.lunar_day in [1]

  # generate_calendar(first_rule, start, end, '農曆初一', 'schedule/農曆初一.csv')

  # def second_rule(lunar):
  #   return lunar.lunar_day in [2]

  # generate_calendar(second_rule, start, end, '農曆初二', 'schedule/農曆初二.csv')

  # def fifteenth_rule(lunar):
  #   return lunar.lunar_day in [15]

  # generate_calendar(fifteenth_rule, start, end, '農曆十五', 'schedule/農曆十五.csv')

  # def sixteenth_rule(lunar):
  #   return lunar.lunar_day in [16]

  # generate_calendar(sixteenth_rule, start, end, '農曆十六', 'schedule/農曆十六.csv')