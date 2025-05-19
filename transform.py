import pandas as pd
import numpy as np

def clean_data(raw_data):
    df = pd.DataFrame(raw_data)
    print("Awal:", df.shape)

    # Filter Title valid
    df = df[df['Title'].str.strip().str.lower() != 'unknown product']
    print("Setelah hapus unknown title:", df.shape)

    # Bersihkan Price
    df['Price'] = df['Price'].str.replace(r'[^0-9.]', '', regex=True)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce') * 16000
    print("Setelah konversi price:", df.shape)

    # Bersihkan Rating
    df['Rating'] = df['Rating'].str.extract(r'([\d.]+)')
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    print("Setelah parsing rating:", df.shape)

    # Bersihkan Colors
    df['Colors'] = df['Colors'].str.extract(r'(\d+)')
    df['Colors'] = pd.to_numeric(df['Colors'], errors='coerce')
    print("Setelah parsing colors:", df.shape)

    # Bersihkan Size & Gender
    df['Size'] = df['Size'].str.replace('Size: ', '', regex=False)
    df['Gender'] = df['Gender'].str.replace('Gender: ', '', regex=False)

    # Drop baris null
    df = df.dropna(subset=['Price', 'Rating', 'Title'])
    print("Setelah dropna:", df.shape)

    return df
