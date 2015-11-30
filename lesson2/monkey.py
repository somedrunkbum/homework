def monkey_solving(text, set_of_words):
    text = text.lower()
    real_word_count = 0
    for word in set_of_words:
        if  word in text:
            real_word_count += 1

    return real_word_count

set_of_words = set(["how", "are", "you", "hello"])
print(monkey_solving("How arererer you?", set_of_words))
print(monkey_solving("arererer?", set_of_words))
print(monkey_solving("heLLo you piska? siska are", set_of_words))