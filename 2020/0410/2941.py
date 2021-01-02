word = input()
length = len(word)
index = 0
character = 0
while index < length:
    if word[index] in "cdlnsz":
        if index + 1 < length:
            """
            c=
            c-
            d-
            s=
            z=

            lj
            nj

            dz=
            
            """
            if word[index + 1] in "=-":
                index += 2
                character += 1
            elif word[index] in "ln":
                if word[index + 1] == "j":
                    index += 2
                    character += 1
                else:
                    index += 1
                    character += 1
            elif word[index] == "d":
                if word[index + 1] == "z":
                    if index + 2 < length:
                        if word[index + 2] == "=":
                            index += 3
                            character += 1
                        else:
                            index += 2
                            character += 2
                    else:
                        character += 2
                        index += 2
                else:
                    index += 1
                    character += 1
            else:
                index += 1
                character += 1
        else:
            index += 1
            character += 1
    else:
        index += 1
        character += 1
print(character)