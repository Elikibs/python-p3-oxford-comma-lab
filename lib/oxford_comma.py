def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    else:
        return ", ".join(items[0:-1]) + " and " + items[-1]

print(oxford_comma(["fiddleheads", "okra", "kohlrabi", "hello", "fine"]))
