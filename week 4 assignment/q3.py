# BS month names in order 
bs_months = ["Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
             "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]
customers = [
    {"name": "Ramesh Thapa",  "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki",  "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai",    "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]
def convert_date(date_str, from_cal, to_cal):
    parts = date_str.split("-")
    year  = int(parts[0])
    month = int(parts[1])
    day   = int(parts[2])
    # if both calendars are same
    if from_cal == to_cal:
        return year, month, day
    # AD to BS: add 56 to year
    if from_cal == "AD" and to_cal == "BS":
        year = year + 56
    # BS to AD: subtract 56 from year
    if from_cal == "BS" and to_cal == "AD":
        year = year - 56

    return year, month, day
def format_date(year, month, day, to_cal, style):
    # adding correct sufix to the numbers
    def ordinal(d):
        if d in [1, 21, 31]:
            return f"{d}st"
        elif d in [2, 22]:
            return f"{d}nd"
        elif d in [3, 23]:
            return f"{d}rd"
        else:
            return f"{d}th"

    if style == "iso":
        return f"{year}-{month:02d}-{day:02d} {to_cal}"

    # style "full" - "15th Ashadh, 2041 BS"
    if style == "full":
        if to_cal == "BS":
            month_name = bs_months[month - 1]  # month-1 because list starts at 0
            return f"{ordinal(day)} {month_name}, {year} BS"
        else:
            return f"{ordinal(day)} {month:02d}, {year} AD"

    # style "nepali" - "2041-06-24 BS"
    if style == "nepali":
        return f"{year}-{month:02d}-{day:02d} {to_cal}"

for c in customers:
    year, month, day = convert_date(c["date"], c["cal"], c["need"])
    converted = format_date(year, month, day, c["need"], c["style"])
    print(f"{c['name']} | Original: {c['date']} {c['cal']} | Converted: {converted}")