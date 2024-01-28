from PIL import Image, ImageDraw, ImageFont

def text_resize(text):
    if text is None:
        return ''
    text = text.replace('실험', ' 실험')
    text = text.replace('(2)', '')
    text = text.replace('Ⅰ', '')
    text = text.replace('Ⅱ', '')
    text = text.replace('Ⅲ', '')
    text = text.replace('Ⅳ', '')
    text = text.replace('Ⅴ', '')
    data = text.split(' ')
    class_num = data[-1]
    data = data[:-1]
    result = ''
    length = 0
    for i in data:
        if length + len(i) > 7:
            result += '\n'
            length = 0
        result += i + ' '
        length += len(i) + 1
    if result.startswith('\n'):
        result = result[1:]
    return result + '\n' +class_num

def get_font(size):
    return ImageFont.truetype("./tools/GmarketSansMedium.otf", size)

def get_title_font(size):
    return ImageFont.truetype("./tools/Jalnan2.otf", size)

def image_maker(data, path):
    image = Image.new('RGB', (2000, 3000), "white")
    draw = ImageDraw.Draw(image)
    inside_color = ['#FFCCCC', '#FFE6CC', '#FCFCCF', '#CCFFCC', '#DDF1FF', '#CCCCFF', '#FFCCFF', '#D7A060']
    outside_color = ['#FF8080', '#FFBF80', '#F8F887', '#80FF80', '#80DDFF', '#8080FF', '#FF80FF', '#AC8250']
    subjects = []
    colors = []

    rects = []
    days = ['mon', 'tue', 'wed', 'thu', 'fri']
    times = ['1', '2', '3', '4', '5', '6', '7', '8']

    for day_index, day in enumerate(days):
        for time_index, time in enumerate(times):
            if data[f'{day}_{time}']['name'] == None:
                continue
            elif time_index > 0 and data[f'{day}_{time}']['name'] == data[f'{day}_{times[time_index-1]}']['name'] and data[f'{day}_{time}']['teacher'] == data[f'{day}_{times[time_index-1]}']['teacher'] and data[f'{day}_{time}']['location'] == data[f'{day}_{times[time_index-1]}']['location']:
                continue
            else:
                if data[f'{day}_{time}']['name'] not in subjects:
                    subjects.append(data[f'{day}_{time}']['name'])
                    colors.append([inside_color[(len(subjects)-1)%8], outside_color[(len(subjects)-1)%8]])
                start_x = day_index * 400 + 10
                start_y = time_index * 350 + 210
                end_x = start_x + 380
                if time_index < 7 and data[f'{day}_{time}']['name'] == data[f'{day}_{times[time_index+1]}']['name'] and data[f'{day}_{time}']['teacher'] == data[f'{day}_{times[time_index+1]}']['teacher'] and data[f'{day}_{time}']['location'] == data[f'{day}_{times[time_index+1]}']['location']:
                    end_y = start_y + 680
                else:
                    end_y = start_y + 330
                rects.append((start_x, start_y, end_x, end_y, colors[subjects.index(data[f'{day}_{time}']['name'])], data[f'{day}_{time}']['name'], data[f'{day}_{time}']['teacher'], data[f'{day}_{time}']['location']))

    for (start_x, start_y, end_x, end_y, color, name, teacher, location) in rects:
        draw.rounded_rectangle((start_x, start_y, end_x, end_y), fill=color[0], outline=color[1], radius=40, width=10)
        draw.text((start_x+15, start_y+20), text_resize(name), font=get_font(55), fill='black')
        draw.text((start_x+15, start_y+200), teacher + 'T' if teacher is not None else '', font=get_font(40), fill='black')
        draw.text((start_x+15, start_y+250), location if location is not None else '', font=get_font(40), fill='black')

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    draw.line((0, 190, 2000, 200), fill='black', width=10)
    for day_index, day in enumerate(days):
        #draw.rounded_rectangle((day_index*400+10, 10, day_index*400+390, 190), fill='#9f9f9f', outline='#7f7f7f', radius=40, width=10)
        draw.text((day_index*400+20, 80), day, font=get_font(100), fill='black')
    image.save(path)

def make_dark_image(data, path):
    image = Image.new('RGB', (2000, 3000), "black")
    draw = ImageDraw.Draw(image)
    inside_color = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
    outside_color = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
    subjects = []
    colors = []

    rects = []
    days = ['mon', 'tue', 'wed', 'thu', 'fri']
    times = ['1', '2', '3', '4', '5', '6', '7', '8']

    for day_index, day in enumerate(days):
        for time_index, time in enumerate(times):
            if data[f'{day}_{time}']['name'] == None:
                continue
            elif time_index > 0 and data[f'{day}_{time}']['name'] == data[f'{day}_{times[time_index - 1]}']['name']:
                continue
            else:
                if data[f'{day}_{time}']['name'] not in subjects:
                    subjects.append(data[f'{day}_{time}']['name'])
                    colors.append([inside_color[(len(subjects) - 1) % 8], outside_color[(len(subjects) - 1) % 8]])
                start_x = day_index * 400 + 10
                start_y = time_index * 350 + 210
                end_x = start_x + 380
                if time_index < 7 and data[f'{day}_{time}']['name'] == data[f'{day}_{times[time_index + 1]}'][
                    'name'] and data[f'{day}_{time}']['teacher'] == data[f'{day}_{times[time_index + 1]}'][
                    'teacher'] and data[f'{day}_{time}']['location'] == data[f'{day}_{times[time_index + 1]}'][
                    'location']:
                    end_y = start_y + 680
                else:
                    end_y = start_y + 330
                rects.append((start_x, start_y, end_x, end_y, colors[subjects.index(data[f'{day}_{time}']['name'])],
                              data[f'{day}_{time}']['name'], data[f'{day}_{time}']['teacher'],
                              data[f'{day}_{time}']['location']))

    for (start_x, start_y, end_x, end_y, color, name, teacher, location) in rects:
        draw.rounded_rectangle((start_x, start_y, end_x, end_y), fill=color[0], outline=color[1], radius=40, width=5)
        draw.text((start_x + 15, start_y + 20), text_resize(name), font=get_font(55), fill='white')
        draw.text((start_x + 15, start_y + 200), teacher + 'T' if teacher is not None else '', font=get_font(40),
                  fill='white')
        draw.text((start_x + 15, start_y + 250), location if location is not None else '', font=get_font(40),
                  fill='white')

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    draw.line((0, 190, 2000, 200), fill='white', width=10)
    for day_index, day in enumerate(days):
        # draw.rounded_rectangle((day_index*400+10, 10, day_index*400+390, 190), fill='#9f9f9f', outline='#7f7f7f', radius=40, width=10)
        draw.text((day_index * 400 + 20, 80), day, font=get_font(100), fill='white')
    image.save(path)