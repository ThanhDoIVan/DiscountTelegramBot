import requests
import json
import os

headers = {
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}

def get_page(url):
    req = requests.get(url, headers=headers)

    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(req.text)

def get_json(url):
    req = requests.get(url, headers=headers)

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(req.json(), file, indent=4, ensure_ascii=False)

def collect_data_men_shoes():
    req = requests.get(url='https://www.lamoda.by/c/2981/shoes-krossovk-kedy-muzhskie/?page=2&json=1', headers=headers)

    """ Для всех страниц """
    data = req.json()
    pagination_count = data.get('payload').get('pagination').get('pages')
    print(pagination_count)
    """ ---------------- """

    result_data = []
    count = 0
    # for page_count in range(1, pagination_count + 1):
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/2981/shoes-krossovk-kedy-muzhskie/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")
    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_men_shoes.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_men_outerwear():
    result_data = []
    count = 0
    # for page_count in range(1, pagination_count + 1):
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/479/clothes-muzhskaya-verkhnyaya-odezhda/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_men_outerwear.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_men_pullover():
    result_data = []
    count = 0
    # for page_count in range(1, pagination_count + 1):
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/497/clothes-muzhskoy-trikotazh/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_men_pullover.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_men_sweatshirts():
    result_data = []
    count = 0
    # for page_count in range(1, pagination_count + 1):
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/2508/clothes-tolstovki-i-olimpiyki/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_men_sweatshirts.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_men_pants():
    result_data = []
    count = 0
    # for page_count in range(1, pagination_count + 1):
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/517/clothes-muzhskie-bryuki/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_men_pants.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_men_shirts():
    result_data = []
    count = 0
    # for page_count in range(1, pagination_count + 1):
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/515/clothes-muzhskie-rubashki-i-sorochki/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_men_shirts.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_men_accessories():
    result_data = []
    count = 0
    # for page_count in range(1, pagination_count + 1):
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/559/accs-muzhskieaksessuary/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_men_accessories.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)


'''-----------------WOMEN-------------------'''

def collect_data_women_shoes():
    req = requests.get(url='https://www.lamoda.by/c/2981/shoes-krossovk-kedy-muzhskie/?page=2&json=1', headers=headers)

    """ Для всех страниц """
    data = req.json()
    pagination_count = data.get('payload').get('pagination').get('pages')
    print(pagination_count)
    """ ---------------- """

    result_data = []
    count = 0
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/2968/shoes-krossovki-kedy/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_women_shoes.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_women_shirts():
    result_data = []
    count = 0
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/2478/clothes-futbolki/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_women_shirts.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_women_overalls():
    result_data = []
    count = 0
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/4184/clothes-coveralls/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_women_overalls.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_women_dress():
    result_data = []
    count = 0
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/369/clothes-platiya/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_women_dress.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_women_hoodies():
    result_data = []
    count = 0
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/2474/clothes-tolstovki-olimpiyki/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_women_hoodies.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_women_trousers():
    result_data = []
    count = 0
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/401/clothes-bryuki-shorty-kombinezony/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_women_trousers.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def collect_data_women_accessories():
    result_data = []
    count = 0
    for page_count in range(1, 5):
        url = f'https://www.lamoda.by/c/557/accs-zhenskieaksessuary/?page={page_count}&json=1'
        req = requests.get(url, headers=headers)

        data = req.json()
        products = data.get('payload').get('products')

        for product in products:
            if 'discount' in product:
                count += 1
                sizes = []
                for size in product.get('sizes'):
                    if size.get('is_available'):
                        sizes.append(size.get('brand_size'))

                if 'model_name' in product:
                    model_name = product.get('model_name')
                else:
                    model_name = product.get('name')

                result_data.append(
                    {
                        'model_name': model_name,
                        'link': f"https://www.lamoda.by/p/{product.get('sku')}",
                        'brand_name': product.get('brand').get('name'),
                        'available_sizes': sizes,
                        'old_price': product.get('old_price_amount'),
                        'price': product.get('price_amount'),
                        'discount': product.get('discount')
                    }
                )

                print(f"Iteration #{count}")

    if not os.path.exists(f"data/"):
        os.mkdir(f"data/")

    with open('data/result_data_women_accessories.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)


def main():
    pass
    # get_page(url='https://www.lamoda.by/c/2981/shoes-krossovk-kedy-muzhskie/')
    # get_json('https://www.lamoda.by/c/2981/shoes-krossovk-kedy-muzhskie/?page=2&json=1')

    # collect_data_men_shoes()
    # collect_data_women_shoes()
    collect_data_women_overalls()

if __name__ == '__main__':
    main()