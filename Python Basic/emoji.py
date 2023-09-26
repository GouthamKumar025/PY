def emojiconvertor(message):
    user = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😔"
    }
    output = ""
    for ch in user:
        output += emojis.get(ch, ch) + " "
    return output


message = input(">")
print(emojiconvertor(message))