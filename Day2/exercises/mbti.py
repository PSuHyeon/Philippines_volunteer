# Print guide message on the terminal
print("Let's test your MBTI! Press 'y' or 'n'. y: yes, n: no")

# Recieve input from user. Invalid input will be rejected with error message.
# User can input only "y" or "n".
while True:
    EI = input("You enjoy participating in team-based activities. y: yes, n: no\n")
    if (EI != "y" and EI != "n"):
        print("Please input 'y' or 'n'. Other inputs are invalid.")
        continue
    break
while True:
    SN = input("You are not too interested in discussions about various interpretations of creative works. y: yes, n: no\n")
    if (SN != "y" and SN != "n"):
        print("Please input 'y' or 'n'. Other inputs are invalid.")
        continue
    break
while True:
    TF = input("People’s stories and emotions speak louder to you than numbers or data. y: yes, n: no\n")
    if (TF != "y" and TF != "n"):
        print("Please input 'y' or 'n'. Other inputs are invalid.")
        continue
    break
while True:
    JP = input("Your living and working spaces are clean and organized. y: yes, n: no\n")
    if (JP != "y" and JP != "n"):
        print("Please input 'y' or 'n'. Other inputs are invalid.")
        continue
    break

# Check input and return MBTI value.
MBTI = ""
if EI == "y":
    MBTI += "E"
    # a += b means a = a + b
    # this is same as MBTI = MBTI + "E"
else:
    MBTI += "I"    

if SN == "y":
    MBTI += "S"
else:
    MBTI += "N"

if TF == "y":
    MBTI += "F"
else:
    MBTI += "T"

if JP == "y":
    MBTI += "J"
else:
    MBTI += "P"

print("Your MBTI is", MBTI)