sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, 
save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, 
if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, 
you all know those redolent remnants of day suspended, with the midges, 
about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; 
a furry warmth, golden midges.'''

for i in sentence:
    if i in ",.!?:)(;":
        sentence = sentence.replace(i, " ").lower()

lst = sentence.split()

my_set = {word for word in lst}
print(*sorted(my_set))