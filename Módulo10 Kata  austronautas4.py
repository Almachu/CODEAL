def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"
print(water_left("3", "200", None))

###
#Exception has occurred: TypeError
#All arguments must be of type int, but received: '3'
#  File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata  austronautas4.py", line 5, in water_left
#    argument / 10

#During handling of the above exception, another exception occurred:

#  File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata  austronautas4.py", line 9, in water_left
#    raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
#  File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata  austronautas4.py", line 16, in <module>
#    print(water_left("3", "200", None))
###