"""Main game classes."""
import random
from enum import Enum

from exceptions import EnemyDown, GameOver
import settings


class Attack(Enum):
    WIZARD = 1
    WARRIOR = 2
    BANDIT = 3


class Enemy:
    """A class to stores enemy's data."""
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return Attack(random.randint(1, 3))

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()


class Player:
    """A class to stores player's data and calculate attack result."""
    def __init__(self, name,):
        self.name = name
        self.lives = settings.PLAYER_LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        is_success = (attack is Attack.WIZARD and defense is Attack.WARRIOR) or \
                     (attack is Attack.WARRIOR and defense is Attack.BANDIT) or \
                     (attack is Attack.BANDIT and defense is Attack.WIZARD)
        if is_success:
            return 1

        if attack is defense:
            return 0

        return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver()

    def attack(self, enemy_obj):
        player_attack = Player._get_player_move(True)
        enemy_defense = enemy_obj.select_attack()
        result = Player.fight(player_attack, enemy_defense)

        if result == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            return True

        if result == 0:
            print("It's a draw!")
        else:
            print("You missed!")

        return False

    def defense(self, enemy_obj):
        enemy_attack = enemy_obj.select_attack()
        player_defense = Player._get_player_move(False)
        result = Player.fight(enemy_attack, player_defense)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        else:
            print("Enemy missed!")

    @staticmethod
    def _get_player_move(is_attack):
        move_name = "attack" if is_attack else "defense"
        while True:
            move = input(
                "Enter your " + move_name + " (1/'WIZARD', 2/'WARRIOR', 3/'BANDIT'): ").upper()
            if move in ["1", "2", "3"]:
                move = Attack(int(move))
                break
            if move in ["WIZARD", "WARRIOR", "BANDIT"]:
                move = Attack[move.upper()]
                break
            print("Incorrect value!")
        return move
