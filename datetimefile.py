from datetime import date
today = date.today()
# Textual month, day and year
d1 = today.strftime("%B %d, %Y")
print(d1)