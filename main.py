import random

def draw_tree(height, shape, color, decorations):
    """
    繪製客製化聖誕樹
    :param height: 樹的高度
    :param shape: 樹的形狀 ('triangle', 'star', 'pine')
    :param color: 樹的顏色 ('green', 'blue', 'red')
    :param decorations: 裝飾列表 (e.g., ['star', 'lights', 'ornaments'])
    """
    # 顏色映射 (簡單的 ANSI 顏色代碼)
    color_codes = {
        'green': '\033[92m',
        'blue': '\033[94m',
        'red': '\033[91m'
    }
    reset_color = '\033[0m'
    tree_color = color_codes.get(color, '\033[92m')

    # 根據形狀繪製樹
    if shape == 'triangle':
        for i in range(1, height + 1):
            spaces = ' ' * (height - i)
            leaves = '*' * (2 * i - 1)
            print(spaces + tree_color + leaves + reset_color)
    elif shape == 'star':
        # 簡單的星星形狀
        for i in range(1, height + 1):
            if i == 1:
                print(' ' * (height - 1) + tree_color + '*' + reset_color)
            elif i <= height // 2:
                spaces = ' ' * (height - i)
                leaves = '*' * (2 * i - 1)
                print(spaces + tree_color + leaves + reset_color)
            else:
                spaces = ' ' * (height - i)
                leaves = '*' * (2 * i - 1)
                print(spaces + tree_color + leaves + reset_color)
    elif shape == 'pine':
        # 松樹形狀 (更寬的底部)
        for i in range(1, height + 1):
            spaces = ' ' * (height - i)
            leaves = '*' * (2 * i - 1)
            print(spaces + tree_color + leaves + reset_color)

    # 樹幹
    trunk_width = max(1, height // 5)
    trunk_height = max(1, height // 4)
    for _ in range(trunk_height):
        spaces = ' ' * (height - trunk_width // 2 - 1)
        trunk = '|' * trunk_width
        print(spaces + '\033[33m' + trunk + reset_color)  # 棕色樹幹

    # 添加裝飾
    if 'star' in decorations:
        # 在樹頂添加星星
        print(' ' * (height - 1) + '\033[93m' + '*' + reset_color)
    if 'lights' in decorations:
        # 隨機添加燈泡 (用不同顏色的小點表示)
        lights = ['\033[91m.', '\033[93m.', '\033[94m.', '\033[92m.']
        for i in range(1, height):
            line = ' ' * (height - i) + '*' * (2 * i - 1)
            # 隨機插入燈泡
            if random.random() < 0.3:  # 30% 機率添加燈泡
                pos = random.randint(0, len(line) - 1)
                line = line[:pos] + random.choice(lights) + line[pos+1:]
            print(tree_color + line + reset_color)
    if 'ornaments' in decorations:
        # 添加裝飾球 (用 O 表示)
        for i in range(2, height, 2):
            line = ' ' * (height - i) + '*' * (2 * i - 1)
            # 隨機插入裝飾球
            if random.random() < 0.4:
                pos = random.randint(0, len(line) - 1)
                line = line[:pos] + '\033[95mO\033[0m' + line[pos+1:]
            print(tree_color + line + reset_color)

def main():
    print("歡迎來到客製化聖誕樹小遊戲！")
    print("讓我們一起製作屬於您的聖誕樹吧！")

    # 選擇樹的高度
    while True:
        try:
            height = int(input("請輸入樹的高度 (3-10): "))
            if 3 <= height <= 10:
                break
            else:
                print("高度必須在 3 到 10 之間。")
        except ValueError:
            print("請輸入有效的數字。")

    # 選擇樹的形狀
    shapes = ['triangle', 'star', 'pine']
    print("可用的形狀: triangle (三角形), star (星星形), pine (松樹形)")
    while True:
        shape = input("請選擇樹的形狀: ").lower()
        if shape in shapes:
            break
        else:
            print("請選擇有效的形狀。")

    # 選擇樹的顏色
    colors = ['green', 'blue', 'red']
    print("可用的顏色: green (綠色), blue (藍色), red (紅色)")
    while True:
        color = input("請選擇樹的顏色: ").lower()
        if color in colors:
            break
        else:
            print("請選擇有效的顏色。")

    # 選擇裝飾
    decorations = []
    print("可用的裝飾: star (星星), lights (燈泡), ornaments (裝飾球)")
    add_decorations = input("是否添加裝飾？ (y/n): ").lower()
    if add_decorations == 'y':
        while True:
            dec = input("請輸入裝飾名稱 (或 'done' 結束): ").lower()
            if dec == 'done':
                break
            elif dec in ['star', 'lights', 'ornaments'] and dec not in decorations:
                decorations.append(dec)
                print(f"已添加 {dec}")
            else:
                print("無效的裝飾或已添加。")

    # 繪製樹
    print("\n您的客製化聖誕樹：")
    draw_tree(height, shape, color, decorations)

    print("\n聖誕快樂！希望您喜歡您的聖誕樹！")

if __name__ == "__main__":
    main()