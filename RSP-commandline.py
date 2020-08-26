import time
import random

def pcChoice():
    rsp = ["rock","scissers","paper"]
    random.shuffle(rsp)
    pc = random.choice(rsp)
    return pc

print("""Hi
welcome to Rock Scissers Paper
(q) for Exit
good lock:)""")
status = "play"
pcScore = 0
playerScore = 0

while True:

    print("---------------------")
    print("Rock...")
    print("Scissers...")
    print("Paper...")
    print(f"player: {playerScore} computer: {pcScore}")
    print("---------------------")

    player = input("choice your move:").lower()

    if player != "q":
        pcMove = pcChoice()
        if player[0] == pcMove[0]: #** player and pc are same. no body won
            print("oh.you are choice same move!")
            print(f"computer choice wad {pcMove}")
        elif player[0] == "r" and pcMove[0] == "s": #** player rock. pc scissers. player won
            print("yoho.you won...")
            print(f"computer choice wad {pcMove}")
            playerScore += 1
        elif player[0] == "r" and pcMove[0] == "p": #** player rock. pc paper. pc won
            print("oh no.computer won:(")
            print(f"computer choice wad {pcMove}")
            pcScore += 1
        elif player[0] == "s" and pcMove[0] == "r": #** player scissers. pc rock. pc won
            print("oh no.computer won:(")
            print(f"computer choice wad {pcMove}")
            pcScore += 1
        elif player[0] == "s" and pcMove[0] == "p": #** player scissers. pc paper. player won
            print("yoho.you won...")
            print(f"computer choice wad {pcMove}")
            playerScore += 1
        elif player[0] == "p" and pcMove[0] == "r": #** player paper. pc rock. player won
            print("yoho.you won...")
            print(f"computer choice wad {pcMove}")
            playerScore += 1
        elif player[0] == "p" and pcMove[0] == "s": #** player paper. pc scissers. pc won
            print("oh no.computer won:(")
            print(f"computer choice wad {pcMove}")
            pcScore += 1

    else:
        break

print("godbye:)")