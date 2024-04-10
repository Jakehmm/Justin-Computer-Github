def main():
    user_input_time = input("What's the time right now? ")
    time_conversion = convert_time(user_input_time)
    if time_conversion < 12:
        return f"{user_input_time}AM, It's currently in the morning."
    if time_conversion < 18:
        return f"{user_input_time}PM, It's currently in the afternoon."
    if time_conversion >= 18:
        return f"{user_input_time}PM, It's currently in the night."

def convert_time(time):
    hour,minutes = time.split(":")
    return float(hour) + float(minutes) / 60


print(main())
