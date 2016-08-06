from ..utils import *


##
# Minions

class ONK_1:
	"The Curator"
	play = (
		Find(FRIENDLY_DECK + BEAST) &
		ForceDraw(RANDOM(FRIENDLY_DECK + BEAST))
	), (
		Find(FRIENDLY_DECK + DRAGON) &
		ForceDraw(RANDOM(FRIENDLY_DECK + DRAGON))
	), (
		Find(FRIENDLY_DECK + MURLOC) &
		ForceDraw(RANDOM(FRIENDLY_DECK + MURLOC))
	)


##
# Spells


##
# Weapons
