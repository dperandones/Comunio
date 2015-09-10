#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import requests
from bs4 import BeautifulSoup
headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0'}

class Comuniazo:
    def __init__(self):
        self.jornada = []

    def load_jornada(self):
        req = requests.post("http://www.comuniazo.com/",headers=headers).content
        bs = BeautifulSoup(req,"lxml")
        matches = bs.findAll("div",{"class":"partido"})
        for match in matches:
            partido = {}
            partido["casa"] = match.find("div",{"class":"casa"}).find("i")["class"][0].replace("spr-","")
            partido["fuera"] = match.find("div",{"class":"fuera"}).find("i")["class"][0].replace("spr-","")
            partido["url"] = match.find("a",{"class":"match"})["href"]
            partido["fecha"] = match.find("div",{"class":"fecha"}).text
            try:
                partido["resultado"] = match.find("div",{"class":"score"}).text
            except:
                partido["resultado"] = ""
            try:
                partido["1"] = float(match.find("a",{"class":"odd-1"}).text.replace("1 • ",""))
                partido["x"] = float(match.find("a",{"class":"odd-x"}).text.replace("X • ",""))
                partido["2"] = float(match.find("a",{"class":"odd-2"}).text.replace("2 • ",""))
            except:
                partido["1"] = 0.0
                partido["x"] = 0.0
                partido["2"] = 0.0
            partido["objeto"] = match
            self.jornada.append(partido)
        return self.jornada
    def load_players(self):
        for partido in self.jornada:
            req = requests.get(partido["url"],headers=headers).content
            bs = BeautifulSoup(req,"lxml")

            partido["jugadores_casa"] = []
            partido["jugadores_fuera"] = []
            if bs.select(".content > .group > .col")[0].text.find("no disponible") >= 0:
                print("imposible importar jugadores casa")
            else:
                casa = bs.select(".content > .group > .col")[0]
                for player in casa.find_all("tr",{"class":None}):
                    if(len(player.find_all("td"))>3):
                        new_player = {
                            "position" : player.find_all("td")[0].text,
                            "nombre" : player.find_all("td")[1].text,
                            "puntos_casa" : player.find_all("td")[2].text,
                            "media_casa" : player.find_all("td")[3].text
                        }
                    else:
                        new_player = {
                            "position" : player.find_all("td")[0].text,
                            "nombre" : player.find_all("td")[1].text,
                            "puntos_jornada" : player.find_all("td")[2].text
                        }
                    partido["jugadores_casa"].append(new_player)
            if bs.select(".content > .group > .col")[2].text.find("no disponible") >= 0:
                print("imposible importar jugadores fuera")
            else:
                fuera = bs.select(".content > .group > .col")[2]
                for player in fuera.find_all("tr",{"class":None}):
                    if(len(player.find_all("td"))>3):
                        new_player = {
                            "position" : player.find_all("td")[0].text,
                            "nombre" : player.find_all("td")[1].text,
                            "puntos_fuera" : player.find_all("td")[2].text,
                            "media_fuera" : player.find_all("td")[3].text
                        }
                    else:
                        new_player = {
                            "position" : player.find_all("td")[0].text,
                            "nombre" : player.find_all("td")[1].text,
                            "puntos_jornada" : player.find_all("td")[2].text
                        }
                    partido["jugadores_fuera"].append(new_player)
