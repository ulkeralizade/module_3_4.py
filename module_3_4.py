def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()

    for word in other_words:
        if root_word in word.lower() or word.lower() in root_word:
            same_words.append(word)

    return(same_words)

result1 = single_root_words('rich','richest','orichalcum','cheers','riches')
result2 = single_root_words('Disablement','Able','Mable','Disable','Bagel')

print(result1)
print(result2)