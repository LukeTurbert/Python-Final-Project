import random
roll = [1, 2, 3, 4, 5]
rollTotal = sum(roll)
roll = sorted(roll)
total = 0
count = 0
yahtzee = 0
threeOfAKind = 0
fourOfAKind = 0
fullHouse = 0

#scorecard player 1
oneScore = 0
twoScore = 0
threeScore = 0
fourScore = 0
fiveScore = 0
sixScore = 0
threeOfAKindScore = 0
fourOfAKindScore = 0
fullHouseScore = 0
smallStraightScore = 0
largeStraightScore = 0
chanceScore = 0
yahtzeeScore = 0

#scorecard player 2
oneScore2 = 0
twoScore2 = 0
threeScore2 = 0
fourScore2 = 0
fiveScore2 = 0
sixScore2 = 0
threeOfAKindScore2 = 0
fourOfAKindScore2 = 0
fullHouseScore2 = 0
smallStraightScore2 = 0
largeStraightScore2 = 0
chanceScore2 = 0
yahtzeeScore2 = 0

#allows for 13 rounds
for turn in range (1, 14):
    print("Player 1")
    print("You are on round", turn)
    if turn > 1:
        #dicitonary containing scorecard
        finalScoring = {"1. Ones Score": oneScore, "2. Twos Score": twoScore, "3. Threes Score": threeScore,
                        "4. Fours Score": fourScore, "5. Fives Score": fiveScore, "6. Sixes Scores": sixScore,
                        "7. Three of a Kind Score": threeOfAKindScore, "8. Four of a Kind Score": fourOfAKindScore,
                        "9. Full House": fullHouseScore, "10. Small Straight Score": smallStraightScore,
                        "11. Large Straight Score": largeStraightScore, "12. Chance Score": chanceScore,
                        "13. Yahtzee Score": yahtzeeScore}
        print("Current Scorecard")
        for category in finalScoring.keys():
            print("___________________________________")
            print (category, finalScoring[category])
    originalroll = []
    roll = []
    ReRollCounter = 0
    ReRollRemain = 1
    print("You have the chance to re roll the dice two times.")
    print("Rolling the dices...")
    Dice1 = (random.randint(1, 6))
    roll.append(str(Dice1))
    originalroll.append(str(Dice1))
    Dice2 = (random.randint(1, 6))
    roll.append(str(Dice2))
    originalroll.append(str(Dice2))
    Dice3 = (random.randint(1, 6))
    roll.append(str(Dice3))
    originalroll.append(str(Dice3))
    Dice4 = (random.randint(1, 6))
    roll.append(str(Dice4))
    originalroll.append(str(Dice4))
    Dice5 = (random.randint(1, 6))
    roll.append(str(Dice5))
    originalroll.append(str(Dice5))
    print("Dice 1:", Dice1)
    print("Dice 2:", Dice2)
    print("Dice 3:", Dice3)
    print("Dice 4:", Dice4)
    print("Dice 5:", Dice5)
    print("What Dice Do you want to reroll? Type 0 to re roll your selection.")
    while ReRollCounter < 2:
        RollAgain = input("Enter the Dice you want to re roll:(space in between)").split()
        if '1' in RollAgain:
            Dice1 = (random.randint(1, 6))
            del roll[0]
            roll.insert(0, Dice1)
        if '2' in RollAgain:
            Dice2 = (random.randint(1, 6))
            del roll[1]
            roll.insert(1, Dice2)
        if '3' in RollAgain:
            Dice3 = (random.randint(1, 6))
            del roll[2]
            roll.insert(2, Dice3)
        if '4' in RollAgain:
            Dice4 = (random.randint(1, 6))
            del roll[3]
            roll.insert(3, Dice4)
        if '5' in RollAgain:
            Dice5 = (random.randint(1, 6))
            del roll[4]
            roll.insert(4, Dice5)
       # if '0' in RollAgain:
        if True:
            if roll == originalroll:
                ReRollCounter = 2
                ReRollRemain = 0
            if ReRollCounter == 2:
                print("Your scoring roll will be:")
                print("Dice 1:", Dice1)
                print("Dice 2:", Dice2)
                print("Dice 3:", Dice3)
                print("Dice 4:", Dice4)
                print("Dice 5:", Dice5)
            if ReRollCounter < 1:
                print("Rolling the dices...")
                print("You have", ReRollRemain, "dice rerolls remaining.")
                print("Dice 1:", Dice1)
                print("Dice 2:", Dice2)
                print("Dice 3:", Dice3)
                print("Dice 4:", Dice4)
                print("Dice 5:", Dice5)
            ReRollCounter += 1
            ReRollRemain -= 1
            if ReRollCounter == 2:
                print("Your scoring roll will be:")
                print("Dice 1:", Dice1)
                print("Dice 2:", Dice2)
                print("Dice 3:", Dice3)
                print("Dice 4:", Dice4)
                print("Dice 5:", Dice5)

    roll = sorted(list(map(int, roll)))
    rollTotal = sum(list(map(int, roll)))

