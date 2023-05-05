import subprocess

from datetime import datetime

import pytz

UTC = pytz.utc

IST = pytz.timezone('Europe/Paris')
  
datetime_ist = datetime.now(IST)
print(datetime_ist.strftime('%Y-%m-%d'))
