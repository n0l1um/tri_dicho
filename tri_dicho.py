def dichotomie_ite(tab, x):
    if len(tab) == 0:
        return False
    if x > tab[len(tab)-1] or x < tab[0]:
        return False
    start = 0
    end = len(tab)
    while start <= end:
        middle = (start + end) // 2
        if x == tab[middle]:
            return True
        if x > tab[middle]:
            start = middle
        if x < tab[middle]:
            end = middle
    return False

liste_1 = [1,2,38,45,51,61,7484,487981,5151581]
print(dichotomie_ite(liste_1, 38))
liste_2 = [4, 7, 8, 9]
print(dichotomie_ite(liste_2, 7))
liste_3 = [4, 8, 9]
print(dichotomie_ite(liste_3, 4))
liste_3 = [4, 8, 9]
print(dichotomie_ite(liste_3, 9))
liste_3 = [4, 8, 9]
print(dichotomie_ite(liste_3, 25))

print(dichotomie_ite([4 , 8, 9], 8))