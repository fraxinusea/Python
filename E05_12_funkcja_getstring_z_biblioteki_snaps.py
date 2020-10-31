#EG5 - 12 Funkcja get_string z biblioteki snaps
import snaps #zaimportuj biblioteke snaps
name =  snaps.get_string('Podaj swoje imię: ')
snaps.display_message('Witaj ' + name)
