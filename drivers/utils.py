import datetime
import os


def history(logs):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    filehandle = open(os.getcwd() + "/" + "logs.txt", "a")
    filehandle.write(dt_string + " ---- " + logs + '\n')
