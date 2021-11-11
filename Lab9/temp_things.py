avg_lows = [26, 27, 32, 36, 42, 47, 50, 50, 44, 36, 31, 24]
avg_highs = [37, 41, 49, 57, 65, 72, 83, 84, 74, 60, 44, 35]

def avg_monthly_temps(avg_lows, avg_highs):
    avg_temps = []
    for i in range(len(avg_lows) - 1):
        low = avg_lows[i]
        high = avg_highs[i]
        average = (low + high) / 2
        avg_temps.append(average)
    print(avg_temps)
    print()

avg_monthly_temps(avg_lows, avg_highs)
        
def annual_avgs(avg_lows, avg_highs):
    total = 0
    for i in range(len(avg_lows)):
        total += avg_lows[i]
    low_average = total / len(avg_lows)
    print(low_average)
    print()

    total = 0
    for i in range(len(avg_highs)):
        total += avg_highs[i]
    high_average = total / len(avg_highs)
    print(high_average)
    print()
    print()
    print()


annual_avgs(avg_lows, avg_highs)

def dumber_annual_avgs(avg_lows, avg_highs):
    total = 0
    for i in range(len(avg_lows) - 1):
        total += avg_lows[i + 1]
    low_average = total / (len(avg_lows) - 2)
    print(low_average)
    print()

    total = 0
    for i in range(len(avg_highs) - 1):
        total += avg_highs[i + 1]
    high_average = total / (len(avg_highs) - 2)
    print(high_average)
    print()


dumber_annual_avgs(avg_lows, avg_highs)
