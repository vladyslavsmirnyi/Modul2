import datetime
import os

import settings


class GameOver(Exception):
    def save_score(self, player_name, score_value):
        score = Score(player_name, score_value, datetime.datetime.today())
        scores = self._load_scores()
        scores.append(score)
        scores = sorted(scores, reverse=True)
        scores = scores[:10]
        self._save_scores(scores)

    def _save_scores(self, scores):
        with open("scores.txt", "w") as f:
            for i in range(len(scores)):
                position = i + 1
                score = scores[i]
                f.write(str(position) + ". " + str(score) + "\n")

    def _load_scores(self):
        scores = []

        if os.path.isfile(settings.SCORES_FILENAME):
            with open(settings.SCORES_FILENAME, "r") as f:
                for line in f:
                    line = line.strip()
                    if len(line) == 0:
                        continue

                    score_string = line.split(". ")[1]
                    splitted_line = score_string.split(" | ")
                    player_name, score_value = splitted_line[0].split(" : ")
                    score_value = int(score_value)
                    score_datetime = datetime.datetime.strptime(splitted_line[1], settings.DATETIME_FORMAT)
                    score = Score(player_name, score_value, score_datetime)
                    scores.append(score)

        return scores


class Score:
    def __init__(self, player_name, score_value, score_datetime):
        self.player_name = player_name
        self.score_value = score_value
        self.score_datetime = score_datetime

    def __repr__(self):
        return f"{self.player_name} : {self.score_value} | " + self.score_datetime.strftime(settings.DATETIME_FORMAT)

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
    pass
