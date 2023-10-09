memory_mb = 1.44
n_pages = 100
n_lines = 50
n_chars = 25
memory_per_char_bytes = 4

books = int((memory_mb * (1024 ** 2)) / (n_pages *
                                     n_lines *
                                     n_chars *
                                     memory_per_char_bytes))

print("Количество книг, помещающихся на дискету:", books)
