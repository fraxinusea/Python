#EG5-10 Wybór przejażdżek
print('''Witamy w naszym parku rozrywki
Dostępne są następujące przejażdżki:

      1. Malowniczy rejs po rzecze
      2. Karnawałowa karuzela
      3. Przygoda w dżungli. Skok do wody
      4. Zjeżdżanie z góry
      5. Szalona kolejka górska
      ''')
ride_number_text = input('wprowadź numer przejażdzki')
ride_number = int(ride_number_text)

if ride_number == 1:
    print('wybrałeś malowniczy rejs po rzece.Nie ma ograniczeń wiekowych')
else:
    print('podaj wiek')
    age_text = input('Podaj ile masz lat')
    age = int(age_text)
    if ride_number == 2:
        print('wybrałeś przejażdżkę Karnawałowa karuzela')
        if age>= 3:
            print('Zapraszam na karnawałową karuzelę')
        else:
            print('Za młody jesteś')
    if ride_number == 3:
        print('wybrałeś przejażdżkę Przygoda w dżungli skok do wody')
        if age >= 6:
            print('Zapraszam na przygodę w dżungli')
        else:
            print('Za młody jesteś')
    if ride_number == 4:
        print('wybrałeś przejażdżkę Zjeżdżanie z góry')
        if age >= 12:
            print('Zapraszam na zjeżdżanie z góry')
        else:
            print('Za młody jesteś')
    if ride_number == 5:
        print('wybrałeś przejażdżkę szalona kolejka górska')
        if age >= 12:
            if age >=70:
                print('Niestety, za stary jesteś')
            else:
                print('Możesz skorzystać z przejażdżki')
        else:
            print('Za młody jesteś ')

  
