input_string = "abcdefghijklmnopqrstuvwxyz" * 10
characters_to_display = 1
for i in range(0, len(input_string), characters_to_display):
    print(input_string[i:i + characters_to_display])
    characters_to_display += 1
