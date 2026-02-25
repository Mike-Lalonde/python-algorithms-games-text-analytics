# import libraries
import os

# clear screen function for putting in menu later
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()
# print("==================Question 1=========================")
# Write a function repeat_characters(s) that takes a string s and returns a new string where each character in s is repeated twice consecutively.
echo_location = []

def echo():
    echo_location.clear() #*********
    echo_madness = "Is there anyone OUT THERE!!!"
    #for loop to itterate through each letter
    for letter in echo_madness:
            # stuff the letters as they come into the list
            echo_location.append(letter)
            # ctrl v :-P
            echo_location.append(letter)
    # join the letters 
    print(f"".join(echo_location))
# =============================================================================
# Write a function slice_edges(s) that returns a new string composed of the first 3 and last 3 characters of s concatenated together. 

def rags_to_riches():
    # carefully selected words famingerous does actually mean notorious
    notorious = "famigerous"
    # print notorious before change
    print(f"notorious : {notorious}" )
    # slicing and returning the new notorious
    return notorious[:3]+notorious[-3:]
# =====================================================================
# print('THE LOOPY WAY')
say_it = "decrement" # shout to Bobcat Goldberg skit
# As per the instructions
def slice_edges_for(s):
    # to empty arrays for first and last 3
    first = []
    last = [] 
    # looks at the length of s
    numb = len(s)
    # itterate through each index
    for i, chop in enumerate(s):
        # take index 0,1,2
        if i < 3:
            # append it to first
            first.append(chop)
        # Take the last three index and 
        if i >= numb - 3:
            # append to last array
            last.append(chop)
            # join the last and the first array
    return "".join(first + last)
# =====================================================================
# print("C) Replace The first Characters : ")
# Write a function replace_first_char(s) that replaces all occurrences of the first character in the string with $ except for the first character itself.
def replace_first_char():
    with open("treasure_map.txt") as story:
        original = story.read()
        # isolates the first character in the string
        captured = original[:1]
        # put the rest of the story into new text (except the first character)
        new_text = original[1:]
        # a list to put the newly constructed story in after changes
        new_story = []
        # itterating through the the rest of the new_text
        for t in new_text:
            #  comparing the first character to every character in the rest of the story
            if t == captured:
                #  if the character  equals the first replace it with drunken pirate squaller
                new_story.append("YO HO HO AND A BOTTLE O'RUM")
            else:
                # otherwise keep the characters the same
                new_story.append(t)
    # outside the loop.  remove the list's "new_story" ,
    changed_text = ''.join(new_story)
    # concatinate the first letter to the rest of the story
    final_story = captured + changed_text
    # print and go celebrate with a beer...or a bottle o rum
    print(final_story)
# ---------------------------------------------------------------------------------
# Write a function remove_nth_char(s, n) that removes the character at index n from the string s. 
def remove_nth_char(catch_phrase, number_index):
# if the number is less then 0  or longer then the phrase just return the catch phrase
    if  number_index < 0 or number_index >= len(catch_phrase):
        return catch_phrase
    # if the above criteria is met, go to letter that is being requested, remove it and return the rest of the catch phrase as is.
    return catch_phrase[:number_index] + catch_phrase[number_index+1:]

# function to take users input, ensure it's valid input and return hand it to remove nth function then take the results
def help_remove_nth_char():
    catch_phrase = input("ARRGGH Matey be yea enter'in a phrase : ")
    # validation of users input
    try:
        number_index = int(input("Which index be ye removin', matey? (0-based): "))
    except ValueError:
        print("That ain't a number, sailor. Leaving the phrase as-is.")
        print(catch_phrase)
        return
    result = remove_nth_char(catch_phrase, number_index)
    print(result)
