import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def text_resize(text):
    if text is None:
        return ''
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
def image_maker(data, path):
    plt.style.use('dark_background')
    prop = fm.FontProperties(fname='./tools/GmarketSansMedium.otf')
    rect = []
    for index, day in enumerate(['mon', 'tue', 'wed', 'thu', 'fri']):
        for i in range(1,9):
            rect.append((index*400, 350 * (8-i), 400, 350, data[f'{day}_{i}']))
    fig, ax = plt.subplots()
    for (x,y,w,h,data) in rect:
        ax.add_patch(plt.Rectangle((x,y),w,h,fill=False, edgecolor='white', linewidth=5))
        plt.annotate(text_resize(data['name']), (x+200, y+320), ha = 'center', va = 'top', fontproperties=prop, color='white', size=25)
        if "location" in data and data['location'] != None:
            plt.annotate(data['location'], (x+200, y+50), ha = 'center', va = 'center', fontproperties=prop, color='white', size=20)
        if "teacher" in data and data['teacher'] != None:
            plt.annotate(data['teacher']+'T', (x+200, y+110), ha = 'center', va = 'center', fontproperties=prop, color='white', size=20)

    for index, day in enumerate(["월", "화", "수", "목", "금"]):
        ax.add_patch(plt.Rectangle((index*400, 2800),400,150,fill=False, edgecolor='white', linewidth=5))
        plt.annotate(day, (index*400+200, 2875), ha = 'center', va = 'center', fontproperties=prop, color='white', size=30)
    ax.set_xlim(0, 2010)
    ax.set_ylim(0, 350 * 8 + 150)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.set_size_inches(20.1, 28.5)
    fig.savefig(f'{path}', dpi=200)
    plt.close(fig)