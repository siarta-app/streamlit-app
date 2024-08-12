import streamlit as st

# Judul utama
st.title("Landing Page Aplikasi")

# Deskripsi
st.write("""
Selamat datang di halaman utama! Di sini Anda dapat menemukan kumpulan aplikasi yang telah kami buat. 
Silakan klik link di bawah ini untuk mengakses aplikasi yang Anda butuhkan.
""")

# Daftar aplikasi dengan link
st.subheader("Kumpulan Aplikasi:")

st.markdown("""
1. [Aplikasi Analisis Data](https://your-app-url.com/analysis) - Alat untuk analisis data dan visualisasi.
2. [Aplikasi Prediksi Harga](https://your-app-url.com/prediction) - Aplikasi untuk prediksi harga menggunakan machine learning.
3. [Aplikasi Pengolahan Teks](https://your-app-url.com/text-processing) - Aplikasi untuk pengolahan dan analisis teks.
4. [Aplikasi Pengelolaan Proyek](https://your-app-url.com/project-management) - Aplikasi untuk mengelola dan melacak kemajuan proyek.
""")

# Pesan penutup
st.write("""
Kami terus mengembangkan lebih banyak aplikasi untuk memenuhi kebutuhan Anda. 
Jangan ragu untuk mengunjungi halaman ini lagi untuk melihat pembaruan dan aplikasi baru.
""")

