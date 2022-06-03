def translate_folder_id(id):
    #limitation with the current number system 36**3 = 46656
    numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #numbers = '0123456789ABCDEF'
    folder_id = ''

    for n in range(2, -7, -1):
        if id//len(numbers)**n:
            folder_id += numbers[id//len(numbers)**n]
            id -= id//len(numbers)**n * len(numbers)**n
        elif id <= len(numbers)-1:
            folder_id += numbers[id]
            break
        else:
            folder_id += numbers[0]
    if folder_id[-1] == '0' and len(folder_id) > 3:
        folder_id = folder_id[:-1]
    return folder_id
