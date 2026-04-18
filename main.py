def convert_time(times):
    result = []
    for time in times:
        hours = time // 3600000
        minutes = (time % 3600000) // 60000
        seconds = (time % 60000) // 1000
        result.append(f"{hours} soat {minutes} minut {seconds} sekund")
    return result

times = [3661001, 3600000, 65000]
print(convert_time(times))
