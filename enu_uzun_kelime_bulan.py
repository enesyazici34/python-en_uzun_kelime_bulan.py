def en_uzun_kelimeyi_bul(cumle):
    kelime = ""
    uzun_kelime = ""

    for harf in cumle + " ":
        if harf != " ":
            kelime += harf
        else:
            if len(kelime) > len(uzun_kelime):
                uzun_kelime = kelime
            kelime = ""
    
    return uzun_kelime

cumle = input("Bir cümle veya paragraf girin: ")

uzun_kelime = en_uzun_kelimeyi_bul(cumle)
print("En uzun kelime:", uzun_kelime)
