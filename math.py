import msvcrt
import time
import os

# Made with love by poki95, based on ChatGPT's prompt and with the help of Scary_J

pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"

# Take the first 1000 digits of pi
pi = pi[:1000]

# Initialize score, user_digits and mistakes
score = 0
user_digits = ""
mistakes = ""

# Initialize the life counter and max number of allowed mistakes
life = 3
max_mistakes = 3

# Loop through each digit of pi
for i in range(len(pi)):
    # Get the current digit of pi and ask for user input
    digit = pi[i]
    answer = ""
    while not answer:
        # Check for user input without waiting for the Enter key
        if msvcrt.kbhit():
            answer = msvcrt.getch().decode()
            # Clear the terminal for a cleaner look
            os.system('cls')
            # Check if the answer is correct
            if answer == digit:
                user_digits += answer
                score += 1
                print("Correct!")
            else:
                life -= 1
                mistakes += answer
                print("Incorrect. The correct answer is " + digit)
                print("You have " + str(life) + " life(s) left.")
                if life == 0:
                    break
            # Show the digits entered so far without the mistakes
            digits_so_far = ""
            for j in range(len(user_digits)):
                if j < len(mistakes) or user_digits[j] == pi[j]:
                    digits_so_far += user_digits[j]
                else:
                    digits_so_far += "*"
            print("Digits entered so far: " + digits_so_far)
    
    # Check if the user has made too many mistakes
    if len(mistakes) >= max_mistakes:
        print("You've made too many mistakes. Game over.")
        break

# Print the digits the user inputted without the mistakes
user_digits_without_mistakes = ""
for j in range(len(user_digits)):
    if j < len(mistakes) or user_digits[j] == pi[j]:
        user_digits_without_mistakes += user_digits[j]
    else:
        user_digits_without_mistakes += "*"
print("You entered: " + user_digits_without_mistakes)

# Print final score
print("Quiz completed. Your final score is " + str(score) + " out of infinity, but I've only put the first " + str(len(pi)) + " digits.")
print(" ")
print("The first 250 digits of pi are:")
print("3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679")
print("  8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196")
print("  4428810975 6659334461 2847564823 3786783165 2712019091")
