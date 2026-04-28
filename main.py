print("hello AI")
#activity 1 "hello ai"
print("hello, I am a AI bot. What's your name?")
name = input()
print(f"Nice to meet you, {name}")
print("How are you feeling today? (good/bad):")
mood = input().lower() 

if mood == "good":
    print("I'm glad to hear that.")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see sometimes its hard to put feelings into words.")

while True:
            follow_up = input("Would you like to share more about your day? (yes/no): ").lower()
            if follow_up == "yes":
                more = input("Tell me more: ")
                print(f"Thank you for sharing, {name}. I'm here to listen!")
                break
            elif follow_up == "no":
                print("That's okay! I'm always here to chat when you need.")
                break
            else:
                print("Please respond with 'yes' or 'no'.")

while True:
            chat = input("Would you like to continue chatting? (yes/no): ").lower()
            if chat == "no":
                print(f"Goodbye, {name}! Take care.")
                break
            elif chat == "yes":
                print("Great! Let's keep chatting.")
                break 
            else:
                print("Please respond with 'yes' or 'no'.")


while True:
            joke = input("Would you like to hear a joke? (yes/no): ").lower()
            if joke == "no":
                print(f"That's okay. I must tell you, it was a funny one")
                break
            elif joke == "yes":
                print("Why don’t skeletons fight each other?\nBecause they don’t have the guts! 😄")
                break 
            else:
                print("Please respond with 'yes' or 'no'.")

while True:
            follow = input("Would you like to continue chatting? (yes/no): ").lower()
            if follow == "no":
                print(f"Goodbye, {name}! Take care.")
                break
            elif follow == "yes":
                print("Great! Let's keep chatting.")
                break 
            else:
                print("Please respond with 'yes' or 'no'.")