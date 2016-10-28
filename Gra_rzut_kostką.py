import random
import time
import turtle as t
import tkinter,sys
import tkinter.messagebox
from tkinter import *







class Rzut:


    def rzuc_kostka(self):

        ile_oczek = random.randint(1,6)
        return ile_oczek

class Zawodnik:
    ile_punktow = 0
    bilans_zwyciestw = 0


    def tura(self):
        ile_punktow = 0
        ile_punktow+=Rzut().rzuc_kostka()
        ile_punktow+=Rzut().rzuc_kostka()
        return ile_punktow

class Panel:

    def rozegraj(self,z1,z2):


        zawodnik1 = z1.tura()
        zawodnik2 = z2.tura()

        print("Zawodnik 1: ",zawodnik1)
        time.sleep(1)
        print("Zawodnik 2: ",zawodnik2)
        time.sleep(1)

        if(zawodnik1 > zawodnik2):
            z1.bilans_zwyciestw+=1
            print("Wygrywa zawodnik nr 1")
        elif(zawodnik1 < zawodnik2):
            z2.bilans_zwyciestw+=1
            print("Wygrywa zawodnik nr 2")
        else:
            z1.bilans_zwyciestw+=1
            z2.bilans_zwyciestw+=1
            print("Jest Remis Wiiiiii !!!!")
        print("Bilans wygranych : ",z1.bilans_zwyciestw," : ",z2.bilans_zwyciestw)
    def sprawdz_stan(self,ile):

        for i in range(0, ile):
            panel.rozegraj(z1, z2)
            print()
            time.sleep(1)

        while True:
            if (z1.bilans_zwyciestw == z2.bilans_zwyciestw):
                panel.rozegraj(z1, z2)
            elif (z1.bilans_zwyciestw != z2.bilans_zwyciestw):
                break

    def wprowadzenie(self):
        print(
            "wprowadz \"tak\" jeśli chcesz wprowadzic ilosc tur do wykonania lub wprowadz \"nie\" jesli chcesz sam zakonczyc gre :")
        pytanie = input()

        if (pytanie == "tak"):
            print("wprowadz ile tur ma sie rozegrac : ")
            ile = int(input())
            panel.sprawdz_stan(ile)
        elif (pytanie == "nie"):
            print("Gramy \"tak\" \\ \"nie\"")
            gramy = input()
            while gramy == "tak":
                panel.rozegraj(z1, z2)
                print("Gramy dalej ? \"tak\" \\ \"nie\"")
                gramy = input()

        else:
            print("cos poszlo nie tak !!!")



z1 = Zawodnik()
z2 = Zawodnik()
panel = Panel()
panel.wprowadzenie()