# score of ones
# iterates through each dice value in roll adds to the total for that number and count for that number
# checks count to see if it matches for 3 or 4 of a kind
    for x in roll:
        if x == 1:
            total = total + 1
            count = count + 1
    oneTotal = total
    oneCount = count
    if oneCount >= 3:
        threeOfAKind = rollTotal
    if oneCount >= 4:
        fourOfAKind = rollTotal
    if oneCount == 5:
        yahtzee = 50
    total = 0
    count = 0

    # score of twos
    # iterates through each dice value in roll adds to the total for that number and count for that number
    # checks count to see if it matches for 3 or 4 of a kind
    for x in roll:
        if x == 2:
            total = total + 2
            count = count + 1
    twoTotal = total
    twoCount = count
    if twoCount >= 3:
        threeOfAKind = rollTotal
    if twoCount >= 4:
        fourOfAKind = rollTotal
    if twoCount == 5:
        yahtzee = 50
    total = 0
    count = 0


    # score of threes
    # iterates through each dice value in roll adds to the total for that number and count for that number
    # checks count to see if it matches for 3 or 4 of a kind
    for x in roll:
        if x == 3:
            total = total + 3
            count = count + 1
    threeTotal = total
    threeCount = count
    if threeCount >= 3:
        threeOfAKind = rollTotal
    if threeCount >= 4:
        fourOfAKind = rollTotal
    if threeCount == 5:
        yahtzee = 50
    total = 0
    count = 0

    # score of fours
    # iterates through each dice value in roll adds to the total for that number and count for that number
    # checks count to see if it matches for 3 or 4 of a kind
    for x in roll:
        if x == 4:
            total = total + 4
            count = count + 1
    fourTotal = total
    fourCount = count
    if fourCount >= 3:
        threeOfAKind = rollTotal
    if fourCount >= 4:
        fourOfAKind = rollTotal
    if fourCount == 5:
        yahtzee = 50
    total = 0
    count = 0

    # score of fives
    # iterates through each dice value in roll adds to the total for that number and count for that number
    # checks count to see if it matches for 3 or 4 of a kind
    for x in roll:
        if x == 5:
            total = total + 5
            count = count + 1
    fiveTotal = total
    fiveCount = count
    if fiveCount >= 3:
        threeOfAKind = rollTotal
    if fiveCount >= 4:
        fourOfAKind = rollTotal
    if fiveCount == 5:
        yahtzee = 50
    total = 0
    count = 0


    # score of sixes
    # iterates through each dice value in roll adds to the total for that number and count for that number
    # checks count to see if it matches for 3 or 4 of a kind
    for x in roll:
        if x == 6:
            total = total + 6
            count = count + 1
    sixTotal = total + 1
    sixCount = count
    if sixCount >= 3:
        threeOfAKind = rollTotal
    if sixCount >= 4:
        fourOfAKind = rollTotal
    if sixCount == 5:
        yahtzee = 50
    total = 0
    count = 0

    #small straight and large straight scoring
    #there are only 2 possible solutions for large straight and 3 for small straight
    #checks to see if the roll has either of those options in it
    option1 = [1, 2, 3, 4, 5]
    option2 = [2, 3, 4, 5, 6]
    option3 = [1, 2, 3, 4]
    option4 = [2, 3, 4, 5]
    option5 = [3, 4, 5, 6]

    if option1 in roll or option2 in roll:
        largeStraight = 40
    else:
        largeStraight = 0

    if option3 in roll or option4 in roll or option5 in roll:
        smallStraight = 40
    else:
        smallStraight = 0

    #full house scoring
    #checks to see if any combination of number counts is equal to 5
    if twoCount + threeCount == 5 or twoCount + fourCount == 5 or twoCount + fiveCount == 5 or twoCount + sixCount == 5 or threeCount + fourCount == 5:
        fullHouse = 25
    if oneCount + twoCount == 5 or oneCount + threeCount == 5 or oneCount + fourCount == 5 or oneCount + fiveCount == 5 or oneCount + sixCount == 5:
        fullHouse = 25
    if threeCount + fiveCount == 5 or threeCount + sixCount == 5 or fourCount + fiveCount == 5 or fourCount + sixCount == 5 or fiveCount + sixCount == 5:
        fullHouse = 25

    #chance scoring
    chance = rollTotal

    #player score selection
    #shows player possible scores for current roll
    possibleScoring = {"1. Ones Score = ": oneTotal, "2. Twos Score = ": twoTotal, "3. Threes Score = ": threeTotal,
                       "4. Fours Score = ": fourTotal, "5. Fives Score = ": fiveTotal, "6. Sixes Score = ": sixTotal,
                       "7. Three of a Kind Score = ": threeOfAKind, "8. Four of a Kind Score = ": fourOfAKind,
                       "9. Full House = ": fullHouse, "10. Small Straight Score = ": smallStraight,
                       "11. Large Straight Score = ": largeStraight, "12. Chance Score = ": chance, "13. Yahtzee Score = ": yahtzee}
    #asks player for which way they would like to score it
    for scoringCategory in possibleScoring.keys():
        print("___________________________________")
        print(scoringCategory, possibleScoring[scoringCategory])

    playersChoice = input("Which scoring would you like to use? (1 - 13)")

    # score choice count
    oneScoreCount = 0
    twoScoreCount = 0
    threeScoreCount = 0
    fourScoreCount = 0
    fiveScoreCount = 0
    sixScoreCount = 0
    fullHouseScoreCount = 0
    smallStraightScoreCount = 0
    largeStraightScoreCount = 0
    chanceScoreCount = 0
    yahtzeeScoreCount = 0
    threeOfAKindScoreCount = 0
    fourOfAKindScoreCount = 0

    #based on user selection it will check to see if it was already on your score card
    #if not it will add it
    #if it is it will request new input
    if playersChoice == "1":
        if oneScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            oneScore = oneTotal
            oneScoreCount = oneScoreCount + 1
    if playersChoice == "2":
        if twoScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            twoScore = twoTotal
            twoScoreCount = twoScoreCount + 1
    if playersChoice == "3":
        if threeScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            threeScore = threeTotal
            threeScoreCount = threeScoreCount + 1
    if playersChoice == "4":
        if fourScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            fourScore = fourTotal
            fourScoreCount = fourScoreCount + 1
    if playersChoice == "5":
        if fiveScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            fiveScore = fiveTotal
            fiveScoreCount = fiveScoreCount + 1
    if playersChoice == "6":
        if sixScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            sixScore = sixTotal
            sixScoreCount = sixScoreCount + 1
    if playersChoice == "7":
        if threeOfAKindScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            threeOfAKindScore = threeOfAKind
            threeOfAKindScoreCount = threeOfAKindScoreCount + 1
    if playersChoice == "8":
        if fourOfAKindScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            fourOfAKindScore = fourOfAKind
            fourOfAKindScoreCount = fourOfAKindScoreCount + 1
    if playersChoice == "9":
        if fullHouseScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            fullHouseScore = fullHouse
            fullHouseScoreCount = fullHouseScoreCount + 1
    if playersChoice == "10":
        if smallStraightScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            smallStraightScore = smallStraight
            smallStraightScoreCount = smallStraightScoreCount + 1
    if playersChoice == "11":
        if largeStraightScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            largeStraightScore = largeStraight
            largeStraightScoreCount = largeStraightScoreCount + 1
    if playersChoice == "12":
        if chanceScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            chanceScore = chance
            chanceScoreCount = chanceScoreCount + 1
    if playersChoice == "13":
        if yahtzeeScoreCount == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            yahtzeeScore = yahtzee
            yahtzeeScoreCount = yahtzeeScoreCount + 1

