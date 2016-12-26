"""Module for converting strings into piglatin, following the rules:

For words that begin with consonant sounds, all letters before the initial
vowel are placed at the end of the word sequence. Then, "ay" is added, as
in the following examples:

"pig" = "igpay"
"banana" = "ananabay"
"trash" = "ashtray"
"happy" = "appyhay"
"duck" = "uckday"
"glove" = "oveglay"
"latin" = "atinlay"
"dopest" = "opestday"

For words that begin with vowel sounds, one just adds "way" to the end.
Examples are:

"eat" → "eatway"
"omelet" → "omeletway"
"are" → "areway"

https://en.wikipedia.org/wiki/Pig_Latin
"""


def convert_to_piglatin(str):
    """ Converts the given string into piglatin and returns the result """
    vowels = ["a", "e", "i", "o", "u"]
    result = ""

    words = str.split(" ")

    for word in words:
        for vowel in vowels:
            if word.startswith(vowel):
                result += word + "way "
                break

        result += word[1:] + word[0].lower() + "ay "

    return result