# ----------------------------------------------------------------------
# Write a function is_palindrome(s) that returns True if s is a palindrome ignoring case and spaces,
# otherwise False
def is_palindrome(buried_treasure):
    # Build a new string with spaces removed and letters lowercased
    scrubbed_deck = ""
    # Forloop to clean up the users input on skipping spaces
    for rune in buried_treasure:
        if rune != " ":
            # convert uppercase to lowercase
            scrubbed_deck += rune.lower()
    
    # variable for storing letters fo backward loop
    magic_scroll = ""
    # itterate backwards through users input and then store it in the magic scroll
    for i in range(len(scrubbed_deck) - 1, -1, -1):
        magic_scroll += scrubbed_deck[i]
    # Compare both words for a match
    return scrubbed_deck == magic_scroll
#  Helpler function checks to see if users input is a palindrome
def palindrome_judgment():
    captain_input = input("🌊 Avast! Enter a phrase to test fer palindrome: ")
    # passing in users input to palindrome function and store the bool that it returns
    verdict = is_palindrome(captain_input)
    # what happens if nothing is said
    if captain_input == "":
        print("🪙 Ye be sitting thur waggin yur tongue wit nuting ta say and by pirate code, that's a palindrome: ", verdict)
    else:
        # the actual true or false
        print(f"☠️  Be it a palindrome, matey? {verdict}")
#
# ==========================================================================
#                          Anchours and Sails (Q2)
#================================================== =======================
# Tic-Tac-Toe! Creating this simple little game will give you
# practice with a list of lists data structure, loops, conditionals, and console output with print statements
# only. This exercise will help you deepen your understanding of nested lists as 2D grids and control
# structures to build simple interactive applications. 

# Creates the game board (3x3) Matrix spaces
def cannons():
    # 3x3 board of spaces
    return [[" " for _ in range(3)] 
            for _ in range(3)]

# function to give 'game pieces'
def cannon_foder(mark):
    if mark == "A":
        return "⚓"
    if mark == "S":
        return "⛵"   
    return " "  

# function to print the board
def display_board(board):
    # printing the column header
    print("    0   1   2")
    # loop to print the rows and the columns
    for r in range(3):
        row = [cannon_foder(board[r][0]),
               cannon_foder(board[r][1]),
               cannon_foder(board[r][2])]
        print(f"{r}   " + " | ".join(row))
        if r < 2:
            print("   ---+---+---")

def fire(board, sailor):
# Main game loop
    while True:
        # Icons for game (update board)
        emoji = cannon_foder(sailor)
        # picking a row and then a column
        row = input(f"\nCaptain {sailor}, pick yer row (0-2 or Q to quit): ").strip().upper()
        if row == "Q":
            return "QUIT"
        col = input(f"\nCaptain {sailor}, pick yer column (0-2 or Q to quit): ").strip().upper()
        if col == "Q":
            return "QUIT"
        # making sure player input is a digit
        if not (row.isdigit() and col.isdigit()):
            print("Those ain't numbers, matey. Try again.")
            continue
        # changing the user input if valid to a number rather then a string
        r = int(row)
        c = int(col)
        # if user inputs any number other then 0,1 or 2 - say this
        if r < 0 or r > 2 or c < 0 or c > 2:
            print("That be off the map! Try 0 - 2, or Q to quit.")
            continue
        #  ensuring the chosen position is empty
        if board[r][c] != " ":
            print("That spot be taken. Choose another.")
            continue
        # place the player's x on the board 
        board[r][c] = sailor
        return  "Nice!"

