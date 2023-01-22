def pig_latin(word):
    vowels = "aeiou"
    if word[0] in vowels:
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"

print(pig_latin("word")) # ordway
print(pig_latin("apple")) # appleway

def pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = [pig_latin(word) if word.isalpha() else word for word in words]
    return " ".join(pig_latin_words)

print(pig_latin("I am a software engineer")) # Iway amway away oftwareway engineerway
