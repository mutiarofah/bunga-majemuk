import streamlit as st
import time

def calculate_compound_interest(principal, annual_rate, compounding_frequency, years):
    """Menghitung bunga majemuk."""
    # Konversi tingkat bunga tahunan menjadi desimal
    r = annual_rate / 100
    # Hitung jumlah periode compounding
    n = compounding_frequency
    # Hitung total tahun
    t = years

    # Rumus bunga majemuk: A = P (1 + r/n)^(nt)
    amount = principal * (1 + r / n)(n * t)
    interest_earned = amount - principal
    return amount, interest_earned

def main():
    st.set_page_config(page_title="Kalkulator Bunga Majemuk", page_icon="💰", layout="centered")

    st.title("💰 Kalkulator Bunga Majemuk 💰")
    st.markdown("""
        <p style='text-align: center; font-size: 18px;'>
            Lihat bagaimana uang Anda bertumbuh dengan kekuatan bunga majemuk!
        </p>
    """, unsafe_allow_html=True)

    st.sidebar.header("Input Investasi Anda")

    principal = st.sidebar.number_input(
        "Modal Awal (Rp)",
        min_value=100_000,
        max_value=1_000_000_000,
        value=10_000_000,
        step=100_000,
        help="Jumlah uang awal yang diinvestasikan atau dipinjam."
    )
    annual_rate = st.sidebar.number_input(
        "Tingkat Bunga Tahunan (%)",
        min_value=0.1,
        max_value=100.0,
        value=5.0,
        step=0.1,
        format="%.1f",
        help="Tingkat bunga per tahun dalam persentase."
    )
    compounding_frequency = st.sidebar.selectbox(
        "Frekuensi Penggabungan Bunga",
        {
            "Tahunan (1x/tahun)": 1,
            "Semi-Tahunan (2x/tahun)": 2,
            "Kuartalan (4x/tahun)": 4,
            "Bulanan (12x/tahun)": 12,
            "Harian (365x/tahun)": 365
        },
        format_func=lambda x: list(x.keys())[list(x.values()).index(x)], # Menampilkan nama frekuensi
        help="Seberapa sering bunga dihitung dan ditambahkan ke pokok."
    )
    years = st.sidebar.number_input(
        "Jangka Waktu (Tahun)",
        min_value=1,
        max_value=100,
        value=10,
        step=1,
        help="Lama waktu investasi dalam tahun."
    )

    st.markdown("---")

    if st.button("Hitung Bunga Majemuk"):
        with st.spinner("Menghitung potensi pertumbuhan uang Anda..."):
            time.sleep(2) # Simulasi loading

        final_amount, interest_earned = calculate_compound_interest(
            principal, annual_rate, compounding_frequency, years
        )

        st.subheader("🎉 Hasil Perhitungan 🎉")

        st.info(f"Modal Awal Anda: *Rp {principal:,.0f}*")
        st.info(f"Tingkat Bunga Tahunan: *{annual_rate:.1f}%*")
        st.info(f"Jangka Waktu: *{years} tahun*")
        st.success(f"Jumlah Akhir Setelah {years} Tahun: *Rp {final_amount:,.0f}*")
        st.success(f"Total Bunga yang Diperoleh: *Rp {interest_earned:,.0f}*")

        st.markdown("---")
        st.subheader("Visualisasi Pertumbuhan (Animasi Sederhana)")

        # Animasi pertumbuhan bunga
        animation_placeholder = st.empty()
        
        # Simulasi pertumbuhan tahun per tahun (sederhana)
        current_amount = principal
        for year in range(1, years + 1):
            # Hitung pertumbuhan untuk tahun ini saja (bukan dari awal)
            yearly_growth = current_amount * (annual_rate / 100)
            
            # Ini adalah simulasi sederhana untuk visualisasi,
            # tidak seakurat perhitungan bunga majemuk total
            # untuk setiap tahun secara terpisah dari rumus awal
            current_amount += yearly_growth / compounding_frequency # bagi per frekuensi agar visual lebih smooth
            
            # Batasi tampilan agar tidak terlalu cepat jika tahun banyak
            if years <= 20 or year % 2 == 0 or year == years: # Tampilkan setiap tahun jika <20, atau setiap 2 tahun, atau tahun terakhir
                animation_placeholder.markdown(
                    f"<h3 style='text-align: center;'>Tahun {year}: Rp {current_amount:,.0f} {'📈' * (year % 5 + 1)}</h3>",
                    unsafe_allow_html=True
                )
                time.sleep(0.2 if years < 10 else 0.05) # Atur kecepatan animasi
            
            if year == years:
                animation_placeholder.markdown(
                    f"<h2 style='text-align: center;'>🎉 Investasi Bertumbuh! 🎉</h2>",
                    unsafe_allow_html=True
                )
                time.sleep(1)
                animation_placeholder.empty()

        st.success("Perhitungan dan visualisasi selesai! Selamat merencanakan keuangan Anda! ✨")

        st.markdown("---")
        st.subheader("Mengapa Bunga Majemuk Itu Penting?")
        st.markdown("""
            Bunga majemuk sering disebut sebagai *"keajaiban dunia kedelapan"* karena kemampuannya membuat uang Anda bertumbuh secara eksponensial dari waktu ke waktu.
            Bunga yang Anda peroleh ditambahkan ke modal awal Anda, dan kemudian bunga di periode berikutnya dihitung dari jumlah yang lebih besar tersebut. Ini menciptakan efek bola salju yang dapat sangat menguntungkan dalam jangka panjang.
            Semakin awal Anda memulai, semakin besar potensi pertumbuhan investasi Anda!
        """)


if _name_ == "_main_":
    main()
