access_time = 69
load_time = 28
replace_time = 14
replace_ratio = 0.64
error_ratio = 4 / 100000

load_ratio = 1 - replace_ratio
reload_time = load_time + replace_time
error_time = (load_ratio * load_time) + (replace_ratio * reload_time)
eat = error_ratio * (error_time * 1000000) + (1 - error_ratio) * access_time

print(eat)
