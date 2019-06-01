def is_pangram(sentence):

    letter = 'abcdefghijklmnopqrstuvwxyz'
    for i in letter.lower():
        if i not in sentence.lower():
            return False
    return True
