# Temat projektu nr 5: Narzędzie do agregacji prefiksów IPv4
Łukasz Grabowski

Krzysztof Ślązak

Tomasz Puchała

Bartosz Adamek

### Zasada agregacji:
* znaleźć najdłuższy wspólny prefiks ich części sieciowych
* skracamy część sieciową (maskę) i tworzymy uogólniony adres IP sieci (tzw. adres nadsieci lub CIDR – supernet address lub CIDR address)
* **uwaga**: nadsieć nie może zawierać adresów spoza danego zakresu adresów IP

Program  wywołuje się z linii komend podając jako parametr pliki z adresami IP. Program obsługuje 1 lub 2 pliki (adresy w plikach w formacie dec np. 192.168.1.1).

![image](https://github.com/Varkame/AgregacjaIP/blob/main/1.jpg)
![image](https://github.com/Varkame/AgregacjaIP/blob/main/2.jpg)

Po braku nazwy pliku jako parametr (wyświetli się błąd) :

![image](https://github.com/Varkame/AgregacjaIP/blob/main/3.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/4.jpg)

Po wpisaniu więcej niż 2 nazwy pliku jako parametr (wyświetli się błąd) :
![image](https://github.com/Varkame/AgregacjaIP/blob/main/5.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/6.jpg)

### Poprawne wywołanie programy dla 1 pliku :
Lista adresów IP w pliku RouterA.txt

![image](https://github.com/Varkame/AgregacjaIP/blob/main/7.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/8.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/9.jpg)

1.	Ilość adresów IP w pliku.
2.	Adresy  IP z pliku przekonwertowane do postaci binarnej
3.	Sprawdzamy czy w pliku duplikują się adresy IP
4.	Sprawdzane jest czy adresy są spójne ( „po kolei”) - nadsieć nie może zawierać adresów spoza danego zakresu adresów IP
5.	Adres nadsieci w postaci binarnej i dec
6.	W przypadku 1 pliku jako parametr nie następuje sprawdzenie duplikujących się adresów z 2 plikiem – nie istnieje.


### Poprawne wywołanie programy dla 1 pliku – duplikacja adresów IP (jedna para) w pliku :
Lista adresów IP w pliku RouterA.txt

![image](https://github.com/Varkame/AgregacjaIP/blob/main/10.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/11.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/12.jpg)

1.	Skrypt przerywa działanie oraz wskazuje numery wierszy duplikujących się wraz adresem IP w formie binarnej. (należy pamiętać ze numeracja wierszy w listach rozpoczyna się od 0) – w naszym przykładzie 4 i 5 to wiersz 5 i 6
 
Poprawne wywołanie programy dla 1 pliku – duplikacja adresów IP (dwie pary) w pliku :
Lista adresów IP w pliku RouterA.txt

![image](https://github.com/Varkame/AgregacjaIP/blob/main/13.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/14.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/15.jpg)

1.	Skrypt przerywa działanie oraz wskazuje numery wierszy duplikujących się wraz adresem IP w formie binarnej. (należy pamiętać ze numeracja wierszy w listach rozpoczyna się od 0) – w naszym przykładzie 0 i 1 to wiersz 1 i 2 oraz 4 i 5 to wiersz 5 i 6

### Poprawne wywołanie programu dla 2 plików :
Lista adresów IP w pliku RouterA.txt oraz RouterB.txt

![image](https://github.com/Varkame/AgregacjaIP/blob/main/16.jpg)
![image](https://github.com/Varkame/AgregacjaIP/blob/main/17.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/18.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/19.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/20.jpg)

1.	Analizowany jest plik nr 1
2.	Analizowany jest plik nr 2
3.	Wypisywane są w postaci binarnej połączone adresy IP z pliku 1 oraz 2 w celu sprawdzeniu duplikujących się adresów IP pomiędzy plikami. 
4.	Informacja o braku duplikujących się adresów

### Poprawne wywołanie programy dla 2 plików (duplikacja adresów IP pomiędzy plikami:
Lista adresów IP w pliku RouterA.txt oraz RouterB.txt

![image](https://github.com/Varkame/AgregacjaIP/blob/main/21.jpg)
![image](https://github.com/Varkame/AgregacjaIP/blob/main/22.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/23.jpg)

1.	Informacja w których wierszach nastąpiła duplikacja adresów IP

### Poprawne wywołanie programy (brak spójności adresów IP):
Lista adresów IP w pliku RouterA.txt

![image](https://github.com/Varkame/AgregacjaIP/blob/main/24.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/25.jpg)

1.	Informacja o braku spójności i propozycja podziału pliku RouteraA.txt na 2 pliki z adresami od 200.1.0.0 do 200.1.3.0 oraz drugi plik z adresami od 200.1.6.0 do 200.1.13.0 – oczywiście w drugim pliku tez nastąpią brak spójności z propozycja podzielenia pliku 2 na kolejna dwa pliki z adresami 200.1.6.0 do 200.1.8.0 oraz 200.1.11.0 do 200.1.13.0 
2.	Brak sprawdzanie spójności naruszy zasadę – „nadsieć nie może zawierać adresów spoza danego zakresu adresów IP” w naszym przypadku przy braku sprawdzania spójności powstałby adres nadsieci 200.1.0.0/20 zawierający nie istniejące adresy IP (200.1.5.0;200.1.9.0;200.1.10.0) – (1)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/26.jpg)

### Kilka uwag:
* Adresy nadsieci zapisywane są w plikach txt o nazwie Wynik_”Nazwa_pliku”

![image](https://github.com/Varkame/AgregacjaIP/blob/main/27.jpg)
 
*	Przy wpisywaniu adresów ip w plikach proszę nie zostawiać pustego pierwsza za ostania linią z adresem – wystąpi błąd:

![image](https://github.com/Varkame/AgregacjaIP/blob/main/28.jpg)

![image](https://github.com/Varkame/AgregacjaIP/blob/main/29.jpg)
