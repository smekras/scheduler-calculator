access_time = 203
load_time = 16
replace_time = 19
replace_ratio = 0.52
error_ratio = 10 / 100000

load_ratio = 1 - replace_ratio
reload_time = load_time + replace_time
error_time = (load_ratio * load_time) + (replace_ratio * reload_time)
eat = error_ratio * (error_time * 1000000) + (1 - error_ratio) * access_time

print(eat)
