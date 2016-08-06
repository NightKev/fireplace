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


class ONK_2:
	"Ethereal Peddler"
	play = Buff(FRIENDLY_HAND + CLASS_CARD - FRIENDLY_CLASS, "ONK_2e")

class ONK_2e:
	events = REMOVED_IN_PLAY
	tags = {GameTag.COST: -2}


class ONK_5:
	"Kindly Grandmother"
	deathrattle = Summon(CONTROLLER, "ONK_5t")


##
# Spells

class ONK_4:
	"Firelands Portal"
	play = Hit(TARGET, 5), Summon(CONTROLLER, RandomMinion(cost=5))


##
# Weapons
