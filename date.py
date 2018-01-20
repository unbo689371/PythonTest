import datetime
import time
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday

print(getYesterday())

while(2>1):
    DD=time.strftime("%Y-%m-%d--%H:%M:%S")
    print(DD) 
    time.sleep(1)