# player 2
    print("Player 2")
    print("You are on round", turn)
    if turn > 1:
        finalScoring2 = {"1. Ones Score": oneScore2, "2. Twos Score": twoScore2, "3. Threes Score": threeScore2,
                        "4. Fours Score": fourScore2, "5. Fives Score": fiveScore2, "6. Sixes Scores": sixScore2,
                        "7. Three of a Kind Score": threeOfAKindScore2, "8. Four of a Kind Score": fourOfAKindScore2,
                        "9. Full House": fullHouseScore2, "10. Small Straight Score": smallStraightScore2,
                        "11. Large Straight Score": largeStraightScore2, "12. Chance Score": chanceScore2,
                        "13. Yahtzee Score": yahtzeeScore2}
        print("Current Score")
        for category in finalScoring.keys():
            print("___________________________________")
            print(category, finalScoring[category])
    originalroll = []
    roll = []
    ReRollCounter = 0
    ReRollRemain = 1
    print("You have the chance to re roll the dice two times.")
    print("Rolling the dices...")
    Dice1 = (random.randint(1, 6))
    roll.append(str(Dice1))
    originalroll.append(str(Dice1))
    Dice2 = (random.randint(1, 6))
    roll.append(str(Dice2))
    originalroll.append(str(Dice2))
    Dice3 = (random.randint(1, 6))
    roll.append(str(Dice3))
    originalroll.append(str(Dice3))
    Dice4 = (random.randint(1, 6))
    roll.append(str(Dice4))
    originalroll.append(str(Dice4))
    Dice5 = (random.randint(1, 6))
    roll.append(str(Dice5))
    originalroll.append(str(Dice5))
    print("Dice 1:", Dice1)
    print("Dice 2:", Dice2)
    print("Dice 3:", Dice3)
    print("Dice 4:", Dice4)
    print("Dice 5:", Dice5)
    print("What Dice Do you want to reroll? Type 0 to re roll your selection.")
    while ReRollCounter < 2:
        RollAgain = input("Enter the Dice you want to re roll:(space in between)").split()
        if '1' in RollAgain:
            Dice1 = (random.randint(1, 6))
            del roll[0]
            roll.insert(0, Dice1)
        if '2' in RollAgain:
            Dice2 = (random.randint(1, 6))
            del roll[1]
            roll.insert(1, Dice2)
        if '3' in RollAgain:
            Dice3 = (random.randint(1, 6))
            del roll[2]
            roll.insert(2, Dice3)
        if '4' in RollAgain:
            Dice4 = (random.randint(1, 6))
            del roll[3]
            roll.insert(3, Dice4)
        if '5' in RollAgain:
            Dice5 = (random.randint(1, 6))
            del roll[4]
            roll.insert(4, Dice5)
        # if '0' in RollAgain:
        if True:
            if roll == originalroll:
                ReRollCounter = 2
                ReRollRemain = 0
            if ReRollCounter == 2:
                print("Your scoring roll will be:")
                print("Dice 1:", Dice1)
                print("Dice 2:", Dice2)
                print("Dice 3:", Dice3)
                print("Dice 4:", Dice4)
                print("Dice 5:", Dice5)
            if ReRollCounter < 1:
                print("Rolling the dices...")
                print("You have", ReRollRemain, "dice rerolls remaining.")
                print("Dice 1:", Dice1)
                print("Dice 2:", Dice2)
                print("Dice 3:", Dice3)
                print("Dice 4:", Dice4)
                print("Dice 5:", Dice5)
            ReRollCounter += 1
            ReRollRemain -= 1
            if ReRollCounter == 2:
                print("Your scoring roll will be:")
                print("Dice 1:", Dice1)
                print("Dice 2:", Dice2)
                print("Dice 3:", Dice3)
                print("Dice 4:", Dice4)
                print("Dice 5:", Dice5)

    roll = sorted(list(map(int, roll)))
    rollTotal = sum(list(map(int, roll)))

    # score of ones
    for x in roll:
        if x == 1:
            total = total + 1
            count = count + 1
    oneTotal = total
    oneCount = count
    if oneCount >= 3:
        threeOfAKind = rollTotal
    if oneCount >= 4:
        fourOfAKind = rollTotal
    if oneCount == 5:
        yahtzee = 50
    total = 0
    count = 0

    # score of twos
    for x in roll:
        if x == 2:
            total = total + 2
            count = count + 1
    twoTotal = total
    twoCount = count
    if twoCount >= 3:
        threeOfAKind = rollTotal
    if twoCount >= 4:
        fourOfAKind = rollTotal
    if twoCount == 5:
        yahtzee = 50
    total = 0
    count = 0

    # score of threes
    for x in roll:
        if x == 3:
            total = total + 3
            count = count + 1
    threeTotal = total
    threeCount = count
    if threeCount >= 3:
        threeOfAKind = rollTotal
    if threeCount >= 4:
        fourOfAKind = rollTotal
    if threeCount == 5:
        yahtzee = 50
    total = 0
    count = 0

    # score of fours
    for x in roll:
        if x == 4:
            total = total + 4
            count = count + 1
    fourTotal = total
    fourCount = count
    if fourCount >= 3:
        threeOfAKind = rollTotal
    if fourCount >= 4:
        fourOfAKind = rollTotal
    if fourCount == 5:
        yahtzee = 50
    total = 0
    count = 0

    # score of fives
    for x in roll:
        if x == 5:
            total = total + 5
            count = count + 1
    fiveTotal = total
    fiveCount = count
    if fiveCount >= 3:
        threeOfAKind = rollTotal
    if fiveCount >= 4:
        fourOfAKind = rollTotal
    if fiveCount == 5:
        yahtzee = 50
    total = 0
    count = 0

    # score of sixes
    for x in roll:
        if x == 6:
            total = total + 6
            count = count + 1
    sixTotal = total + 1
    sixCount = count
    if sixCount >= 3:
        threeOfAKind = rollTotal
    if sixCount >= 4:
        fourOfAKind = rollTotal
    if sixCount == 5:
        yahtzee = 50
    total = 0
    count = 0

    # small straight and large straight scoring
    option1 = [1, 2, 3, 4, 5]
    option2 = [2, 3, 4, 5, 6]
    option3 = [1, 2, 3, 4]
    option4 = [2, 3, 4, 5]
    option5 = [3, 4, 5, 6]
    # print("hi")
    # print(roll)
    # print("option1",option1)
    # print("option2", option2)

    if option1 in roll or option2 in roll:
        largeStraight = 40
    else:
        largeStraight = 0

    if option3 in roll or option4 in roll or option5 in roll:
        smallStraight = 40
    else:
        smallStraight = 0

    # full house scoring
    if twoCount + threeCount == 5 or twoCount + fourCount == 5 or twoCount + fiveCount == 5 or twoCount + sixCount == 5 or threeCount + fourCount == 5:
        fullHouse = 25
    if oneCount + twoCount == 5 or oneCount + threeCount == 5 or oneCount + fourCount == 5 or oneCount + fiveCount == 5 or oneCount + sixCount == 5:
        fullHouse = 25
    if threeCount + fiveCount == 5 or threeCount + sixCount == 5 or fourCount + fiveCount == 5 or fourCount + sixCount == 5 or fiveCount + sixCount == 5:
        fullHouse = 25

    # chance scoring
    chance = rollTotal

    # player score selection

    possibleScoring = {"1. Ones Score = ": oneTotal, "2. Twos Score = ": twoTotal, "3. Threes Score = ": threeTotal,
                       "4. Fours Score = ": fourTotal, "5. Fives Score = ": fiveTotal,
                       "6. Sixes Score = ": sixTotal,
                       "7. Three of a Kind Score = ": threeOfAKind, "8. Four of a Kind Score = ": fourOfAKind,
                       "9. Full House = ": fullHouse, "10. Small Straight Score = ": smallStraight,
                       "11. Large Straight Score = ": largeStraight, "12. Chance Score = ": chance,
                       "13. Yahtzee Score = ": yahtzee}

    for scoringCategory in possibleScoring.keys():
        print("___________________________________")
        print(scoringCategory, possibleScoring[scoringCategory])

    playersChoice = input("Which scoring would you like to use? (1 - 13)")

    # score choice count
    oneScoreCount2 = 0
    twoScoreCount2 = 0
    threeScoreCount2 = 0
    fourScoreCount2 = 0
    fiveScoreCount2 = 0
    sixScoreCount2 = 0
    fullHouseScoreCount2 = 0
    smallStraightScoreCount2 = 0
    largeStraightScoreCount2 = 0
    chanceScoreCount2 = 0
    yahtzeeScoreCount2 = 0
    threeOfAKindScoreCount2 = 0
    fourOfAKindScoreCount2 = 0


    if playersChoice == "1":
        if oneScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            oneScore2 = oneTotal
            oneScoreCount2 = oneScoreCount + 1
    if playersChoice == "2":
        if twoScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            twoScore2 = twoTotal
            twoScoreCount2 = twoScoreCount2 + 1
    if playersChoice == "3":
        if threeScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            threeScore2 = threeTotal
            threeScoreCount2 = threeScoreCount2 + 1
    if playersChoice == "4":
        if fourScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            fourScore2 = fourTotal
            fourScoreCount2 = fourScoreCount2 + 1
    if playersChoice == "5":
        if fiveScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            fiveScore2 = fiveTotal
            fiveScoreCount2 = fiveScoreCount2 + 1
    if playersChoice == "6":
        if sixScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            sixScore2 = sixTotal
            sixScoreCount2 = sixScoreCount2 + 1
    if playersChoice == "7":
        if threeOfAKindScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            threeOfAKindScore2 = threeOfAKind
            threeOfAKindScoreCount2 = threeOfAKindScoreCount2 + 1
    if playersChoice == "8":
        if fourOfAKindScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            fourOfAKindScore2 = fourOfAKind
            fourOfAKindScoreCount2 = fourOfAKindScoreCount2 + 1
    if playersChoice == "9":
        if fullHouseScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            fullHouseScore2 = fullHouse
            fullHouseScoreCount2 = fullHouseScoreCount2 + 1
    if playersChoice == "10":
        if smallStraightScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            smallStraightScore2 = smallStraight
            smallStraightScoreCount2 = smallStraightScoreCount2 + 1
    if playersChoice == "11":
        if largeStraightScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            largeStraightScore2 = largeStraight
            largeStraightScoreCount2 = largeStraightScoreCount2 + 1
    if playersChoice == "12":
        if chanceScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            chanceScore2 = chance
            chanceScoreCount2 = chanceScoreCount2 + 1
    if playersChoice == "13":
        if yahtzeeScoreCount2 == 1:
            print("This score is already filled, try a different one")
            playersChoice = input("Which scoring would you like to use? (1 - 13)")
        else:
            yahtzeeScore2 = yahtzee
            yahtzeeScoreCount2 = yahtzeeScoreCount2 + 1

    turn = turn + 1


