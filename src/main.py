import os

import pygame

from garage import Garage
from constants import *

if not os.path.isfile(RECORDS):
	open(RECORDS, 'w').close()
pygame.init()
g = Garage()
g.menu()
