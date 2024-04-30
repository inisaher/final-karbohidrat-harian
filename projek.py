import streamlit as st


def hitung_karbohidrat(berat_badan, tinggi_badan, usia):
    # Hitung jumlah karbohidrat harian
    # Sebagai contoh, kita menggunakan rumus sederhana
    karbohidrat_harian = (berat_badan + tinggi_badan) * 2 + (usia / 10)  # Misalnya, 2 gram per kilogram berat badan
    return karbohidrat_harian

def main():
    st.title("Kalkulator Jumlah Karbohidrat Harian")

    st.write('''Aplikasi ini membantu Anda menghitung kebutuhan karbohidrat harian berdasarkan faktor-faktor seperti usia, berat badan, dan tinggi badan.
    Aplikasi membantu ini dalam merencanakan diet seimbang dengan memastikan asupan karbohidrat yang cukup, yang merupakan sumber energi utama bagi tubuh. 
    Serta aplikasi ini dapat menyajikan saran menu makanan (karbohidrat) untuk diet seimbang.
    
    ''')

    # Input nama
    st.header("Perhitungan Untuk Menentukan Kebutuhan Karbohidrat Harian", divider="rainbow")
    nama = st.text_input("Masukkan nama Anda:")

    # Input usia
    usia = st.number_input("Masukkan usia Anda:", min_value=1, max_value=120)

    # Input berat badan
    berat_badan = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0)

    # Input tinggi badan
    tinggi_badan = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=1.0)
#Informasi nama anggota kelompok dan tim
    st.sidebar.title('Informasi Tim')
    st.sidebar.write('Kelompok 5')
    st.sidebar.write('Anggota:')
    st.sidebar.write('- Asyahra Mutia Rojak (2320510)')
    st.sidebar.write('- Chindy Nur Anjani (2320515)')
    st.sidebar.write('- Fadil Zaky As Sammary (2320523)')
    st.sidebar.write('- Muhammad Nur Iqbal (2320537)')
    st.sidebar.write('- Rahil Nafisah (2320549)')
    # Tombol untuk menghitung
    if st.button("Hitung"):
        # Hitung jumlah karbohidrat harian
        import streamlit as st

def hitung_karbohidrat(berat_badan, tinggi_badan, usia, tingkat_aktivitas):
    # Daftar faktor tingkat aktivitas
    faktor_aktivitas = {
        "Sangat Sedikit atau Tidak Aktif": 1.2,
        "Sedikit Aktif (Latihan Ringan/Sekali atau Dua Kali Seminggu)": 1.375,
        "Aktif (Latihan Sedang/Tiga atau Empat Kali Seminggu)": 1.55,
        "Sangat Aktif (Latihan Berat/Lima atau Enam Kali Seminggu)": 1.725,
        "Super Aktif (Latihan Berat & Pekerjaan Fisik Berat/Setiap Hari)": 1.9
    }

    # Hitung jumlah karbohidrat harian
    karbohidrat_harian = (berat_badan + tinggi_badan) * 2 + (usia / 10)  # Misalnya, 2 gram per kilogram berat badan

    # Sesuaikan jumlah karbohidrat berdasarkan tingkat aktivitas
    karbohidrat_harian *= faktor_aktivitas[tingkat_aktivitas]

    return karbohidrat_harian

def main():
    st.title("Kalkulator Jumlah Karbohidrat Harian")

    st.write('''Aplikasi ini membantu Anda menghitung kebutuhan karbohidrat harian berdasarkan faktor-faktor seperti usia, berat badan, tinggi badan, dan tingkat aktivitas fisik.
    Aplikasi membantu ini dalam merencanakan diet seimbang dengan memastikan asupan karbohidrat yang cukup, yang merupakan sumber energi utama bagi tubuh. 
    Serta aplikasi ini dapat menyajikan saran menu makanan (karbohidrat) untuk diet seimbang.
    
    ''')

    # Input nama
    st.header("Perhitungan Untuk Menentukan Kebutuhan Karbohidrat Harian", divider="rainbow")
    nama = st.text_input("Masukkan nama Anda:")

    # Input usia
    usia = st.number_input("Masukkan usia Anda:", min_value=1, max_value=120)

    # Input berat badan
    berat_badan = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0)

    # Input tinggi badan
    tinggi_badan = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=1.0)

    # Input tingkat aktivitas
    tingkat_aktivitas = st.selectbox("Pilih tingkat aktivitas fisik Anda:", [
        "Sangat Sedikit atau Tidak Aktif",
        "Sedikit Aktif (Latihan Ringan/Sekali atau Dua Kali Seminggu)",
        "Aktif (Latihan Sedang/Tiga atau Empat Kali Seminggu)",
        "Sangat Aktif (Latihan Berat/Lima atau Enam Kali Seminggu)",
        "Super Aktif (Latihan Berat & Pekerjaan Fisik Berat/Setiap Hari)"
    ])

    # Informasi nama anggota kelompok dan tim
    st.sidebar.title('Informasi Tim')
    st.sidebar.write('Kelompok 5')
    st.sidebar.write('Anggota:')
    st.sidebar.write('- Asyahra Mutia Rojak (2320510)')
    st.sidebar.write('- Chindy Nur Anjani (2320515)')
    st.sidebar.write('- Fadil Zaky As Sammary (2320523)')
    st.sidebar.write('- Muhammad Nur Iqbal (2320537)')
    st.sidebar.write('- Rahil Nafisah (2320549)')

    # Tombol untuk menghitung
    if st.button("Hitung"):
        # Hitung jumlah karbohidrat harian
        karbohidrat_harian = hitung_karbohidrat(berat_badan, tinggi_badan, usia, tingkat_aktivitas)
        
        st.success(f"Halo {nama}, jumlah karbohidrat harian yang disarankan adalah: {karbohidrat_harian:.2f} gram")

        if berat_badan > 100:
            st.warning("Wow, berat badan Anda cukup tinggi. Pastikan untuk berkonsultasi dengan dokter untuk saran lebih lanjut.")

        if usia > 60:
            st.info("Anda sudah berusia di atas 60 tahun, pastikan untuk mengonsumsi makanan yang kaya nutrisi untuk mendukung kesehatan Anda.")

    st.header("Tabel Informasi Jumlah Karbohidrat", divider="blue")
    st.write("Informasi ini dibuat untuk memberikan informasi kepada pengguna tentang jumlah karbohidrat dalam makanan")

    st.markdown('''
    |Nama Makanan|Jumlah Karbohidrat per 100g  |
    |------------|-----------------------------|
    |Nasi putih  |          28 gram            |
    |Nasi Merah  |          23 gram            |
    |Gandum      |          68 gram            |
    |Kentang     |          22 gram            |
    |Singkong    |          38 gram            |
    |Ubi         |          20 gram            |
    |Jagung      |          36 gram            |

    ''')



    st.header("Tips Diet Karbo Seimbang", divider="red")
    st.write("Informasi ini dibuat untuk memudahkan anda dalam melakukan diet seimbang.")
    st.markdown('''
    Bagaimanakah cara mengontrol asupan karbo harian?
    1. Pilih karbohidrat yang sehat
    2. Kontrol porsi
    3. Pertimbangkan waktu konsumsi
    4. Hindari karbohidrat bersamaan dengan lemak tinggi
    5. Dan pastikan diimbangi dengan melakukan olahraga
    
    
    
    
    ''')

# Call the main function directly
main()

        