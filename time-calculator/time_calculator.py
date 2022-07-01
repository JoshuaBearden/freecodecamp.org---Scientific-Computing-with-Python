def add_time(start, duration, day=""):
  
#Takes apart 
  start_data = start.split()
  start_time = start_data[0]
  am_pm = start_data[1]
  start_time_data = start_time.split(":")
  start_hour = int(start_time_data[0])
  start_min = int(start_time_data[1])
  duration_data = duration.split(":")
  duration_hour = int(duration_data[0])
  duration_min = int(duration_data[1])
  
# Start + Duration converts time to a 24 hour period
  final_min = start_min + duration_min
  final_hour = start_hour + duration_hour
  day_change_count = 0
  if am_pm == "PM":
    final_hour += 12
  if final_min >= 60:
    final_min %= 60
    final_hour += 1
  if final_hour >= 24:
    day_change_count = final_hour // 24
    final_hour = final_hour - (day_change_count * 24)
  
# AM to PM / PM to AM 
  if final_hour > 0 and final_hour < 12:
    am_pm = "AM"
  elif final_hour == 12:
    am_pm = "PM"
  elif final_hour > 12 :
    am_pm = "PM"
    final_hour -= 12
  else:
    am_pm = "AM"
    final_hour += 12

#Day changing uses function to create a key to find value in day_o_week
  day_o_week = {1: "Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
  display_day = ""
  if day != "":
    def get_key(val):
      for k,v in day_o_week.items():
        if val == v:
          return k
    day_key = get_key(day.lower().capitalize())
    new_day_key = day_key + day_change_count
    if new_day_key > 7:
      new_day_key = new_day_key % 7
      if new_day_key % 7 == 0:
        new_day_key = 7
    display_day = ", " + day_o_week[new_day_key]
  
  # Displaying time data
  display_str = ""
  if day_change_count >= 1:
    if day_change_count == 1:
      display_str = " (next day)"
    else: 
      display_str = " (" + str(day_change_count) + " days later)"
      
  new_time = str(final_hour) + ":" + (str(final_min) if final_min > 9 else ("0" + str(final_min))) + " " + am_pm + display_day + display_str
                                                
  return new_time


