import ipaddress
from operator import xor
from collections import defaultdict
import sys
import os


def ip2bin(ip):
    octets = map(int, ip.split('/')[0].split('.'))  # '1.2.3.4'=>[1, 2, 3, 4]
    binary = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
    range = int(ip.split('/')[1]) if '/' in ip else None
    return binary[:range] if range else binary


def ip_format(bin):
    return '.'.join(str(int(bin[i:i + 8], 2)) for i in range(0, 32, 8))


def myfunc(listy_ip_dec):
    for i in range(len(listy_ip_dec[0])):
        for l in range(len(listy_ip_dec)):
            if (l + 1 < (len(listy_ip_dec))):
                if (xor((int(listy_ip_dec[l][i])), int((listy_ip_dec[l + 1][i])))):
                    # print("Bład na bicie",i)
                    return i


def zapis_do_pliku(filename, adres_Agregacja_str):
    f = open("Wynik_" + filename, "w", encoding="utf-8")
    f.write(adres_Agregacja_str)


def spraw_ip_dupl(listy_def):
    print()
    D = defaultdict(list)
    for i, item in enumerate(listy_def):
        D[item].append(i)
    D = {k: v for k, v in D.items() if len(v) > 1}
    if D:
        print("Bład : duplikuje sie adres IP")
        print(D)
        print()
        sys.exit()

    else:
        print("Nie ma duplikacji adresow IP")
        print()


def ilosc_argumentow(ilsoc_arg):
    if (ilsoc_arg > 3) or (ilsoc_arg < 2):
        print("Skrypt osbługuje 1 lub 2 pliki 'txt'")
        sys.exit()

def spoj_adresacji(listy_ip_dec):
    for line in range(0, len(listy_ip_dec)):
        if (line + 1 < (len(listy_ip_dec))):
            if ((int(listy_ip_dec[line], 2) + 1) != (int(listy_ip_dec[line + 1], 2))):
                #print(line)
                print("Nie spojny adres pomiedzy wierszem nr ", line + 1, "a nr ", line + 2)
                print("Podziel plik na plik zawierajacy adresy od ",(line-line)+1," do ",line+1)
                print("Podziel plik na plik zawierajacy adresy od ",line+2," do ",(len(listy_ip_dec)))
                sys.exit()
        else:
            print("Adresy spojne")



# ilosc_arg=len(sys.argv)
# print("Ilosc rgumentow ",ilosc_arg)

os.system('cls')  # czyszczenie konsoli przed uruchomieniem skryptu

ilosc_arg = len(sys.argv)
#print("Ilosc argumentow ", ilosc_arg)
ilosc_argumentow(ilosc_arg)

