from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}


def fetch_page(url):
    """Mengambil konten HTML"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengambil {url}: e")
        return None

def parse_product(article):
    """Parse satu produk dari elemen HTML"""
    try:
        details = article.select_one('.product-details')
        if not details: return None

        title = details.select_one('.product-title').text.strip() if details.select_one('.product-title') else None
        price_container = details.select_one('.price-container')
        price = None
        if price_container:
            price_span = price_container.select_one('span.price')
            price_p = price_container.select_one('p.price')
            price = price_span.text.strip() if price_span else (price_p.text.strip() if price_p else None)
        p_tags = details.select('p')
        rating = None
        colors = None
        size = None
        gender = None

        for p in p_tags:
            text = p.text.strip()
            if 'Rating:' in text and '⭐' in text and '/' in text:
                rating = text.split('⭐')[-1].split('/')[0].strip()
            elif 'Colors' in text:
                colors = text
            elif 'Size:' in text:
                size = text
            elif 'Gender:' in text:
                gender = text
        if not all([title, price, rating, colors, size, gender]):
            return None
        return{
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "Timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        }
    except AttributeError as e:
        print(f"Gagal parsing produk: {str(e)}")
        return None
def scrape_main(base_url="https://fashion-studio.dicoding.dev", total_pages=50, delay=2):
    """Fungsi utama scrape data produk Fashion"""
    all_data=[]
    for page in range(1, total_pages+1):
        url = base_url if page == 1 else f"{base_url}/page{page}"
        print(f"Scrapping halaman: {url}")

        content = fetch_page(url)
        if content:
            soup = BeautifulSoup(content, "html.parser")
            products = soup.select('.collection-card')

            for product in products:
                product_data = parse_product(product)
                if product_data:
                    all_data.append(product_data)
            time.sleep(delay)
        else:
            print(f"Melewatkan halaman {page} akibat masalah fetch")
            continue
    if not all_data:
        raise ValueError("Tidak ada data yang terekstrasi pada website")
    return pd.DataFrame(all_data)
