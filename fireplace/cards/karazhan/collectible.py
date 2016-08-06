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


class ONK_6:
	"Malchezaar's Imp"
	events = Discard(FRIENDLY).on(Draw(CONTROLLER))


class ONK_7:
	"Babbling Book"
	play = Give(CONTROLLER, RandomSpell(card_class = CardClass.MAGE))


class ONK_8:
	"Book Wyrm"
	powered_up = HOLDING_DRAGON
	play = powered_up & Destroy(TARGET)


class ONK_9:
	"Moroes"
	events = OWN_TURN_END.on(Summon(CONTROLLER, "ONK_9t"))


class ONK_13:
	"Zoobot"
	play = (
		Buff(RANDOM_FRIENDLY_MINION + BEAST, "ONK_13e"),
		Buff(RANDOM_FRIENDLY_MINION + DRAGON, "ONK_13e"),
		Buff(RANDOM_FRIENDLY_MINION + MURLOC, "ONK_13e")
	)

ONK_13e = buff(+1, +1)


class ONK_14:
	"Medivh, the Guardian"
	play = Summon(CONTROLLER, "ONK_14w")


class ONK_15:
	"Silverware Golem"
	events = Discard(SELF).on(Summon(CONTROLLER, SELF))


class ONK_16:
	"Netherspite Historian"
	powered_up = HOLDING_DRAGON
	play = powered_up & DISCOVER(RandomDragon())


class ONK_19:
	"Violet Illusionist"
	events = (
		OWN_TURN_BEGIN.on(Refresh(FRIENDLY_HERO, {GameTag.CANT_BE_DAMAGED: True})),
		OWN_TURN_END.after(Refresh(FRIENDLY_HERO, {GameTag.CANT_BE_DAMAGED: False}))
	)


class ONK_20:
	"Arcane Giant"
	#cost_mod = -Attr(CONTROLLER, GameTag.NUM_SPELLS_PLAYED_THIS_GAME)


class ONK_21:
	"Arcanosmith"
	play = Summon(CONTROLLER, "ONK_21t")


class ONK_22:
	"Menagerie Magician"
	play = (
		Buff(RANDOM_FRIENDLY_MINION + BEAST, "ONK_22e"),
		Buff(RANDOM_FRIENDLY_MINION + DRAGON, "ONK_22e"),
		Buff(RANDOM_FRIENDLY_MINION + MURLOC, "ONK_22e")
	)

ONK_22e = buff(+2, +2)


class ONK_23:
	"Moat Lurker"
	play = Destroy(TARGET)
	deathrattle = Summon(TARGET)


class ONK_24:
	"Avian Watcher"
	play = Find(FRIENDLY_SECRETS) & Buff(SELF, "ONK_24e")

ONK_24e = buff(+1, +1, taunt=True)


##
# Spells

class ONK_4:
	"Firelands Portal"
	play = Hit(TARGET, 5), Summon(CONTROLLER, RandomMinion(cost=5))


class ONK_10:
	"Protect The King!"
	play = Summon(CONTROLLER, "ONK_10t") * Count(ENEMY_MINIONS)


class ONK_12:
	"Kara Kazham!"
	play = (
		Summon(CONTROLLER, "ONK_12ta"),
		Summon(CONTROLLER, "ONK_12tb"),
		Summon(CONTROLLER, "ONK_12tc")
	)


class ONK_18:
	"Moonglade Portal"
	play = Heal(TARGET, 6), Summon(CONTROLLER, RandomMinion(cost=6))


##
# Weapons

class ONK_14w:
	"Atiesh"
	events = OWN_SPELL_PLAY.on(
		Summon(CONTROLLER, RandomMinion(cost=Attr(Play.CARD, GameTag.COST))),
		Hit(SELF, 1)
	)


class ONK_17:
	"Fool's Bane"
	play = Buff(CONTROLLER, "ONK_17o")

class ONK_17o:
	update = (
		Refresh(FRIENDLY_WEAPON, {GameTag.CANT_EXHAUST: True}),
		Refresh(FRIENDLY_WEAPON, {GameTag.CANNOT_ATTACK_HEROES: True})
	)
	events = Death(FRIENDLY_WEAPON).on(Destroy(SELF))
