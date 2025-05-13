# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

#ROUGH
def minion(string):
    n = len(string)

    #initializing scores
    kevin_score = 0
    stuart_score = 0


    for i in range(n):
        if string[i].lower() in "aeiou":
            kevin_score += (n - i)  # Kevin scores for substrings starting with vowels
        else:
            stuart_score += (n - i)  # Stuart scores for substrings starting with consonants

    # Print results
    if kevin_score > stuart_score:
        print(f"Kevin wins with {kevin_score} points")
    elif kevin_score < stuart_score:
        print(f"Stuart wins with {stuart_score} points")
    else:
        print("It's a tie!")

minion("michelle")