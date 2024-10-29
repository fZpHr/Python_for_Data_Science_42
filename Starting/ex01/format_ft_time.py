import time as t
import datetime as dt

current_time = t.time()
date_time = dt.datetime.fromtimestamp(current_time).strftime('%B %d, %Y')
scientific_notation = format(current_time, ".2e")
formatted_current_time = format(current_time, ",.4f")

print("Second since January 1, 1970: " + formatted_current_time + " or " + scientific_notation + " in scientific notation" + "\n" + date_time)