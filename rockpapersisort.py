import random


moves = ["rock", "paper", "scissors"]


player_history = {"rock": 0, "paper": 0, "scissors": 0}

def predict_move():
    if sum(player_history.values()) == 0:
        return random.choice(moves)
    most_common = max(player_history, key=player_history.get)

    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"


def get_player_move():
    while True:
        move = input("Enter your move (rock, paper, or scissors): ").lower()
        if move in moves:
            return move
        print("Invalid move. Try again.")


def get_ai_move(strategy="random"):
    if strategy == "predict":
        return predict_move()
    return random.choice(moves)


def determine_winner(player, ai):
    if player == ai:
        return "tie"
    elif (player == "rock" and ai == "scissors") or \
         (player == "scissors" and ai == "paper") or \
         (player == "paper" and ai == "rock"):
        return "player"
    else:
        return "ai"


def play_game():
    player_score = 0
    ai_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    strategy = input("Use smart AI? (yes/no): ").lower()

    while True:
        player_move = get_player_move()
        player_history[player_move] += 1

        ai_move = get_ai_move("predict" if strategy == "yes" else "random")
        print(f"AI chose: {ai_move}")

        result = determine_winner(player_move, ai_move)
        if result == "player":
            print("You win this round!")
            player_score += 1
        elif result == "ai":
            print("AI wins this round!")
            ai_score += 1
        else:
            print("It's a tie!")

        print(f"Score -> You: {player_score} | AI: {ai_score}")

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

play_game()