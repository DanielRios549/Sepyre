def time(ms: int) -> str:
    secs = 0

    if str(ms).isnumeric() and str(ms) != '0':
        secs = int(str(ms)[:-3])

    if secs == 0:
        return '0:00'
    else:
        minutes = secs // 60
        seconds = secs % 60
        returnedSeconds = f'0{seconds}' if seconds < 10 else str(seconds)

        return f'{minutes}:{returnedSeconds}'