# Function to see if winning conditions have been met.
def check_winner(board):
    # rows win condition
    for r in range(3):
        if board[r][0] != " " and board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]
    # cols win condition
    for c in range(3):
        if board[0][c] != " " and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # diagonals  win conditions
    if board[1][1] != " ":
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    return None
# function that looks at the board and checks to see if there is any spaces left
def brass_monkey(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                return False
    return True
#  main game function. handles game turns
def anchours_and_sails():
    # main game loop
    while True:
        # stores game state
        balls = cannons()  
        # Player A your up first        
        sailor = "A"   
        # inner game loop looks at each turn to see if there is a winner              
        while True:
            clear_screen()
            print("=== Anchours and Sails (Question 2) ===")
            print("A = Anchours, S = Sails")
            # show the games current state
            display_board(balls)
            # Calls the main game function and calls the player to take his turn
            fire(balls, sailor)

            # checks to see if winnng conditions have been met and displays the appropriate statement
            winner = check_winner(balls)
            if winner is not None:
                clear_screen()
                print("=== Anchours and Sails (Question 2) ===")
                display_board(balls)
                if winner == "A":
                    print("Anchours (A) claim the seas!")
                else:
                    print("Sails (S) catch the wind and win!")
                break
            # checks to see if it's a cat's game
            if brass_monkey(balls):
                clear_screen()
                print("=== Anchours and Sails (Question 2) ===")
                # shows the current board state
                display_board(balls)
                print("It be a draw—call it still waters.")
                break

            # switches the actual turns (players) everyturn
            sailor = "S" if sailor == "A" else "A"

        # /conditional check o see if player wants more punishment.
        again = input("Hoist 'nother round? (Y/N): ").strip().upper()
        if again == "Q":
            print("Abandon ship! Back to port...")
            return        
        if again != "Y":
            print("Fair winds and following seas!")
            break
#=============================================================================
                        #    Question 3     *
# ========================================================================
# Function that sanitizes and makes text consistent for all parts of q3.
def first_mate(line):
    chest = [] 
    piece_o_eight = ""
    # Itterates through the text handed to it and looks at conditions
    for rune in line:
        # checks to see if input is alphanumerical or apostrophies
        if rune.isalnum() or rune == "'":
            piece_o_eight += rune
        else:
            if piece_o_eight != "":
                chest.append(piece_o_eight.lower())
                piece_o_eight = ""
    if piece_o_eight != "":
        chest.append(piece_o_eight.lower())
    return chest

#  my Statics function.  it collects and holds each of thr requested states for the HTML page
def tally_booty(booty_bag):
    # total word count
    total_doubloons = 0
    # sum of the word lengths
    total_lengths = 0.0
    # longest words
    longest_shanty = ""
    # unique word list
    crew_manifest = []
    # frequency counters
    parrot_words = []
    parrot_counts = []
    # forloop to itterate through the text
    for word in booty_bag:
        # count each word
        total_doubloons += 1
        # count the length of each word
        total_lengths += len(word)
        # check for the longest word
        if len(word) > len(longest_shanty):
            # store the longest word
            longest_shanty = word
            # collect the word if it hasn't been seen
        if word not in crew_manifest:
            crew_manifest.append(word)
            # frequency count of parrot arrays
        squawked = False
        # itterate through all the words and see which ones are the same
        for i, pw in enumerate(parrot_words):
            if pw == word:
                # count the word if it's a repeat
                parrot_counts[i] += 1
                # continue with the next word
                squawked = True
                break
        # if the word hasn't been seen store in the unqie list
        if not squawked:
            parrot_words.append(word)
            # add 1 to the unique counts
            parrot_counts.append(1)
    # average word length
    avg_grog = (total_lengths / total_doubloons) if total_doubloons > 0 else 0.0
    # /intitializes  the variables
    captains_word = "" 
    captains_count = 0
    # loops over i and whenever a higher count is seen replaces both indices
    for i in range(len(parrot_words)):
        if parrot_counts[i] > captains_count:
            captains_count = parrot_counts[i]
            captains_word = parrot_words[i]
            # returns the following dictionary
    return {
        "vocab_size": len(crew_manifest),
        "avg_length": round(avg_grog, 2),
        "total_words": total_doubloons,
        "longest_word": longest_shanty,
        "most_frequent": (captains_word, captains_count),
    }
# function to read the text and then........
def read_the_sea(map_path="treasure_map.txt"):
    with open(map_path) as t_map:
        contents = t_map.read()
    #  split the lines without adding newline characters
    sea_lines = contents.splitlines()
    booty_bag = []
    # intterates each line of text
    for wake in sea_lines:
        # itterates each character of each line
        for coin in first_mate(wake):
            # puts sanitized **firstmate** text into the bootybag
            booty_bag.append(coin)
    # computes all the stats and puts it in haul (tally_booty)
    haul = tally_booty(booty_bag)
    # storing for display on the website
    jolly = haul["longest_word"]
    parrot, squawks = haul["most_frequent"]
    # USED TO BE A SEPERATE FUNCTION
    ye_message = []
    # starting to itterate through each line
    for treasure in contents.splitlines():
        # each letter getting rid of whitespace
        treasure = treasure.strip()
        if treasure:
            # grab the first letter of each line and append them list 
            ye_message.append(treasure[0])
            # join them {no spaces}
            black_pearls = ye_message.join()
    # select each line range and remove the commas
    da_real_treasure = black_pearls[0:3] + " " + \
                       black_pearls[3:5] + " " + \
                       black_pearls[5:12] + " " + \
                       black_pearls[12:14] + " " + \
                       black_pearls[14:18] + " " + \
                       black_pearls[18:] + "!!"
    # put the message in hidden treasure
    hidden_treasure = da_real_treasure 
    # something to put the entire HTML inside of
    # ==============HTML ===========================
    captain_log = f"""
  
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Captain's Log: Whale of a Tale Report</title>
</head>
<body>
    <h1>Whale of a Tale Report (Captain's Log)</h1>
    <h3>Ye be wonderin aboat dis matey???</h3>
    <ul>
        <li><strong>Vocabulary Size:</strong> {haul['vocab_size']}</li>
        <li><strong>Average Word Length:</strong> {haul['avg_length']}</li>
        <li><strong>Total Words:</strong> {haul['total_words']}</li>
        <li><strong>Longest Word:</strong> {jolly} (length {len(jolly)})</li>
        <li><strong>Most Frequent Word:</strong> {parrot} (appears {squawks} times)</li>
    </ul>
    <p onmouseover="this.querySelector('.secret').style.display='inline'"
       onmouseout="this.querySelector('.secret').style.display='none'">
       <strong>And don't Ye be frettin' Yur Secret Message : </strong>
       <span class="secret" hidden style="color:red;">{hidden_treasure}</span> be safe with me
    </p>
</body>
</html>"""
    with open("whale_of_a_tale_report.html", "w") as bottle:
        bottle.write(captain_log)
    print("\nSaved report to whale_of_a_tale_report.html")

# THE MENU BELOW

def show_menu():
    print("==========================")
    print("     Assignment One")
    print("==========================")
    print("1) Repeat Characters -  Question (1a)")
    print("2) Slice and Extract -  Question (1b)")
    print("3) Replace Character -  Question (1c)")
    print("4) Remove Nth Character Question (1d)")
    print("5) Check Palindrome  -  Question (1e)")
    print("6) Anchours and Sails - Question (2) ")
    print("7) Yer Secret Message - Question (3) ")
    print("Q) End Program")
    
def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("\nChoose: ").strip().upper()
        clear_screen()

        if choice == "1":
            echo()
            input("\nPress enter to continue...")
        elif choice == "2":
            print("The Loopy way")
            print(f"Bad Pirate : {say_it}")  
            print(f"Good Pirate : {slice_edges_for(say_it)}")
            print("\nThe Best Way") 
            print(f"riches : {rags_to_riches()}")
            input("\nPress enter to continue...")
        elif choice == "3":
            print("C) Replace The first Characters : ")
            replace_first_char()
            input("\nPress Enter to continue...")
        elif choice == "4":
             print("Removing the nth Character")
             help_remove_nth_char()
             input("\nPress Enter to continue...")
        elif choice == "5":
            print("Palindrome ye say! we will seeNaboat dat!")
            palindrome_judgment() 
            input("\nPress Enter to continue...")
        elif choice == "6":
            print("Dar ye play me a game of Anchours and Sails huh?")
            anchours_and_sails()
            input("\nPress Enter to continue...")           
        elif choice == "7":
            print("Story Text Analysis")
            read_the_sea()
            input("\nPress Enter to continue...")                
        elif choice == "Q":
            break
        else:
            print("Unknown choice. Try 1-7 or Q.\n")

if __name__ == "__main__":
    clear_screen()
    main()