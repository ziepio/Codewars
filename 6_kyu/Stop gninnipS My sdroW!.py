'''Write a function that takes in a string of one or more words, and returns the same string, but with all five or
more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns
"This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
'''

def spin_words(sentence):
    word_joiner = []
    output = []
    splited_sentence = sentence.split()
    print(splited_sentence)
    for word in splited_sentence:
        if len(word) >= 5:
            for letter in word:
                word_joiner.insert(0, letter)
            output.append(''.join(word_joiner))
            word_joiner.clear()
        else:
            output.append(word)
    print(' '.join(output))
    return ' '.join(output)


test.assert_equals(spin_words("Welcome You"), "emocleW You")

'''
Other people's solutions:

1.
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

2.
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)
'''