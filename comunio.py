#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
import time
from Comuniazo import Comuniazo
equipos = {"athletic":"1","atletico":"2","barcelona":"3","betis":"4","celta":"5","deportivo":"6","eibar":"24","espanyol":"7","getafe":"8","granada":"9","las-palmas":"27","levante":"10","malaga":"11","rayo":"14","rayo-vallecano":"14","real-madrid":"15","real-sociedad":"16","sevilla":"17","sporting":"26","valencia":"18","villarreal":"22"}



pp = pprint.PrettyPrinter(indent=4)
c = Comuniazo()
c.load_jornada()
c.load_players()





print "Content-type: text/html"
print ""
print ""
print "<html><head></head><style>.equipo{float: left}</style><body>"

for partido in c.jornada:
	print "<div class='partido'>"
	print "<div class='equipo casa'>"
	print "<img src='http://www.futbolfantasy.com/uploads/images/alineaciones/" + equipos[partido["casa"]] + ".jpg?v=" +  str(time.time()) + "'>"
	print "<table>"
	for jugador in partido["jugadores_casa"]:
		print "<tr>"
        if len(jugador)==3:
            print "<td>" + jugador["nombre"].encode("utf-8") +"</td>" + "<td>" + jugador["posicion"].encode("utf-8") +"</td>" + "<td>" + jugador["puntos_jornada"].encode("utf-8") +"</td>"
        elif len(jugador)==4:
            print "<td>" + jugador["nombre"].encode("utf-8") +"</td>" + "<td>" + jugador["posicion"].encode("utf-8") +"</td>" + "<td>" + jugador["puntos_casa"].encode("utf-8") +"</td>" + jugador["media_casa"].encode("utf-8") +"</td>"
        else:
            print "<td>Algo estás haciendo mal</td>"
        print "</tr>"
	print "</table>"
	print "</div>"
	print "<div class='equipo fuera'>"
	print "<img src='http://www.futbolfantasy.com/uploads/images/alineaciones/" + equipos[partido["fuera"]] + ".jpg?v=" +  str(time.time()) + "'>"
	print "<table>"
	for jugador in partido["jugadores_fuera"]:
		print "<tr>"
        if len(jugador)==3:
            print "<td>" + jugador["nombre"].encode("utf-8") +"</td>" + "<td>" + jugador["posicion"].encode("utf-8") +"</td>" + "<td>" + jugador["puntos_jornada"].encode("utf-8") +"</td>"
        elif len(jugador)==4:
            print "<td>" + jugador["nombre"].encode("utf-8") +"</td>" + "<td>" + jugador["posicion"].encode("utf-8") +"</td>" + "<td>" + jugador["puntos_fuera"].encode("utf-8") +"</td>" + jugador["media_fuera"].encode("utf-8") +"</td>"
        else:
            print "<td>Algo estás haciendo mal</td>"
        print "</tr>"
	print "</table>"
	print "</div>"
	print "</div>"
	print "<div class='clear'></div>"

print "</body></html>"
