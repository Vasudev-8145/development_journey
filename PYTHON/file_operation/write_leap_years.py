"""
write leap years from 1800 to 2026
"""

fw = open("file_operation\\leap_years.txt","w")

for year in range(1800,2027):

    if (year%400 == 0 and year%100 == 0) or (year%100 != 0 and year%4 == 0):

        fw.write(str(year)+"\n")

print("complted...")

fw.close()