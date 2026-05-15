def to_secs(hours, minutes, seconds):
    hours = hours * 3600
    minutes = minutes * 60
    total = hours + minutes + seconds
    return total


print(to_secs(2, 30, 10))
print(to_secs(2, 0, 0))
print(to_secs(0, 2, 0))
print(to_secs(0, 0, 42))
print(to_secs(0, -10, 10))
