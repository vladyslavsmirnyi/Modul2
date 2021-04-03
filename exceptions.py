"""Game exceptions."""
import datetime
import os

import settings


class GameOver(Exception):
    """An exception that indicates game ending after player lost all his lives."""
    @staticmethod
    def save_score(player_name, score_value):
        score = Score(player_name, score_value, datetime.datetime.today())
        scores = GameOver.load_scores()
        scores.append(score)
        scores = sorted(scores, reverse=True)
        scores = scores[:10]
        GameOver._save_scores(scores)

    @staticmethod
    def _save_scores(scores):
        with open("scores.txt", "w") as file:
            for i in range(len(scores)):
                position = i + 1
                score = scores[i]
                file.write(str(position) + ". " + str(score) + "\n")

    @staticmethod
    def load_scores():
        scores = []

        if os.path.isfile(settings.SCORES_FILENAME):
            with open(settings.SCORES_FILENAME, "r") as file:
                for line in file:
                    line = line.strip()
                    if len(line) == 0:
                        continue

                    score_string = line.split(". ")[1]
                    splitted_line = score_string.split(" | ")
                    player_name, score_value = splitted_line[0].split(" : ")
                    score_value = int(score_value)
                    score_datetime = datetime.datetime.strptime(
                        splitted_line[1], settings.DATETIME_FORMAT)
                    score = Score(player_name, score_value, score_datetime)
                    scores.append(score)

        return scores


class Score:
    """A class to store players score."""
    def __init__(self, player_name, score_value, score_datetime):
        self.player_name = player_name
        self.score_value = score_value
        self.score_datetime = score_datetime

    def __repr__(self):
        return f"{self.player_name} : {self.score_value} | " + \
               self.score_datetime.strftime(settings.DATETIME_FORMAT)

    def __lt__(self, other):
        return self.score_value < other.score_value

    def __le__(self, other):
        return self.score_value <= other.score_value

    def __gt__(self, other):
        return self.score_value > other.score_value

    def __ge__(self, other):
        return self.score_value >= other.score_value

    def __eq__(self, other):
        return self.score_value == other.score_value

    def __ne__(self, other):
        return not self.__eq__(other)


class EnemyDown(Exception):
    """An exception that indicates enemy defeat."""
    pass
