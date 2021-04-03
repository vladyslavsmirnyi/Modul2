from exceptions import GameOver, EnemyDown
from models import Player, Enemy


def play():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    level = 1
    enemy = Enemy(level)
    score_value = 0

    while True:
        try:
            player.attack(enemy)
            player.defense(enemy)
        except EnemyDown:
            level += 1
            enemy = Enemy(level)
            score_value += 5
            print(f"\nEnemy defeated! Your score: {score_value}. Next enemy level: {level}.")
        except GameOver as e:
            e.save_score(player_name, score_value)
            print("\nGame over!")
            break


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
