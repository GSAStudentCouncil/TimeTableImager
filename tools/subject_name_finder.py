def name_finder(name):
    if name == None:
        return {
            'name': None,
            'class': None
        }
    data = name.split(' ')
    name_end = 0
    for i in range(len(data)):
        if data[i].endswith('반'):
            name_end = i
            break
    return {
        'name': ' '.join(data[:name_end+1]),
        'class': data[name_end]
    }