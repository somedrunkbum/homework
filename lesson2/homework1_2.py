def find_message(text):
    message = []
    for n in text:
        if n.isupper():
            message.append(n)
    return ''.join(message)

print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
