def find_message(text):
    message = ''
    for n in text:
        if n.isupper():
            message += n
    return message

print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
