import time
import Design
import random

dif = {
        "e": ["Time is money, but knowledge is power",
    "Practice makes perfect in everything you do",
    "Happiness comes from simple little things",
    "The sky is blue and the sun is bright today",
    "Reading is a window to new worlds and ideas",
    "Hard work always pays off in the end",
    "Dream big, work hard, and stay humble",
    "Patience is the key to achieving great goals",
    "Life is short, so make every moment count",
    "Good habits create a strong and successful life",],

       "m" : ["Success is not about being the best, it is about being better than yesterday",
    "Typing with speed and accuracy requires constant practice and concentration",
    "The internet has completely changed how people share knowledge and ideas",
    "Healthy food and regular exercise can improve both body and mind",
    "Learning to manage time wisely is one of the most important life skills",
    "Mistakes are proof that you are trying and learning something new",
    "Communication is the bridge between people, cultures, and generations",
    "Teamwork allows ordinary people to achieve extraordinary results together",
    "Failure is not the opposite of success, it is part of the process of learning",
    "Discipline is choosing between what you want now and what you want most",],

       "h" : ["Technology continues to advance rapidly, shaping the way we work, learn, and interact every single day",
    "Developing strong problem-solving skills is essential for programmers who want to write efficient code",
    "Reading challenging books can improve not only your vocabulary but also your critical thinking abilities",
    "The most successful people are those who remain consistent even when they feel unmotivated",
    "Creativity allows us to find unique solutions to problems that logic alone cannot always solve",
    "The ability to focus deeply on one task is becoming rare, but it is more valuable than ever before",
    "Learning from failure is often more important than celebrating success, because failure teaches resilience",
    "Digital privacy and security are important issues that affect everyone in the modern connected world",
    "When you practice typing daily, your fingers develop muscle memory, allowing faster and smoother writing",
    "Innovation happens when curiosity meets persistence and a willingness to take risks despite uncertainty"]
    }

Design.color("\n                              ---<( Wellcome to speed typing game )>--\n","yellow","bold")
print("  In this game you must type a specific text appered when you choose a difficulty and you will figuer out your speed by second measure.\n" \
"Moreover, you can choose playing ( 1 player ) or ( 2 players ) in order to know whos the fastest.")

