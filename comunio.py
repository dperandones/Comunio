#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
pp = pprint.PrettyPrinter(indent=4)
from Comuniazo import Comuniazo
c = Comuniazo()
c.load_jornada()
c.load_players()
pp.pprint(c.jornada)
