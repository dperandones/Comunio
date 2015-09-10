#!/usr/bin/python
# -*- coding: utf-8 -*-
import pp
from Comuniazo import Comuniazo
c = Comuniazo.new()
c.load_jornada()
c.load_players()
pp c.jornada
