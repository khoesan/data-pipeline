import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

def fetch_page_content(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil {url}: {e}")
        return None

def scrape_main(url):
    content = fetch_page_content(url)
    if not content:
        return []
    
    soup = BeautifulSoup(content, 'html.parser')
    products = []

    titles = soup.find_all('h3', class_='product-title')

    for title_tag in titles:
        try:
            title = title_tag.text.strip()
            product_block = title_tag.find_parent()  # coba naik 1 level untuk dapatkan konteks lain

            price_tag = product_block.find('span', class_='price')
            price = price_tag.text.strip() if price_tag else ''

            p_tags = product_block.find_all('p')
            rating = ''
            colors = ''
            size = ''
            gender = ''
            
            for p in p_tags:
                text = p.text.strip()
                if 'Rating' in text:
                    rating = text.replace('Rating: ', '')
                elif 'Colors' in text:
                    colors = text
                elif 'Size' in text:
                    size = text.replace('Size: ', '')
                elif 'Gender' in text:
                    gender = text.replace('Gender: ', '')

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            products.append({
                'Title': title,
                'Price': price,
                'Rating': rating,
                'Colors': colors,
                'Size': size,
                'Gender': gender,
                'Timestamp': timestamp
            })

        except Exception as e:
            print(f"Gagal parsing produk: {e}")
            continue

    return products

def scrape_all_pages(total_pages=50):
    all_products = []
    print("🔍 Mulai scraping data...")

    for page in range(1, total_pages + 1):
        if page == 1:
            url = "https://fashion-studio.dicoding.dev"
        else:
            url = f"https://fashion-studio.dicoding.dev/page{page}"
        
        print(f"Mengambil data dari: {url}")
        page_data = scrape_main(url)
        all_products.extend(page_data)
    
    print(f"Data berhasil diambil: {len(all_products)} baris")
    return all_products

import pandas as pd

def extract_data():
    from utils.extract import scrape_all_pages
    data = scrape_all_pages(total_pages=50)
    return pd.DataFrame(data)