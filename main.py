import pprint


def reader():
    sneakers = []
    with open('sneakers.csv', 'r', encoding='utf-8') as file:
        file.readline()
        while True:
            line = file.readline().strip("\n")
            if line == "":
                break
            split = line.split(",")
            title = split[0]
            color_breif = split[1]
            full_price = float(split[2])
            current_price = float(split[3])
            publish_date = split[4]
            sneakers.append(
                {
                    'title': title,
                    'color': color_breif,
                    'full_price': full_price,
                    'current_price': current_price,
                    'publish_date': publish_date,
                }
            )
    return sneakers


def get_order():
    print('Válassz, melyik szempont alapján rendezzem a ciőket?')
    print('1 - title')
    print('2 - color')
    print('3 - full price')
    print('4 - current price')
    print('5 - publish date')
    return int(input('Add meg a lehetőség számát! '))


def main():
    sneakers = reader()
    order_num = get_order()
    keys = {
        1: 'title',
        2: 'color',
        3: 'full_price',
        4: 'current_price',
        5: 'publish_date',
    }
    pprint.pprint(sorted(sneakers, key=lambda item: item[keys[order_num]]))


main()
