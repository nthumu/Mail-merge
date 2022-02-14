# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as invitees:
    names = invitees.readlines()
    print(names)

with open("Input/Letters/starting_letter.txt") as letter_sample:
    letter = letter_sample.readlines()
    for line in letter:
        print(line)

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as final_letter:
        for line in letter:
            line.replace("[name]", str(name))
            final_letter.write(line)


