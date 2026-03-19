import time
import random

print("welcome to blackjack")


def draw_card():
    deck = [1,11,2,3,4,5,6,7,8,9,10,10,10,10]

    random_card = random.choice(deck)

    return random_card

player_hand = [draw_card(),draw_card()]

print(f"your hand is a {player_hand}")

house_hand = [draw_card(),draw_card()]

print(f"the hose has a {player_hand[0]} and a misterious card")

hit = str(input("Would u like to hit: "))

while hit == "yes":

    total_score = 0

    player_hand.append(draw_card())

    print(player_hand)

    for card in player_hand:
        total_score += card

    print(total_score)

    time.sleep(1)



    if total_score  > 21 :
            print(f"BUSTED you loose final score was {total_score}")

            break

    elif total_score == 21:
            print(f"BLACKJACK lets wait for the house to reveal")

            hit == "no"

    else:
          hit = str(input("would you like to hit again: "))


print(f"the house reveals a {house_hand}")


house_total = 0
       
    
while house_total < 17:
      
      
      house_hand.append(draw_card())

      for card in house_hand:
            house_total+=card

            print(f"house total is {house_total}")

      if house_total > 21:
            print("The house busted")

            break
      
      elif house_total == 21:
            print("blackjack")

   

        




