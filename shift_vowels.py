# Have a function that shifts vowels. Trying to develop it further...


# If a vowel is repeated multiple times the vowel is shifted by multiple steps.
# The number of steps is equal to the number of repeated vowels.
# For instance, “mood” becomes “maad”.
# helloo -> hillaa
# a e i o u, aa ee ii Oo uU, aAa ---> e i o u a, ii oo uu Aa eE, iIi


def shift_vowels(word):
    vowels_lower = "aeiou"
    vowels_upper = "AEIOU"

    # get the count of each vowel
    ans = list()
    words = word.split()
    for word in words:
        count = {}
        for letter in word:
            if letter.lower() in vowels_lower:
                count.setdefault(letter.lower(), 0)
                count[letter.lower()] += 1
        wlist = list(word)
        for i in range(len(wlist)):
            if wlist[i] in vowels_lower:
                wlist[i] = vowels_lower[(vowels_lower.index(wlist[i]) + count[wlist[i]]) % 5]
            elif wlist[i] in vowels_upper:
                wlist[i] = vowels_upper[(vowels_upper.index(wlist[i]) + count[wlist[i].lower()]) % 5]

        ans.append(''.join(wlist) + ' ')
    return ''.join(ans)


print(shift_vowels("a e i o u, aa ee ii Oo uU, aAa"))