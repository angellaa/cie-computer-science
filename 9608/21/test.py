
def compress(image):
    if image == "":
        return ""

    letter = image[0]
    i = 0
    result = ""

    while True:
        count = 0

        while i < len(image) and letter == image[i]:
            count += 1
            i += 1

        result += letter + str(count)

        if i >= len(image):
            break
        else:
            letter = image[i]

    return result

print(compress(""))
print(compress("A"))
print(compress("AAAA"))
print(compress("AAAABBBBB"))
print(compress("AAAABBBBBCCCCCCCCCCC"))

