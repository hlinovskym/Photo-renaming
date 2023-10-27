import os
import shutil
from datetime import datetime, timedelta
import pytz


# nezapomenout v main.py i check.py prepsat spravnou cestu
# odmazat dlouhy nazvy rucne - mozna kontrola pomoci check.py
# spustit main.py - prejmenuje soubory o 1 nebo 2 hodiny
# pomoci hromadneho prejmenovani v total commanderu odmazat posledni tri znaky (koncime sekundama)
# zkontrolovat delku pomoci check.py a pripadne rucne prejmenovat ty fotky, co byly vyfoceny v jedne sekunde


################################################################
###       prepis cestu a pozor na milisekundy !!!            ###
################################################################

PATH = "/.../"


def is_dst(dt, time_zone):
    aware_dt = time_zone.localize(dt)
    if aware_dt.dst() != timedelta(0, 0):
        print("summer")
        return 2
    else:
        print("winter")
        return 1


time_zone = pytz.timezone("Europe/Prague")
files = os.listdir(PATH)

for file in files:
    print(file)
    file_split = file.split("_")
    print(file_split)
    file_time = file_split[-1].split(".")
    file_split = file_split[:2]
    file_split.append(file_time[0])
    file_split.append(file_time[1])
    print(file_split)

    year = int(file_split[1][:4])
    month = int(file_split[1][4:6])
    day = int(file_split[1][6:])
    hour = int(file_split[2][:2])
    minute = int(file_split[2][2:4])
    second = int(file_split[2][4:6])
    milisecond = int(file_split[2][6:])

    photo_date = datetime(year, month, day, hour, minute, second)
    print(photo_date)

    delta = is_dst(photo_date, time_zone)
    time_delta = timedelta(hours=delta)

    new_photo_date = photo_date + time_delta
    print(new_photo_date)

    # s milisekundama
    new_name = new_photo_date.strftime(f"%Y%m%d_%H%M%S{milisecond}.{file_split[-1]}")
    # bez milisekund
    # new_name = new_photo_date.strftime(f"%Y%m%d_%H%M%S.{file_split[-1]}")
    print(new_name)
    print("--------------------------------------")

    shutil.move(PATH + file, PATH + new_name)

print("--------------------------------------")
print(len(files))
# help(shutil.move)
