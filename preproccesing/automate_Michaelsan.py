# automate_MichaelSan.py
# File ini melakukan preprocessing data e-commerce secara otomatis
# Jalankan: python automate_MichaelSan.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_data(filepath, nrows=50000):
    df = pd.read_csv(filepath, encoding='latin1', nrows=nrows)
    print(f"✅ Data loaded: {df.shape[0]} baris, {df.shape[1]} kolom")
    return df

def remove_invalid_rows(df):
    df = df[df['Quantity'] > 0]
    print(f"✅ Setelah drop Quantity negatif: {df.shape[0]} baris")
    df = df[(df['UnitPrice'] > 0) & (df['UnitPrice'] < 500)]
    print(f"✅ Setelah drop UnitPrice bermasalah: {df.shape[0]} baris")
    df = df.dropna(subset=['CustomerID'])
    print(f"✅ Setelah drop CustomerID kosong: {df.shape[0]} baris")
    df = df.dropna(subset=['Description'])
    print(f"✅ Setelah drop Description kosong: {df.shape[0]} baris")
    df = df.drop_duplicates()
    print(f"✅ Setelah drop duplikat: {df.shape[0]} baris")
    return df

def feature_engineering(df):
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    print(f"✅ Fitur Revenue ditambahkan")
    return df

def encode_categoricals(df):
    le = LabelEncoder()
    df['Country_encoded'] = le.fit_transform(df['Country'])
    print(f"✅ Encoding Country selesai")
    return df

def normalize_features(df):
    scaler = StandardScaler()
    num_cols = ['Quantity', 'UnitPrice', 'Revenue']
    df[num_cols] = scaler.fit_transform(df[num_cols])
    print(f"✅ Normalisasi selesai")
    return df

def save_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"✅ Dataset disimpan ke: {output_path}")
    print(f"✅ Shape final: {df.shape}")

def preprocess(input_path, output_path):
    print("="*50)
    print("🚀 MEMULAI PREPROCESSING OTOMATIS")
    print("="*50)
    df = load_data(input_path)
    df = remove_invalid_rows(df)
    df = feature_engineering(df)
    df = encode_categoricals(df)
    df = normalize_features(df)
    save_data(df, output_path)
    print("="*50)
    print("✅ PREPROCESSING SELESAI!")
    print("="*50)
    return df

if __name__ == "__main__":
    preprocess(
    input_path='data.csv',
    output_path='ecommerce_preprocessing.csv')