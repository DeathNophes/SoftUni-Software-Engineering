def concatenate(*words, **kwargs):
    text = ''.join(words)

    for key, value in kwargs.items():
        text = text.replace(key, value)

    return text
