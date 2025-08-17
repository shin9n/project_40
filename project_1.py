import random

random_number = random.randint(1, 100)

game_count = 1

while True:
    try:
        my_number = int(input("1~100 사이의 숫자를 입력하세요: "))
        if my_number > random_number:
            print("down")
        elif my_number < random_number:
            print("up")
        elif my_number == random_number:
            print(f"정답입니다! {game_count}번 만에 맞추셨습니다.")
            break   
        game_count += 1
    except:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        
        