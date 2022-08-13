import time

print('UTC time on 0 Sec :', time.gmtime(0))
print('Current local Time :', time.localtime())

print('Current Seconds on UTC :', time.time())

# will give you time according to UTC
print('UTC time on give sec :', time.gmtime(1586672727.925807))

# default value for parameter us time.time()
print('Current UTC time :', time.gmtime())

# Printing some properties
time_local = time.localtime()
print('Year : ', time_local[0], time_local.tm_year)
print('Month : ', time_local[1], time_local.tm_mon)
print('Day : ', time_local[2], time_local.tm_mday)

print('Print Formatted Time :', time.strftime('%x', time_local))

print('Time : \t\t\t', time.get_clock_info('time'))
print('Perf Counter \t: ', time.get_clock_info('perf_counter'))
print('Monotonic  \t\t: ', time.get_clock_info('monotonic'))
print('Process Time : \t', time.get_clock_info('process_time'))




