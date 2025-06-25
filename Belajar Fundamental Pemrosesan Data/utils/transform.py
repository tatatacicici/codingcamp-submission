import pandas as pd
import re

def clean_data(shop_df):
    """Menghapus duplikat dan nilai null dari DataFrame"""
    try:
        shop_df = shop_df.drop_duplicates()
        shop_df = shop_df.dropna()
        if shop_df.empty:
            raise ValueError('DataFrame menjadi kosong setelah membersihkan duplikat dan nilai null')
        return shop_df
    except Exception as e:
        raise ValueError(f'Gagal membersihkan data: {str(e)}')
def clean_price(price):
    """Mengkonversi dari USD ke IDR (1 USD = 16.OOO IDR)"""
    try:
        if not price or price == "" or 'Price Unavailable'in price:
            return None
        price_clean = re.sub(r'[^\d.]', '', price)
        return float(price_clean) * 16000
    except (ValueError, TypeError) as e:
        print(f"Gagal membersihkan data price '{price}': {str(e)}")
        return None
def clean_rating(rating):
    """Mengkonversi Rating menjadi float"""
    try:
        if not rating or 'Invalid Rating/5'in rating or 'Not Rated'in rating or 'Invalid Rating'in rating:
            return None
        match = re.search(r'(\d*\.?\d*)', rating)
        return float(match.group(0)) if match else None
    except (ValueError, TypeError) as e:
        print(f"Gagal membersihkan data rating '{rating}': {str(e)}")
        return None
def clean_colors(colors):
    """Membersihkan data colors"""
    try:
        if not colors in colors:
            return None
        match = re.search(r'(\d+)', colors)
        return int(match.group(0)) if match else None
    except (ValueError, TypeError) as e:
        print(f"Gagal membersihkan data colors '{colors}': {str(e)}")
        return None
def clean_size(size):
    """Membersihkan data size"""
    try:
        if not size or not isinstance(size, str):
            return None
        return size.replace('Size: ', '').strip()
    except AttributeError as e:
        print(f"Gagal membersihkan data size '{size}': {str(e)}")
        return None
def clean_gender(gender):
    """Membersihkan data gender"""
    try:
        if not gender or 'Unknown' in gender:
            return None
        return gender.replace('Gender: ', '').strip()
    except AttributeError as e:
        print(f"Gagal membersikan data gender '{gender}': {str(e)}")
        return None
def validate_title(title):
    """Memastika nama produk sesuai"""
    try:
        if not title or 'Unknown Product' in title:
            return None
        return title
    except AttributeError as e:
        print(f"Gagal membersihkan data title '{title}': {str(e)}")
        return None
def transform_data(shop_df):
    """Membersihkan data"""
    try:
        shop_df = clean_data(shop_df)

        #mentransformasikan tiap tiap kolom
        shop_df['Price'] = shop_df['Price'].apply(clean_price)
        shop_df['Rating'] = shop_df['Rating'].apply(clean_rating)
        shop_df['Colors'] = shop_df['Colors'].apply(clean_colors)
        shop_df['Size'] = shop_df['Size'].apply(clean_size)
        shop_df['Gender'] = shop_df['Gender'].apply(clean_gender)
        shop_df['Title'] = shop_df['Title'].apply(validate_title)

        #menghapus baris dengan nilai null setelah transformasi
        shop_df = shop_df.dropna()
        if shop_df.empty:
            raise ValueError("DataFrame kosong setelah proses transformasi")

        #memastikan tipe data nya benar
        shop_df = shop_df.astype({
            'Title':'object',
            'Price':'float64',
            'Rating':'float64',
            'Colors':'int64',
            'Size':'object',
            'Gender':'object'
        })

        return shop_df
    except Exception as e:
        raise ValueError(f"Gagal transformasi data: {str(e)}")
