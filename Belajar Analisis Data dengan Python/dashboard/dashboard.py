import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
@st.cache_data
def load_data():
    data = pd.read_csv("dashboard/main_data.csv")
    return data

df_bike_all = load_data()

# Sidebar Navigation
st.sidebar.title("Bike Sharing Dashboard")
page = st.sidebar.radio("Pilih Visualisasi", ["Overview Data", "Pengaruh Cuaca", "Distribusi Penyewaan", "Tren Peminjaman"])

if page == "Overview Data":
    st.title("Overview Data")
    st.write("### Dataframe Bike Sharing")
    show_data = st.radio("Tampilkan Data:", ["Head (5 data)", "Seluruh Data"])
    if show_data == "Head (5 data)":
        st.dataframe(df_bike_all.head())
    else:
        st.dataframe(df_bike_all)

    st.write("Jumlah Data:", df_bike_all.shape[0])
    st.write("Jumlah Kolom:", df_bike_all.shape[1])

    # Tambahan informasi
    st.write("### Deskripsi Statistik Data")
    st.dataframe(df_bike_all.describe())

    # Missing Values
    st.write("### Jumlah Missing Values")
    missing_values = df_bike_all.isnull().sum()
    st.dataframe(missing_values[missing_values > 0])

    # Duplikat
    st.write("### Jumlah Data Duplikat")
    st.write(df_bike_all.duplicated().sum(), "data duplikat")

    # Tipe Data
    st.write("### Tipe Data Kolom")
    st.dataframe(df_bike_all.dtypes)


# Pengaruh Cuaca
elif page == "Pengaruh Cuaca":
    st.title("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    st.write("### Penyewaan Berdasarkan Kondisi Cuaca")

    weather_order = {1: "Cerah", 2: "Mendung", 3: "Hujan Ringan", 4: "Hujan Lebat"}
    df_bike_all["weathersit"] = df_bike_all["weathersit"].replace(weather_order)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df_bike_all, x="weathersit", y="cnt", palette="coolwarm")
    plt.title(f"Pengaruh Penyewaan Sepeda Berdasarkan Cuaca (Per-Jam)")
    plt.xlabel("Cuaca")
    plt.ylabel("Rata-rata Penyewaan Sepeda")
    st.pyplot(fig)

# Distribusi Penyewaan
elif page == "Distribusi Penyewaan":
    st.title("Distribusi Penyewaan Sepeda")
    st.write("### Penyewaan pada Hari Kerja vs Akhir Pekan")

    day_type = st.radio("Pilih Jenis Hari:", ["Weekday", "Weekend"])
    user_type = st.radio("Pilih Jenis Pengguna:", ["Total", "Casual", "Registered"])
    day_map = {"Weekday": 1, "Weekend": 0}
    selected_day = day_map[day_type]

    filtered_df = df_bike_all[df_bike_all["workingday"] == selected_day]

    target_column = "cnt"
    if user_type == "Casual":
        target_column = "casual"
    elif user_type == "Registered":
        target_column = "registered"

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=filtered_df.groupby("hr")[target_column].sum().reset_index(), x="hr", y=target_column, marker="o")
    plt.title(f"Distribusi Penyewaan Sepeda pada {day_type} - {user_type}")
    plt.xlabel("Jam")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

# Tren Peminjaman
elif page == "Tren Peminjaman":
    st.title("Tren Peminjaman Sepeda")
    st.write("### Penyewaan Sepeda Berdasarkan Jam")

    user_type = st.radio("Pilih Jenis Pengguna (Tren):", ["Total", "Casual", "Registered"])

    target_column = "cnt"
    if user_type == "Casual":
        target_column = "casual"
    elif user_type == "Registered":
        target_column = "registered"

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df_bike_all.groupby("hr")[target_column].sum().reset_index(), x="hr", y=target_column, marker="o", color="green")
    plt.title(f"Tren Peminjaman Sepeda Berdasarkan Jam - {user_type}")
    plt.xlabel("Jam")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

st.sidebar.info("Bike Sharing Dashboard.")

