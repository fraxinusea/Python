#E05 - 03 Prosty budzik z dzwiękiem
import time #zaimportuj biblioteke time
import snaps
current_time = time.localtime() #uzyskaj wartość czasu
hour = current_time.tm_hour #uzyskaj wartość godziny
minute = current_time.tm_min
it_is_time_to_get_up = (hour>7) or (hour>7 and minute>29)
if it_is_time_to_get_up:
    print('RAFCIU, JUŻ PORA PRZESTAĆ SIĘ DĄSAĆ')
    snaps.display_message('już pora wstać')
    snaps.play_sound('siren.wav')
    time.sleep(10)#daje czas na wstrzymanie
