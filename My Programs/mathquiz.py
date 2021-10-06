from random import choice, randrange # Import randrang and choice from the random module


age = int(input("How old are you? ")) # Asking user input for their age
if age > 18:
    print("You are too old to do this quiz.") # If the user's age is more than 18, it will return to the following string.
elif age < 13:
    print("You are too young to do this quiz.") # If the user's age is less than 13, it will return to the following string.
else:
    points = 0 # Set a starting point

    for x in range(11): # Loop the range from 0 to 11
        fnum = randrange(1, 100) # Define first number in a random range from 1 to 100
        mnum = randrange(1, 100) # Define middle number in a random range from 1 to 100
        lnum = randrange(1, 100) # Define last number in a random range from 1 to 100
        sign1 = choice("+", "-", "*", "/") # Define random choice of the 1st mathematical operator
        sign2 = choice("+", "-", "*", "/") # Define random choice of the 2nd mathematical operator

        if x == 0: # Question 1
            ans = float(input(f"{fnum} {sign1} {lnum} = ")) # Define user's answer as user input. The question is based on string formatting.
            res = eval(f"{fnum} {sign1} {lnum}") # Define the result of the math

            if ans == res: # If user's answer equals to the result of the math, add 1 point. And then, print the current points.
                points += 1
                print(f"✅ | Current Points: {points}/10")
            elif ans == res + 1 or ans == res - 1: # Else if the answer is off by 1 number, only add half points. And then, print the current points.
                points += 0.5
                print(f"Almost correct | Current Points: {points}/10")
            else: # If the answer is not equal to the math result, no points will be added. And then, print the current points.
                print(f"❌ | Current Points: {points}/10")
        elif x == 1: # Question 2
            ans = float(input(f"{fnum} {sign1} {lnum} = "))
            res = eval(f"{fnum} {sign1} {lnum}")

            if ans == res:
                points += 1
                print(f"✅ | Current Points: {points}/10")
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                print(f"Almost correct | Current Points: {points}/10")
            else:
                print(f"❌ | Current Points: {points}/10")
        elif x == 2: # Question 3
            ans = float(input(f"{fnum} {sign1} {lnum} = "))
            res = eval(f"{fnum} {sign1} {lnum}")

            if ans == res:
                points += 1
                print(f"✅ | Current Points: {points}/10")
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                print(f"Almost correct | Current Points: {points}/10")
            else:
                print(f"❌ | Current Points: {points}/10")
        elif x == 3: # Question 4
            ans = float(input(f"{fnum} {sign1} {lnum} = "))
            res = eval(f"{fnum} {sign1} {lnum}")

            if ans == res:
                points += 1
                print(f"✅ | Current Points: {points}/10")
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                print(f"Almost correct | Current Points: {points}/10")
            else:
                print(f"❌ | Current Points: {points}/10")
        elif x == 4: # Question 5
            ans = float(input(f"{fnum} {sign1} {lnum} = "))
            res = eval(f"{fnum} {sign1} {lnum}")

            if ans == res:
                points += 1
                print(f"✅ | Current Points: {points}/10")
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                print(f"Almost correct | Current Points: {points}/10")
            else:
                print(f"❌ | Current Points: {points}/10")
        elif x == 5: # Question 6
            ans = float(input(f"{fnum} {sign1} {mnum} {sign2} {lnum} = "))
            res = eval(f"{fnum} {sign1} {mnum} {sign2} {lnum}")

            if ans == res:
                points += 1
                print(f"✅ | Current Points: {points}/10")
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                print(f"Almost correct | Current Points: {points}/10")
            else:
                print(f"❌ | Current Points: {points}/10")
        elif x == 6: # Question 7
            ans = float(input(f"{fnum} {sign1} {mnum} {sign2} {lnum} = "))
            res = eval(f"{fnum} {sign1} {mnum} {sign2} {lnum}")

            if ans == res:
                points += 1
                print(f"✅ | Current Points: {points}/10")
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                print(f"Almost correct | Current Points: {points}/10")
            else:
                print(f"❌ | Current Points: {points}/10")
        elif x == 7: # Question 8
            ans = float(input(f"{fnum} {sign1} {mnum} {sign2} {lnum} = "))
            res = eval(f"{fnum} {sign1} {mnum} {sign2} {lnum}")

            if ans == res:
                points += 1
                print(f"✅ | Current Points: {points}/10")
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                print(f"Almost correct | Current Points: {points}/10")
            else:
                print(f"❌ | Current Points: {points}/10")
        elif x == 8: # Question 9
            ans = float(input(f"{fnum} {sign1} {mnum} {sign2} {lnum} = "))
            res = eval(f"{fnum} {sign1} {mnum} {sign2} {lnum}")

            if ans == res:
                points += 1
                print(f"✅ | Current Points: {points}/10")
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                print(f"Almost correct | Current Points: {points}/10")
            else:
                print(f"❌ | Current Points: {points}/10")
        elif x == 9: # Question 10
            ans = float(input(f"{fnum} {sign1} {mnum} {sign2} {lnum} = "))
            res = eval(f"{fnum} {sign1} {mnum} {sign2} {lnum}")

            if ans == res:
                points += 1
                print(f"✅ | Current Points: {points}/10")
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                print(f"Almost correct | Current Points: {points}/10")
            else:
                print(f"❌ | Current Points: {points}/10")
        elif x == 10: # Final Result
            score = int((points / 10) * 100) # Define the score as integer to prevent additional ".0".
            print(f"📋 | Quiz Done. Total Points: {points}/10. Overall Score: {score}%.") # Finally, print the result based on the string formatting.