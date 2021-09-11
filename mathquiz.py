age = int(input("How old are you? ")) # Asking user input for their age
if age > 18:
    print("You are too old to do this quiz.") # If the user's age is more than 18, it will return to the following string.
elif age < 13:
    print("You are too young to do this quiz.") # If the user's age is less than 13, it will return to the following string.
else:
    points = 0 # Set a starting point

    for x in range(11): # Loop the range from 0 to 11
        from random import randrange # Import random range from the random module

        fnum = randrange(1, 100) # Define first number in a random range from 1 to 100
        mnum = randrange(1, 100) # Define middle number in a random range from 1 to 100
        lnum = randrange(1, 100) # Define last number in a random range from 1 to 100

        if x == 0: # Question 1
            q = "{} + {} = "
            ans = int(input(q.format(fnum, lnum))) # Define user's answer as user input. The question is based on string formatting.
            res = fnum + lnum # Define the result of the math

            if ans == res: # If user's answer equals to the result of the math, add 1 point. And then, print the current points.
                points += 1
                pts = "✅ | Current Points: {}/10"

                print(pts.format(points))
            elif ans == res + 1 or ans == res - 1: # Else if the answer is off by 1 number, only add half points. And then, print the current points.
                points += 0.5
                pts = "Almost correct | Current Points: {}/10"

                print(pts.format(points))
            else: # If the answer is not equal to the math result, no points will be added. And then, print the current points.
                pts = "❌ | Current Points: {}/10"

                print(pts.format(points))
        elif x == 1: # Question 2
            q = "{} - {} = " 
            ans = int(input(q.format(fnum, lnum)))
            res = fnum - lnum

            if ans == res:
                points += 1
                pts = "✅ | Current Points: {}/10"

                print(pts.format(points))
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                pts = "Almost correct | Current Points: {}/10"

                print(pts.format(points))
            else:
                pts = "❌ | Current Points: {}/10"

                print(pts.format(points))
        elif x == 2: # Question 3
            q = "{} × {} = "
            ans = int(input(q.format(fnum, lnum)))
            res = fnum * lnum

            if ans == res:
                points += 1
                pts = "✅ | Current Points: {}/10"

                print(pts.format(points))
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                pts = "Almost correct | Current Points: {}/10"

                print(pts.format(points))
            else:
                pts = "❌ | Current Points: {}/10"

                print(pts.format(points))
        elif x == 3: # Question 4
            q = "{} + {} - {} = "
            ans = int(input(q.format(fnum, mnum, lnum)))
            res = fnum + mnum - lnum

            if ans == res:
                points += 1
                pts = "✅ | Current Points: {}/10"

                print(pts.format(points))
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                pts = "Almost correct | Current Points: {}/10"

                print(pts.format(points))
            else:
                pts = "❌ | Current Points: {}/10"

                print(pts.format(points))
        elif x == 4: # Question 5
            q = "{} - {} + {} = "
            ans = int(input(q.format(fnum, mnum, lnum)))
            res = fnum - mnum + lnum

            if ans == res:
                points += 1
                pts = "✅ | Current Points: {}/10"

                print(pts.format(points))
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                pts = "Almost correct | Current Points: {}/10"

                print(pts.format(points))
            else:
                pts = "❌ | Current Points: {}/10"

                print(pts.format(points))
        elif x == 5: # Question 6
            q = "{} + {} * {} = "
            ans = int(input(q.format(fnum, mnum, lnum)))
            res = fnum + mnum * lnum

            if ans == res:
                points += 1
                pts = "✅ | Current Points: {}/10"

                print(pts.format(points))
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                pts = "Almost correct | Current Points: {}/10"

                print(pts.format(points))
            else:
                pts = "❌ | Current Points: {}/10"

                print(pts.format(points))
        elif x == 6: # Question 7
            q = "{} * {} + {} = "
            ans = int(input(q.format(fnum, mnum, lnum)))
            res = fnum * mnum + lnum

            if ans == res:
                points += 1
                pts = "✅ | Current Points: {}/10"

                print(pts.format(points))
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                pts = "Almost correct | Current Points: {}/10"

                print(pts.format(points))
            else:
                pts = "❌ | Current Points: {}/10"

                print(pts.format(points))
        elif x == 7: # Question 8
            q = "{} - {} * {} = "
            ans = int(input(q.format(fnum, mnum, lnum)))
            res = fnum - mnum * lnum

            if ans == res:
                points += 1
                pts = "✅ | Current Points: {}/10"

                print(pts.format(points))
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                pts = "Almost correct | Current Points: {}/10"

                print(pts.format(points))
            else:
                pts = "❌ | Current Points: {}/10"

                print(pts.format(points))
        elif x == 8: # Question 9
            q = "{} * {} - {} = "
            ans = int(input(q.format(fnum, mnum, lnum)))
            res = fnum * mnum - lnum

            if ans == res:
                points += 1
                pts = "✅ | Current Points: {}/10"

                print(pts.format(points))
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                pts = "Almost correct | Current Points: {}/10"

                print(pts.format(points))
            else:
                pts = "❌ | Current Points: {}/10"

                print(pts.format(points))
        elif x == 9: # Question 10
            q = "{} * {} * {} = "
            ans = int(input(q.format(fnum, mnum, lnum)))
            res = fnum * mnum * lnum

            if ans == res:
                points += 1
                pts = "✅ | Current Points: {}/10"

                print(pts.format(points))
            elif ans == res + 1 or ans == res - 1:
                points += 0.5
                pts = "Almost correct | Current Points: {}/10"

                print(pts.format(points))
            else:
                pts = "❌ | Current Points: {}/10"
                
                print(pts.format(points))
        elif x == 10: # Final Result
            score = int((points / 10) * 100) # Define the score as integer to prevent additional ".0".
            final = "📋 | Quiz Done. Total Points: {}/10. Overall Score: {}%."

            print(final.format(points, score)) # Finally, print the result based on the string formatting.