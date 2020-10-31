#E05 - 04 Budzik z wyświetlaniem
import time #zaimportuj biblioteke time
import snaps
current_time = time.localtime() #uzyskaj wartość czasu
hour = current_time.tm_hour #uzyskaj wartość godziny
minute = current_time.tm_min
it_is_time_to_get_up = (hour>7) or (hour>7 and minute>29)
if it_is_time_to_get_up:
    print('JUŻ PORA WSTAĆ')
    print('WSTAŃ I UŚMIECHNIJ SIĘ')
print('Bieżący czas: ', hour, ':' , minute) #wcięcie w tekście pozwala wyjść poza konstrukcję if//komunikat wyświetli się zawsze

