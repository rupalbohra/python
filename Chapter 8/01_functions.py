def percent(marks):
    return (sum(marks)/400)*100

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks1 = [95, 98, 96, 99]
percentage2 = percent(marks1)

print(percentage1, percentage2, sep = ', ')