#player 1 final scoring

finalScoring = {"1. Ones Score": oneScore, "2. Twos Score": twoScore, "3. Threes Score": threeScore,
                "4. Fours Score": fourScore, "5. Fives Score": fiveScore, "6. Sixes Scores": sixScore,
                "7. Three of a Kind Score": threeOfAKindScore, "8. Four of a Kind Score": fourOfAKindScore,
                "9. Full House": fullHouseScore, "10. Small Straight Score": smallStraightScore,
                "11. Large Straight Score": largeStraightScore, "12. Chance Score": chanceScore,
                "13. Yahtzee Score": yahtzeeScore}

print("Player 1 Final Score")
for category in finalScoring.keys():

    print("___________________________________")
    print (category, finalScoring[category])

scoreTotal = oneScore + twoScore + threeScore + fourScore + fiveScore + sixScore + fullHouseScore + yahtzeeScore + largeStraightScore + smallStraightScore + chanceScore
bonus = 50
print("Player 1 Score total is:", scoreTotal)
if scoreTotal >= 63:
    scoreTotal = scoreTotal + bonus
    print("Congratualtions you have recieved the bonus points")
    print("Your new score is", scoreTotal)

#player 2 final scoring

finalScoring2 = {"1. Ones Score": oneScore2, "2. Twos Score": twoScore2, "3. Threes Score": threeScore2,
                 "4. Fours Score": fourScore2, "5. Fives Score": fiveScore2, "6. Sixes Scores": sixScore2,
                 "7. Three of a Kind Score": threeOfAKindScore2, "8. Four of a Kind Score": fourOfAKindScore2,
                 "9. Full House": fullHouseScore2, "10. Small Straight Score": smallStraightScore2,
                 "11. Large Straight Score": largeStraightScore2, "12. Chance Score": chanceScore2,
                 "13. Yahtzee Score": yahtzeeScore2}

print("Player 2 Final Score")
for category in finalScoring2.keys():
    print("___________________________________")
    print (category, finalScoring2[category])

scoreTotal2 = oneScore2 + twoScore2 + threeScore2 + fourScore2 + fiveScore2 + sixScore2 + fullHouseScore2 + yahtzeeScore2 + largeStraightScore2 + smallStraightScore2 + chanceScore2
print("Player 2 Score total is:", scoreTotal2)
if scoreTotal2 >= 63:
    bonus = 50
    scoreTotal2 = scoreTotal2 + bonus
    print("Congratualtions you have recieved the bonus points")
    print("Your new score is", scoreTotal)

if scoreTotal > scoreTotal2:
    print("Player 1 is the winner")
else:
    print("Player 2 is the winner")
   
