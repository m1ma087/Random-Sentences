import random
part1 = ["In Idre", "In Stömne", "In Gammelbyn"]
part2 = ["isst ein Elch", "fliegen Enten über", "lacht ein Tourenbegleiter über"]
part3 = ["den Materialschuppen.", "das herrlich grüne Gras.", "die Hose des Campleiters."]
part4 = ["So ist das in Schweden!", "Das passiert oft bei Rucksack Reisen!", "Wer hätte das gedacht?" ]
best_words = [part1, part2, part3, part4]
sentence = []
for part in best_words:
    r = random.randint(0,len(part)-1)
    sentence.append(part[r])
print(" ".join(sentence))
