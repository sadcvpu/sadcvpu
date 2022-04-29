from sutime import SUTime

test_case = 'martes'
sutime = SUTime(mark_time_ranges=True, include_range=True,language='spanish')
print(sutime.parse(test_case))