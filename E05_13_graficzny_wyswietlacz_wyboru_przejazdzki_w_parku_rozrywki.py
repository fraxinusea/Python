#EG5 - 13 Graficzny wyświetlacz wyboru przejażdzki w parku rozrywki
import snaps
snaps.display_image('themepark.png')
prompt='''Dostepne są następujące przejażdżki

      1. Malowniczy rejs po rzecze
      2. Karnawałowa karuzela
      3. Przygoda w dżungli. Skok do wody
      4. Zjeżdżanie z góry
      5. Szalona kolejka górska
    
wprowadź numer przejażdzki'''
                    
ride_number_text = snaps.get_string(prompt,vert='bottom', max_line_length=3)
confirm='Przejażdżka ' + ride_number_text
snaps.display_message(confirm)
