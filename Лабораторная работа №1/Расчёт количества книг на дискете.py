# TODO Найдите количество книг, которое можно разместить на дискете

V_disk = 1.44 * 2**20
V_book = 100 * 50 * 25 * 4

amount = V_disk // V_book

print("Количество книг, помещающихся на дискету:", int(amount))
