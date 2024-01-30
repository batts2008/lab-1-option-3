#Loop starts here
while True:

    #The user can input any string of text they want
    text = (input("enter a string of text: "))

    #This variable holds all the vowels so the program knows what they are
    vowels = ["a","o","e","i","u" ]
    highest_streak = 0

    #This is the vowel counter
    counter = 0

    #This for loop checks for any vowlels in the string and adds to the counter if any are present
    for letter in text:
        if letter in vowels:
            counter = counter + 1
            if counter > highest_streak:
                highest_streak = counter
    print(highest_streak)
        
