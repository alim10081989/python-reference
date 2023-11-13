names = open('Input/Names/invited_names.txt')

with open('Input/Letters/starting_letter.txt') as letter:
    new_letter = letter.read()
    for person in names.readlines():
        name = person.strip()
        with open(f'Output/ReadyToSend/letter_for_{name}', mode='w') as file:
            file.write(new_letter.replace('[name]', name))
