"""Main game module."""
from exceptions import GameOver, EnemyDown
from models import Player, Enemy
import settings


def play():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    level = 1
    enemy = Enemy(level)
    score_value = 0

    while True:
        try:
            if player.attack(enemy):
                score_value += 1
            player.defense(enemy)
        except EnemyDown:
            level += 1
            enemy = Enemy(level)
            # 5 scores for enemy defeat + 1 score for the last attack before defeat
            score_value += 6
            print(f"\nEnemy defeated! Your score: {score_value}. Next enemy level: {level}.")
        except GameOver as exception:
            exception.save_score(player_name, score_value)
            print(f"\nGame over! Your score is: {score_value}")
            break
        except KeyboardInterrupt:
            GameOver.save_score(player_name, score_value)
            print(f"\nGame interrupted! Your score is: {score_value}")
            break


if __name__ == "__main__":
    try:
        while True:
            command = input("\nEnter your command: ")
            if command == "start":
                play()
            elif command == "exit":
                raise KeyboardInterrupt()
            elif command == "show scores":
                scores = GameOver.load_scores()
                for i in range(len(scores)):
                    print(f"{i+1}. {scores[i]}")
            elif command == "help":
                print("Supported commands:", ", ".join(settings.SUPPORTED_COMMANDS))
            else:
                print("Unknown command!")
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
