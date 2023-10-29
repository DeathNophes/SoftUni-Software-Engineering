import random


def get_random_words(words):
    return random.choice(words)


names = ['Iliyan', 'Darin', 'Petar', 'Alexandra', 'Martin', 'Ivaylo']
places = ['Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Otmanli', 'Marikostinovo']
verbs = ['holds', 'shoots', 'watches', 'enjoys', 'reads', 'plays with']
nouns = ['stones', 'cake', 'kids', 'pistol', 'Ak-74', 'hammer']
adverbs = ['slowly', 'delightfully', 'calmly', 'angrily']
details = ['at home', 'near the playground', 'at the hotel', 'at the water park', 'at the field']

print("Hello this is your first random sentence!")

while True:
    random_name = get_random_words(names)
    random_place = get_random_words(places)
    random_verb = get_random_words(verbs)
    random_noun = get_random_words(nouns)
    random_adverb = get_random_words(adverbs)
    random_detail = get_random_words(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")
    input("Click [Enter] to generate another one")
