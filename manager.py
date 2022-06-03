def translate_folder_id(id):
    numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    folder_id = ''

    for n in range(2, -1, -1):
        print(id, len(numbers)**n, folder_id)
        if id//len(numbers)**n:
            folder_id += numbers[id//len(numbers)**n]
            id -= id//len(numbers)**n * len(numbers)**n
        elif id <= len(numbers)-1:
            folder_id += numbers[id]
            break
        else:
            folder_id += numbers[0]
    return folder_id
