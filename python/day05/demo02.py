import statistics, time, datetime
import calendar

d = datetime.date.today()
print(d.weekday())
print(datetime.date(2018, 10, 1).weekday())
print(calendar.month(2018, 10))

# score = {30, 40, 60, 70, 80, 90}
# print(statistics.mean(score))
# print(statistics.median_high(score))
# print(statistics.median_low(score))

# t = time.time()
# print(t)
# print(time.ctime(t))
# now = time.localtime(t)
# print(now)
# print("%d년 %d월 %d일" % (now.tm_year, now.tm_mon, now.tm_mday))
# print("{0}:{1}:{2}".format(now.tm_hour, now.tm_min, now.tm_sec))

# start = time.time()
# str = ""
# for a in range(10000):
#     time.sleep(0.5)
#     str += "*"
#     print(str)

# end = time.time()
# print("Elapsed time:{0}".format(end - start))

# for dan in range(1, 10):
#     print(dan, "단")
#     for hang in range(2, 10):
#         print(dan, "*", hang, "=", (dan*hang))
#         time.sleep(0.2)
#     print()
#     time.sleep(1)