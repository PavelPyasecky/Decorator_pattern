from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):

    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):

    def get_positive_effects(self):
        pos_ef = self.base.get_positive_effects()
        pos_ef.append(type(self).__name__)
        return pos_ef

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats()
        for x in ["Strength", "Endurance", "Agility", "Luck"]:
            stats[x] += 7

        for x in ["Perception", "Charisma", "Intelligence"]:
            stats[x] -= 3

        stats["HP"] += 50

        return stats


class Blessing(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats()
        for x in ["Strength", "Endurance", "Agility", "Luck", "Perception", "Charisma", "Intelligence"]:
            stats[x] += 2

        return stats


class AbstractNegative(AbstractEffect):

    def get_negative_effects(self):
        neg_ef = self.base.get_negative_effects()
        neg_ef.append(type(self).__name__)
        return neg_ef

    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Weakness(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        for x in ["Strength", "Endurance", "Agility"]:
            stats[x] -= 4

        return stats


class EvilEye(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10

        return stats


class Curse(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        for x in ["Strength", "Endurance", "Agility", "Luck", "Perception", "Charisma", "Intelligence"]:
            stats[x] -= 2

        return stats


if __name__ == '__main__':
    hero = Hero()
    print(hero.get_negative_effects())
    print(hero.get_positive_effects())
    print(hero.get_stats())
    print('-' * 50)

    bers1 = Berserk(hero)
    print(bers1.get_negative_effects())
    print(bers1.get_positive_effects())
    print(bers1.get_stats())
    print('-' * 50)

    bers2 = Berserk(bers1)
    print(bers2.get_negative_effects())
    print(bers2.get_positive_effects())
    print(bers2.get_stats())
    print('-' * 50)

    bers2.base = bers2.base.base
    print(bers2.get_negative_effects())
    print(bers2.get_positive_effects())
    print(bers2.get_stats())
    print('-' * 50)