while True:

    choice = input("\nChoose (A) for 1 player or (B) for 2 players or (C) for 3 players: ").lower().strip()

    if choice == "a":
        choice2 = input("\nChoose a difficulty among ( easy(E) or medium(M) or hard(H) ): ").lower().strip()
        if choice2 in dif:
            sentence = random.choice(dif[choice2[0]]).lower()
            input("\nbefore starting, text should be similar to the showen sentence, get ready and type anything to start: ")
            print("\n                              Three",end="\r")
            time.sleep(1)
            print("                               Two  ",end="\r")
            time.sleep(1)
            print("                               One  ",end="\r")
            time.sleep(1)
            print("                               GO!  ",end="\r")
            time.sleep(1)
            start = time.time()
            Design.color(f"          ---<( {sentence} )>--\n","white","bold")
            text = input("start typing: ").lower()
            end = time.time()
            if sentence.strip() == text.strip():
                Design.shape3(f"All done your time is {round(end-start,2)}")
            elif abs(len(sentence.strip()) - len(text.strip())) < 6:
                Design.shape3(f"you have few mistakes however your time is {round(end-start,2)}")
            else:
                Design.shape3(f"Your answer is not suitable enough")
            Final = input("Choose brtween restart(Type any thing) or close(C): ").lower().strip()
            while Final[0] == "c": exit() 
            else : continue
        else:
            print(Design.shape1("You must choose a difficulty among ( easy(E) or medium(M) or hard(H) ) only !"))
    elif choice == "b":
        choice2 = input("\nChoose a difficulty among ( easy(E) or medium(M) or hard(H) ): ").lower().strip()
        if choice2 in dif:
            sentence = random.choice(dif[choice2[0]]).lower()
            input("\nplayer 1: before starting, text should be similar to the showen sentence, get ready and type anything to start: ")
            print("\n                              Three",end="\r")
            time.sleep(1)
            print("                               Two  ",end="\r")
            time.sleep(1)
            print("                               One  ",end="\r")
            time.sleep(1)
            print("                               GO!  ",end="\r")
            time.sleep(1)
            start = time.time()
            Design.color(f"          ---<( {sentence} )>--\n","white","bold")
            text = input("start typing: ").lower()
            end = time.time()
            difference1 = end - start
            if sentence.strip() == text.strip():
                Design.shape3(f"All done your time is {round(difference1,2)}")
            elif abs(len(sentence.strip()) - len(text.strip())) < 6:
                Design.shape3(f"you have few mistakes however your time is {round(difference1,2)}")
            else:
                Design.shape3(f"Your answer is not suitable enough")
            sentence = random.choice(dif[choice2[0]]).lower()
            input("\nplayer 2: before starting, text should be similar to the showen sentence, get ready and type anything to start: ")
            print("\n                              Three",end="\r")
            time.sleep(1)
            print("                               Two  ",end="\r")
            time.sleep(1)
            print("                               One  ",end="\r")
            time.sleep(1)
            print("                               GO!  ",end="\r")
            time.sleep(1)
            start = time.time()
            Design.color(f"          ---<( {sentence} )>--\n","white","bold")
            text = input("start typing: ").lower()
            end = time.time()
            difference2 = end - start
            if sentence.strip() == text.strip():
                Design.shape3(f"All done your time is {round(difference2,2)}")
            elif abs(len(sentence.strip()) - len(text.strip())) < 6:
                Design.shape3(f"you have few mistakes however your time is {round(difference2,2)}")
            else:
                Design.shape3(f"Your answer is not suitable enough")
            if difference1 > difference2:
                Design.color(f"                              ---<( player 2 won whith nearly {round(difference1-difference2,2)})>--\n","yellow","bold")
            else:
                Design.color(f"                              ---<( player 1 won white nearly {round(difference2-difference1,2)} )>--\n","yellow","bold")
            while Final[0] == "c": exit() 
            else : continue
    elif choice == "c":
        choice3 = input("\nChoose a difficulty among ( easy(E) or medium(M) or hard(H) ): ").lower().strip()
        if choice3 in dif:
            sentence = random.choice(dif[choice3[0]]).lower()
            input("\nplayer 1: before starting, text should be similar to the showen sentence, get ready and type anything to start: ")
            print("\n                              Three",end="\r")
            time.sleep(1)
            print("                               Two  ",end="\r")
            time.sleep(1)
            print("                               One  ",end="\r")
            time.sleep(1)
            print("                               GO!  ",end="\r")
            time.sleep(1)
            start = time.time()
            Design.color(f"          ---<( {sentence} )>--\n","white","bold")
            text = input("start typing: ").lower()
            end = time.time()
            difference1 = end - start
            if sentence.strip() == text.strip():
                Design.shape3(f"All done your time is {round(difference1,2)}")
            elif abs(len(sentence.strip()) - len(text.strip())) < 6:
                Design.shape3(f"you have few mistakes however your time is {round(difference1,2)}")
            else:
                Design.shape3(f"Your answer is not suitable enough")
            sentence = random.choice(dif[choice3[0]]).lower()
            input("\nplayer 2: before starting, text should be similar to the showen sentence, get ready and type anything to start: ")
            print("\n                              Three",end="\r")
            time.sleep(1)
            print("                               Two  ",end="\r")
            time.sleep(1)
            print("                               One  ",end="\r")
            time.sleep(1)
            print("                               GO!  ",end="\r")
            time.sleep(1)
            start = time.time()
            Design.color(f"          ---<( {sentence} )>--\n","white","bold")
            text = input("start typing: ").lower()
            end = time.time()
            difference2 = end - start
            if sentence.strip() == text.strip():
                Design.shape3(f"All done your time is {round(difference2,2)}")
            elif abs(len(sentence.strip()) - len(text.strip())) < 6:
                Design.shape3(f"you have few mistakes however your time is {round(difference2,2)}")
            else:
                Design.shape3(f"Your answer is not suitable enough")
            sentence = random.choice(dif[choice3[0]]).lower()
            input("\nplayer 3: before starting, text should be similar to the showen sentence, get ready and type anything to start: ")
            print("\n                              Three",end="\r")
            time.sleep(1)
            print("                               Two  ",end="\r")
            time.sleep(1)
            print("                               One  ",end="\r")
            time.sleep(1)
            print("                               GO!  ",end="\r")
            time.sleep(1)
            start = time.time()
            Design.color(f"          ---<( {sentence} )>--\n","white","bold")
            text = input("start typing: ").lower()
            end = time.time()
            difference3 = end - start
            if sentence.strip() == text.strip():
                Design.shape3(f"All done your time is {round(difference3,2)}")
            elif abs(len(sentence.strip()) - len(text.strip())) < 6:
                Design.shape3(f"you have few mistakes however your time is {round(difference3,2)}")
            else:
                Design.shape3(f"Your answer is not suitable enough")
            if difference1 < difference2 and difference1 < difference3:
                Design.color(f"                              ---<( player 1 won )>--\n","yellow","bold")
            elif difference2< difference1 and difference2 < difference3:
                Design.color(f"                              ---<( player 2 won )>--\n","yellow","bold")
            else:
                Design.color(f"                              ---<( player 3 won )>--\n","yellow","bold")
            Final = input("Choose brtween restart(Type any thing) or close(C): ").lower().strip()
            while Final[0] == "c": exit() 
            else : continue
    else:
        print(Design.shape1("You must choose ( A or B ) only !"))#