# -----------------------------------------------------PLIK 1-------------------------------------------------------------------------------------
if (ilosc_arg == 2 or 3):

    filepath_1 = sys.argv[1]

    print()
    print("------------OBLICZANIE AGREGACJI Z PLIKU NR 1--------------")

    f = open(filepath_1, "r", encoding="utf-8").read()
    lines_1 = f.split('\n')  # całą treść pliku musimy podzielić przez nową linię („\n”) i wiersze zapisać do tablicy.
    ilosc_lini = 0  # zmienna pomocnicza do liczenia lini w pliku

    for line in lines_1:  # zliczam ilosc lini w pliku
        ilosc_lini = ilosc_lini + 1
    print()
    print("Ilosc adresow w pliku :", end="")
    print(ilosc_lini)

    listy_ip_dec = [[] for i in range(ilosc_lini)]  # tworze dynamicznie liste w liscie
    listy_ip_int = [[] for i in range(ilosc_lini)]  # tworze dynamicznie liste w liscie

    print()
    ilosc_lini_tmp = 0  # zmienna pomocnicza do indeksowania list
    for line in lines_1:
        listy_ip_dec[ilosc_lini_tmp] = ip2bin(line)
        ilosc_lini_tmp = ilosc_lini_tmp + 1
    '''   
    print("Adresy IP pliku nr 1 przed sortowaniowaniem:")
    ilosc_lini_tmp_1 = 0  # wypisywanie listy
    for line in lines_1:
        print(listy_ip_dec[ilosc_lini_tmp_1])
        ilosc_lini_tmp_1 = ilosc_lini_tmp_1 + 1
    print()
    '''
    listy_ip_dec.sort()
    print("Adresy IP pliku nr 1 po sortowaniu:")
    ilosc_lini_tmp_1 = 0  # wypisywanie listy
    for line in lines_1:
        print(listy_ip_dec[ilosc_lini_tmp_1])
        ilosc_lini_tmp_1 = ilosc_lini_tmp_1 + 1

    # ----------------------------------konwersja str na int---------------------------------------
    ilosc_lini_tmp_2 = 0  # wypisywanie listy
    for line in lines_1:
        listy_ip_int[ilosc_lini_tmp_2] = int(listy_ip_dec[ilosc_lini_tmp_2])
        ilosc_lini_tmp_2 = ilosc_lini_tmp_2 + 1
    # ---------------------------------------------------------------------------------------------------------------
    # ---------------------------------sprawdzam czy duplikuja sie adresy IP w pliku-----------------------------
    #print()
    spraw_ip_dupl(listy_ip_int)
    # ---------------------------------sprawdzam spojnosci adresow ip-----------------------------
    spoj_adresacji(listy_ip_dec)
    print()

    # ---------------------------------XOR - znajdywanie roznic ----------------------------------------
    blad = (myfunc(listy_ip_dec))
    # print(blad)
    # ---------------------------------------------------------------------------------------------------------------
    # ---------------------------------Tworze adres agregacji--------------------------------------------
    adres_Agregacja = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, blad + 1):  # przypisuje do adres_Agregacja pierwsze adres na liscie do "n" bitu
        adres_Agregacja[i] = listy_ip_dec[0][i]

    adres_Agregacja = [str(i) for i in adres_Agregacja]  # konwwersja z int na string w celu zamiany bin na adres ip
    print("Adres Nadsieci w formie binarnej : ")
    print(''.join(adres_Agregacja))
    print()
    print("Adres Nadsieci w formie decymenalnej : ")
    print(ip_format(''.join(adres_Agregacja)) + "/" + str(i))
    adres_Agregacja_str = ip_format(''.join(adres_Agregacja)) + "/" + str(i)

    # ---------------------------------Zapis do pliku-----------------------------------------------------
    zapis_do_pliku(filepath_1, adres_Agregacja_str)
    # ---------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------PLIK 1-------------------------------------------------------------------------------------

