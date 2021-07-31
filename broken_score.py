def is_score():
    score = float(input("Please enter your score: "))
    if score < 0 and score >= 100:
        print(f"Invalid number")
    elif score > 20 and score < 50:
        print(f"Bad")
    elif score == 50:
        print(f"Passable")
    elif score >= 90:
        print(f"Excellet")
    elif score < 10:
        print(f"Very Bad")






is_score()