def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

print(water_left(5, 100, 2))

###
#Exception has occurred: RuntimeError
#There is not enough water for 5 astronauts after 2 days!
#  File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata  austronautas2.py", line 6, in water_left
#    raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
#  File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata  austronautas2.py", line 9, in <module>
#    print(water_left(5, 100, 2))
###