# -----------------------------------------------------PLIK 2-------------------------------------------------------------------------------------
if (ilosc_arg == 3):
    filepath_2 = sys.argv[2]
    print()
    print("------------OBLICZANIE AGREGACJI Z PLIKU NR 2--------------")

    f = open(filepath_2, "r", encoding="utf-8").read()
    lines_1 = f.split('\n')  # całą treść pliku musimy podzielić przez nową linię („\n”) i wiersze zapisać do tablicy.
    ilosc_lini = 0  # zmienna pomocnicza do liczenia lini w pliku

    for line in lines_1:  # zliczam ilosc lini w pliku
        ilosc_lini = ilosc_lini + 1
    print()
    print("Ilosc adresow w pliku :", end="")
    print(ilosc_lini)

    listy_ip_dec_2 = [[] for i in range(ilosc_lini)]  # tworze dynamicznie liste w liscie
    listy_ip_int_2 = [[] for i in range(ilosc_lini)]  # tworze dynamicznie liste w liscie

    print()
    ilosc_lini_tmp = 0  # zmienna pomocnicza do indeksowania list
    for line in lines_1:
        listy_ip_dec_2[ilosc_lini_tmp] = ip2bin(line)
        ilosc_lini_tmp = ilosc_lini_tmp + 1
    '''
    print("Adresy IP pliku nr 2 przed sortowaniowaniem:")
    ilosc_lini_tmp_1 = 0  # wypisywanie listy
    for line in lines_1:
        print(listy_ip_dec_2[ilosc_lini_tmp_1])
        ilosc_lini_tmp_1 = ilosc_lini_tmp_1 + 1
    print()
    '''
    listy_ip_dec_2.sort()
    print("Adresy IP pliku nr 2 po sortowaniu:")
    ilosc_lini_tmp_1 = 0  # wypisywanie listy
    for line in lines_1:
        print(listy_ip_dec_2[ilosc_lini_tmp_1])
        ilosc_lini_tmp_1 = ilosc_lini_tmp_1 + 1

    # ----------------------------------konwersja str na int---------------------------------------
    ilosc_lini_tmp_2 = 0  # wypisywanie listy
    for line in lines_1:
        listy_ip_int_2[ilosc_lini_tmp_2] = int(listy_ip_dec_2[ilosc_lini_tmp_2])
        ilosc_lini_tmp_2 = ilosc_lini_tmp_2 + 1
    # ---------------------------------------------------------------------------------------------------------------
    # ---------------------------------sprawdzam czy duplikuja sie adresy IP w pliku-----------------------------
    print()
    spraw_ip_dupl(listy_ip_int_2)
    # ---------------------------------sprawdzam spojnosci adresow ip-----------------------------
    spoj_adresacji(listy_ip_dec_2)
    print()

    # ---------------------------------------------------------------------------------------------------------------
    # ---------------------------------XOR - znajdywanie roznic ----------------------------------------
    blad = (myfunc(listy_ip_dec_2))
    # print(blad)
    # ---------------------------------------------------------------------------------------------------------------
    # ---------------------------------Tworze adres agregacji--------------------------------------------
    adres_Agregacja = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, blad + 1):  # przypisuje do adres_Agregacja pierwsze adres na liscie do "n" bitu
        adres_Agregacja[i] = listy_ip_dec_2[0][i]

    adres_Agregacja = [str(i) for i in adres_Agregacja]  # konwwersja z int na string w celu zamiany bin na adres ip
    print("Adres Nadsieci w formie binarnej : ")
    print(''.join(adres_Agregacja))
    print()
    print("Adres Nadsieci w formie decymenalnej : ")
    print(ip_format(''.join(adres_Agregacja)) + "/" + str(i))
    adres_Agregacja_str = ip_format(''.join(adres_Agregacja)) + "/" + str(i)

    # ---------------------------------Zapis do pliku-----------------------------------------------------
    zapis_do_pliku(filepath_2, adres_Agregacja_str)
    # ---------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------

# -----------------------------------------------------SPRAWDZANIE PLIKOW-------------------------------------------------------------------------------------
if (ilosc_arg == 3):
    print()
    print()
    print("------------SPRAWDZANIE DUPLIKATOW POMIEDZY PLIKAMI--------------")
    print()
    listy_ip_int_pliki = []
    listy_ip_int_pliki = listy_ip_int + listy_ip_int_2

    ilosc_lini_tmp_1 = 0  # wypisywanie listy
    ilosc_linii_tmp_pliki = len(listy_ip_int_pliki)
    for line in range(0, ilosc_linii_tmp_pliki):
        print(listy_ip_int_pliki[ilosc_lini_tmp_1])
        ilosc_lini_tmp_1 = ilosc_lini_tmp_1 + 1

    # ---------------------------------sprawdzam czy duplikuja sie adresy IP w pliku-----------------------------
    print()
    D = defaultdict(list)
    for i, item in enumerate(listy_ip_int_pliki):
        D[item].append(i)
    D = {k: v for k, v in D.items() if len(v) > 1}
    if D:
        print("Bład : duplikuje sie adres IP pomiedzy plikami")
        print(D)
        print()
    else:
        print("Nie ma duplikacji adresow IP")
        print()
    # -----------------------------------------------------SPRAWDZANIE PLIKOW-------------------------------------------------------------------------------------
else:
    print()
    print("Potrzebna 2 pliki w celu porównania duplikacji pomiedzy plikami")