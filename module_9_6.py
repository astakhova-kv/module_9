def all_variants(text):

    for len_ in range(1, len(text)+1):
        for i in range(len(text)):
            if len(text[i:i+len_]) == len_:
                yield text[i:i+len_]

a = all_variants("abcd")
for i in a:
    print(i)

