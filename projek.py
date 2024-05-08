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

def hitung_kalori(karbohidrat, protein, lemak):
    # Set nilai kalori per gram untuk karbohidrat, protein, dan lemak
    kalori_per_gram = {
        "karbohidrat": 4,
        "protein": 4,
        "lemak": 9
    }

    # Hitung total kalori berdasarkan asupan karbohidrat, protein, dan lemak
    total_kalori = (karbohidrat * kalori_per_gram["karbohidrat"]) + (protein * kalori_per_gram["protein"]) + (lemak * kalori_per_gram["lemak"])

    return total_kalori

def main():
    st.sidebar.title('Navigasi')
    page = st.sidebar.radio("Pilih Halaman", ["Perkenalan Kelompok", "Pengetahuan Kalkulator Karbohidrat", "Perhitungan Kebutuhan Karbohidrat", "Informasi Hitung Kalori", "Informasi Hitung Kandungan Gula", "Daftar Informasi Sumber Karbohidrat", "Tips Diet Karbo Seimbang"])

    if page == "Perkenalan Kelompok":
        st.title("Perkenalan Kelompok")
        # Garis pembatas berwarna-warni
        st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
        st.write("Kelompok 5")
        st.write("Anggota:")
        st.write("- Asyahra Mutia Rojak (2320510)")
        st.write("- Chindy Nur Anjani (2320515)")
        st.write("- Fadil Zaky As Sammary (2320523)")
        st.write("- Muhammad Nur Iqbal (2320537)")
        st.write("- Rahil Nafisah (2320549)")

    elif page == "Pengetahuan Kalkulator Karbohidrat":
        st.title("Pengetahuan Kalkulator Karbohidrat")
        # Garis pembatas berwarna-warni
        st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
        st.write('''Aplikasi ini membantu Anda menghitung kebutuhan karbohidrat harian berdasarkan faktor-faktor seperti usia, berat badan, tinggi badan, dan tingkat aktivitas fisik.
        Aplikasi membantu ini dalam merencanakan diet seimbang dengan memastikan asupan karbohidrat yang cukup, yang merupakan sumber energi utama bagi tubuh. 
        Serta aplikasi ini dapat menyajikan saran menu makanan (karbohidrat) untuk diet seimbang.''')
        st.write("Karbohidrat adalah salah satu dari tiga macronutrien utama bersama dengan protein dan lemak. Karbohidrat merupakan sumber energi utama bagi tubuh manusia.")
        st.write("Karbohidrat dipecah menjadi glukosa oleh tubuh, yang kemudian digunakan sebagai bahan bakar untuk otak, otot, dan sel-sel tubuh lainnya.")
        st.write("Ada dua jenis utama karbohidrat: sederhana dan kompleks. Karbohidrat sederhana terdiri dari molekul gula tunggal atau gula sederhana, sementara karbohidrat kompleks terdiri dari molekul gula yang lebih kompleks dan serat.")
        st.write("Sumber karbohidrat yang sehat termasuk biji-bijian utuh (seperti beras merah dan quinoa), sayuran berdaun hijau, buah-buahan, serta kacang-kacangan dan biji-bijian.")
        st.write("Penting untuk memperhatikan jenis karbohidrat yang dikonsumsi. Karbohidrat kompleks cenderung lebih sehat karena mereka mengandung serat yang membantu mengatur gula darah dan memberikan rasa kenyang lebih lama.")
        st.write("Meskipun karbohidrat penting untuk energi, jumlah dan jenis karbohidrat yang tepat yang harus dikonsumsi akan bervariasi tergantung pada kebutuhan energi individu, tingkat aktivitas, dan tujuan kesehatan.")

    elif page == "Perhitungan Kebutuhan Karbohidrat":
        st.title("Perhitungan Kebutuhan Karbohidrat")
        # Garis pembatas berwarna-warni
        st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
        nama = st.text_input("Masukkan nama Anda:")
        usia = st.number_input("Masukkan usia Anda:", min_value=1, max_value=120)
        berat_badan = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0)
        tinggi_badan = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=1.0)
        tingkat_aktivitas = st.selectbox("Pilih tingkat aktivitas fisik Anda:", [
            "Sangat Sedikit atau Tidak Aktif",
            "Sedikit Aktif (Latihan Ringan/Sekali atau Dua Kali Seminggu)",
            "Aktif (Latihan Sedang/Tiga atau Empat Kali Seminggu)",
            "Sangat Aktif (Latihan Berat/Lima atau Enam Kali Seminggu)",
            "Super Aktif (Latihan Berat & Pekerjaan Fisik Berat/Setiap Hari)"
        ])

        if st.button("Hitung"):
            karbohidrat_harian = hitung_karbohidrat(berat_badan, tinggi_badan, usia, tingkat_aktivitas)
            st.success(f"Halo {nama}, jumlah karbohidrat harian yang disarankan adalah: {karbohidrat_harian:.2f} gram")
            if berat_badan > 100:
                st.warning("Wow, berat badan Anda cukup tinggi. Pastikan untuk berkonsultasi dengan dokter untuk saran lebih lanjut.")
            if usia > 60:
                st.info("Anda sudah berusia di atas 60 tahun, pastikan untuk mengonsumsi makanan yang kaya nutrisi untuk mendukung kesehatan Anda.")

    elif page == "Informasi Hitung Kalori":
        st.title("Informasi Hitung Kalori")
        # Garis pembatas berwarna-warni
        st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
        st.write("Perhitungan total kalori berdasarkan asupan karbohidrat, protein, dan lemak")
        karbohidrat = st.number_input("Masukkan jumlah karbohidrat (gram):", min_value=0.0)
        protein = st.number_input("Masukkan jumlah protein (gram):", min_value=0.0)
        lemak = st.number_input("Masukkan jumlah lemak (gram):", min_value=0.0)

        if st.button("Hitung"):
            total_kalori = hitung_kalori(karbohidrat, protein, lemak)
            st.success(f"Total kalori harian Anda adalah: {total_kalori:.2f} kalori")

    elif page == "Informasi Hitung Kandungan Gula":
        st.title("Informasi Hitung Kandungan Gula")
        # Garis pembatas berwarna-warni
        st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
        st.write("Perhitungan gula berdasarkan jumlah karbohidrat harian yang disarankan")
        nama = st.text_input("Masukkan nama Anda:")
        usia = st.number_input("Masukkan usia Anda:", min_value=1, max_value=120)
        berat_badan = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0)
        tinggi_badan = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=1.0)
        tingkat_aktivitas = st.selectbox("Pilih tingkat aktivitas fisik Anda:", [
            "Sangat Sedikit atau Tidak Aktif",
            "Sedikit Aktif (Latihan Ringan/Sekali atau Dua Kali Seminggu)",
            "Aktif (Latihan Sedang/Tiga atau Empat Kali Seminggu)",
            "Sangat Aktif (Latihan Berat/Lima atau Enam Kali Seminggu)",
            "Super Aktif (Latihan Berat & Pekerjaan Fisik Berat/Setiap Hari)"
        ])

        if st.button("Hitung"):
            karbohidrat_harian = hitung_karbohidrat(berat_badan, tinggi_badan, usia, tingkat_aktivitas)
            gula_harian = hitung_gula(karbohidrat_harian)
            st.success(f"Halo {nama}, jumlah gula harian yang disarankan adalah: {gula_harian:.2f} gram")

    elif page == "Daftar Informasi Sumber Karbohidrat":
        st.title("Daftar Informasi Sumber Karbohidrat")
        # Garis pembatas berwarna-warni
        st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
        st.write("Informasi ini dibuat untuk memberikan informasi kepada pengguna tentang jumlah karbohidrat dalam makanan, termasuk kandungan gula dan serat.")
        nama_makanan = st.selectbox("Pilih nama makanan:", ["Nasi putih", "Nasi Merah", "Gandum", "Kentang", "Singkong", "Ubi", "Jagung"])

        if nama_makanan == "Nasi putih":
            st.markdown('''
            |Nama Makanan|Jumlah Karbohidrat per 100g|Jumlah Gula per 100g|Jumlah Serat per 100g|Kalori per 100g|
            |------------|---------------------------|---------------------|----------------------|---------------|
            |Nasi putih  |          28 gram          |        0 gram       |        0 gram        |     130 kcal  |
            ''')
        elif nama_makanan == "Nasi Merah":
            st.markdown('''
            |Nama Makanan|Jumlah Karbohidrat per 100g|Jumlah Gula per 100g|Jumlah Serat per 100g|Kalori per 100g|
            |------------|---------------------------|---------------------|----------------------|---------------|
            |Nasi Merah  |          23 gram          |        0 gram       |        1 gram        |     111 kcal  |
            ''')
        elif nama_makanan == "Gandum":
            st.markdown('''
            |Nama Makanan|Jumlah Karbohidrat per 100g|Jumlah Gula per 100g|Jumlah Serat per 100g|Kalori per 100g|
            |------------|---------------------------|---------------------|----------------------|---------------|
            |Gandum      |          68 gram          |        0 gram       |        12 gram       |     329 kcal  |
            ''')
        elif nama_makanan == "Kentang":
            st.markdown('''
            |Nama Makanan|Jumlah Karbohidrat per 100g|Jumlah Gula per 100g|Jumlah Serat per 100g|Kalori per 100g|
            |------------|---------------------------|---------------------|----------------------|---------------|
            |Kentang     |          22 gram          |        1 gram       |        2 gram        |      77 kcal  |
            ''')
        elif nama_makanan == "Singkong":
            st.markdown('''
            |Nama Makanan|Jumlah Karbohidrat per 100g|Jumlah Gula per 100g|Jumlah Serat per 100g|Kalori per 100g|
            |------------|---------------------------|---------------------|----------------------|---------------|
            |Singkong    |          38 gram          |        3 gram       |        3 gram        |     160 kcal  |
            ''')
        elif nama_makanan == "Ubi":
            st.markdown('''
            |Nama Makanan|Jumlah Karbohidrat per 100g|Jumlah Gula per 100g|Jumlah Serat per 100g|Kalori per 100g|
            |------------|---------------------------|---------------------|----------------------|---------------|
            |Ubi         |          20 gram          |        1 gram       |        3 gram        |      86 kcal  |
            ''')
        elif nama_makanan == "Jagung":
            st.markdown('''
            |Nama Makanan|Jumlah Karbohidrat per 100g|Jumlah Gula per 100g|Jumlah Serat per 100g|Kalori per 100g|
            |------------|---------------------------|---------------------|----------------------|---------------|
            |Jagung      |          36 gram          |        6 gram       |        2 gram        |     86 kcal   |
            ''')

    elif page == "Tips Diet Karbo Seimbang":
        st.title("Tips Diet Karbo Seimbang")
        # Garis pembatas berwarna-warni
        st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
        st.write("Informasi ini dibuat untuk memudahkan anda dalam melakukan diet seimbang.")
        st.markdown('''
        Bagaimanakah cara mengontrol asupan karbo harian?
        1. Pilih karbohidrat yang sehat
        2. Kontrol porsi
        3. Pertimbangkan waktu konsumsi
        4. Hindari karbohidrat bersamaan dengan lemak tinggi
        5. Dan pastikan diimbangi dengan melakukan olahraga
        ''')

if __name__ == "__main__":
    main()
