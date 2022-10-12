with open("C:/Users/ariel/OneDrive/Рабочий стол/homework_5_python/homework/TASK1/text.txt", "r") as fin:
    for line in fin:
        words = line.split()
        for word in words:
            if "абв" in word:
                words.remove(word)
        sentence = " ".join(words)
        print(sentence)
