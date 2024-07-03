def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.casefold() in i.casefold() or i.casefold() in root_word.casefold():
            same_words == same_words.append(i)
    print(same_words)
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
