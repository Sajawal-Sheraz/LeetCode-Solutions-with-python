def decodeMessage(key, message):
    letters = "abcdefghijklmnopqrstuvwxyz"
    unique_key = ""
    for i in key:
        if i in unique_key or i == " ":
            continue
        unique_key = unique_key + i

    decoder = {}
    for i in range(len(unique_key)):
        decoder[f"{unique_key[i]}"] = f"{letters[i]}"
    result_str = ""
    for i in message:
        if i == " ":
            result_str = result_str + " "
            continue
        result_str = result_str + decoder[i]
    return result_str


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"


print(decodeMessage(key, message))
