#EG5 - 05 Prosty budzik z blokiem else
import time
current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
if (hour>7) or ( hour==7 and minute>29 ):
    print('Już pora wstać')

else:
    print('Wracaj do łóżka')
