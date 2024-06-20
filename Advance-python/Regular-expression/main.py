import re

pattern = r"[A-Z]+yclone"
text = '''Cyclone Godzilla is a fictional monster, also known as a kaiju, that first appeared in the 1954 film of the same name. Most versions of Godzilla are prehistoric mutated reptiles, transformed by nuclear testing. The character's powers come from radiation, which it craves and gains strength from. Godzilla cyclone serves as a metaphor for the consequences of nuclear warfare and the harm caused by nuclear weapons in Japan. Over the years, Godzilla has become an international pop culture icon, appearing in Japanese and American films, video games, novels, comic books, and television shows. The creature has been dubbed the “King of the Dyclone Monsters,” a title first used in the American localization of the 1954 film. Its legacy extends beyond cinema, making it a powerful symbol in both entertainment and cultural discourse.'''

# match = re.search(pattern,text) # stop for first match
# print(match)

matches = re.finditer(pattern,text)
for match in matches:
    print(match)
    # print(match.span())
    print(text[match.span()[0]:match.span()[1]])