import itertools

decompressed_message1 = "E,QAPLOAINAI OTCA ES E,,RLI OSRLNIAACPPROQ SUPERSTTTGVACNEODCA LNCVRRCUE DLVARSLONNQENRVLNSAIEEBIRANQPII ENIAACP O"
decompressed_message2 = "NVOGAR,IOQ EDOM,TRU MI PIOQA D EODENGE ODEI R"

messages = [decompressed_message1, decompressed_message2]

def generate_combinations(words, max_len=3):
    combinations = []
    for i in range(1, max_len + 1):
        for combo in itertools.permutations(words, i):
            combinations.append(' '.join(combo))
    return combinations

for i, message in enumerate(messages, 1):
    words = message.split()
    combinations = generate_combinations(words)
    print(f"Message {i}:")
    for combo in combinations:
        print(combo)
    print("\n")

