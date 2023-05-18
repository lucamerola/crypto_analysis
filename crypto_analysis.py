#!/usr/bin/python3
# -*- Coding: UTF-8 -*-
#-------------------------------
# Created By: Luca Merola
# Created Date: 18/05/2023
# Version='1.0'
# Github: lucamerola
# ------------------------------

from base64 import b64decode
import urllib.parse
import re

def main():
    while True:
        print("\n---Menu---\n1 - Converti dati binari in ascii\n2 - Decode base64\n3 - Converti morse in ascii\n4 - URL Decoding\n5 - Esci")
        opzione=input("Scegli: ")
        try:
            opzione = int(opzione)
        except Exception:
            print("Devi inserire un valore intero")
            continue

        if opzione==1:
            binario_ascii()
        elif opzione==2:
            decode_base64()
        elif opzione==3:
            morse_italiano()
        elif opzione==4:
            urldecoding()
        elif opzione==5:
            exit()
        else:
            continue

def binario_ascii():
    stringa_analizzare = input("Valore: ")
    rappresentazione_intero = int(stringa_analizzare,2)
    #rappresentazione big endian
    rappresentazione_binaria = rappresentazione_intero.to_bytes((rappresentazione_intero.bit_length() + 7) // 8, 'big')
    stringa_decodificata = rappresentazione_binaria.decode(encoding='utf-8')
    print("\nRappresentazione: Big-endian\nDecodifica: utf-8\nTesto decodificato: {}".format(stringa_decodificata))
    #rappresentaizone little endian
    rappresentazione_binaria = rappresentazione_intero.to_bytes((rappresentazione_intero.bit_length() + 7) // 8, 'little')
    stringa_decodificata = rappresentazione_binaria.decode(encoding='utf-8')
    print("\nRappresentazione: Little-endian\nDecodifica: utf-8\nTesto decodificato: {}\n".format(stringa_decodificata))
    return

def decode_base64():
    stringa_analizzare = input("Valore: ")
    if(verifica_base64(stringa_analizzare)):
        print("\nStringa codificata in base64")
    else:
        print("\nStringa non codificata in base64")
        return
    byte_stringa = b64decode(stringa_analizzare)
    stringa_decodificata = byte_stringa.decode(encoding='latin-1')
    print("Decodifica: latin-1\nTesto decodificato: {}\n".format(stringa_decodificata))
    return

def verifica_base64(testo_codificato):
    x = re.search("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$", testo_codificato)
    return x

def morse_italiano():
    MORSE_CODE_DICT2 = { '.-': 'a', '-...':'b',
                    '-.-.':'c', '-..':'d', '.':'e',
                    '..-.':'f', '--.':'g', '....':'h',
                    '..':'i', '.---':'j', '-.-':'k',
                    '.-..':'l', '--':'m', '-.':'n',
                    '---':'o', '.--.':'p', '--.-':'q',
                    '.-.':'r', '...':'s', '-':'t',
                    '..-':'u', '...-':'v', '.--':'w',
                    '-..-':'x', '-.--':'y', '--..':'z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':', ', '.-.-.-':'.',
                    '..--..':'?', '-..-.':'/', '-....-':'-',
                    '-.--.':'(', '-.--.-':')'}
    stringa_analizzare = input("Valore: ")
    parole_analizzare = stringa_analizzare.split(" ")
    stringa_finale = ""
    for parola in parole_analizzare:
        stringa_finale+=MORSE_CODE_DICT2[parola]+" "
    print("\nMorse: {}".format(stringa_finale[:-1]))
    return

def urldecoding():
    stringa_analizzare = input("Valore: ")
    stringa_decodificata = urllib.parse.unquote_plus(string=stringa_analizzare,encoding="latin-1")
    print("\nDecodifica: latin-1\nTesto decodificato: {}".format(stringa_decodificata))
    return

if __name__ == "__main__":
    main()