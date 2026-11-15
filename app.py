import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# 1. KONFIGURASI HALAMAN & STYLING KLASIK
# ---------------------------------------------------------
st.set_page_config(
    page_title="Dashboard Pengamatan Cuaca",
    page_icon="🌤️",
    layout="wide"
)

# Custom CSS Sederhana & Rapi
st.markdown("""
    <style>
    /* Styling Kartu KPI Klasik */
    .kpi-box {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 6px;
        padding: 16px;
        text-align: left;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .kpi-title {
        color: #6B7280;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    .kpi-value {
        color: #111827;
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    /* Layout Container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. LOAD DATA
# ---------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv('dataset_cuaca.csv')
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    
    # Pengelompokan Kategori Kelembaban (Ordinal)
    bins = [0, 70, 85, 100]
    labels = ['Kering (<70%)', 'Ideal (70-85%)', 'Sangat Lembap (>85%)']
    df['Kategori_Kelembaban'] = pd.cut(df['Kelembaban (%)'], bins=bins, labels=labels)
    return df

df = load_data()

# ---------------------------------------------------------
# 3. HEADER
# ---------------------------------------------------------
st.title("🌤️ Laporan Analisis Pengamatan Cuaca")
st.caption("Bedah Kasus 3: Visualisasi & Eksplorasi Dataset Cuaca Wilayah")
st.divider()

# ---------------------------------------------------------
# 4. SIDEBAR FILTER
# ---------------------------------------------------------
st.sidebar.header("Filter Data")

kota_filter = st.sidebar.multiselect(
    "Pilih Kota:",
    options=df['Kota'].unique(),
    default=df['Kota'].unique()
)

kondisi_filter = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca:",
    options=df['Kondisi'].unique(),
    default=df['Kondisi'].unique()
)

min_date = df['Tanggal'].min().date()
max_date = df['Tanggal'].max().date()

date_range = st.sidebar.date_input(
    "Rentang Tanggal Pengamatan:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Terapkan Filter
if len(date_range) == 2:
    start_date, end_date = date_range
    df_filtered = df[
        (df['Kota'].isin(kota_filter)) &
        (df['Kondisi'].isin(kondisi_filter)) &
        (df['Tanggal'].dt.date >= start_date) &
        (df['Tanggal'].dt.date <= end_date)
    ]
else:
    df_filtered = df[(df['Kota'].isin(kota_filter)) & (df['Kondisi'].isin(kondisi_filter))]

# ---------------------------------------------------------
# 5. METRIK KPI KLASIK
# ---------------------------------------------------------
tot_obs = len(df_filtered)
avg_suhu = df_filtered['Suhu (°C)'].mean() if not df_filtered.empty else 0
avg_lemb = df_filtered['Kelembaban (%)'].mean() if not df_filtered.empty else 0
max_suhu = df_filtered['Suhu (°C)'].max() if not df_filtered.empty else 0
min_suhu = df_filtered['Suhu (°C)'].min() if not df_filtered.empty else 0

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Total Pengamatan</div>
            <div class="kpi-value">{tot_obs:,}</div>
        </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Rata-Rata Suhu</div>
            <div class="kpi-value">{avg_suhu:.1f} °C</div>
        </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Rata-Rata Kelembaban</div>
            <div class="kpi-value">{avg_lemb:.1f} %</div>
        </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Suhu Maksimum</div>
            <div class="kpi-value">{max_suhu:.1f} °C</div>
        </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Suhu Minimum</div>
            <div class="kpi-value">{min_suhu:.1f} °C</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------------------------------------------------
# 6. VISUALISASI CHART
# ---------------------------------------------------------
COLOR_THEME = ['#1E3A8A', '#475569', '#0284C7', '#94A3B8', '#334155']

c1, c2 = st.columns(2)

with c1:
    st.subheader("🏙️ Rata-Rata Suhu per Kota (Kategorik Nominal)")
    df_suhu_kota = df_filtered.groupby('Kota')['Suhu (°C)'].mean().reset_index()
    fig_suhu = px.bar(
        df_suhu_kota, x='Kota', y='Suhu (°C)',
        text_auto='.1f', color_discrete_sequence=['#1E3A8A']
    )
    fig_suhu.update_layout(
        plot_bgcolor='#F8FAFC',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="Kota", yaxis_title="Suhu (°C)"
    )
    st.plotly_chart(fig_suhu, use_container_width=True)

with c2:
    st.subheader("🌈 Proporsi Kondisi Cuaca (Kategorik Nominal)")
    df_kon = df_filtered.groupby('Kondisi').size().reset_index(name='Jumlah')
    fig_pie = px.pie(
        df_kon, values='Jumlah', names='Kondisi', hole=0.4,
        color_discrete_sequence=COLOR_THEME
    )
    fig_pie.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_pie, use_container_width=True)

c3, c4 = st.columns(2)

with c3:
    st.subheader("📈 Tren Suhu Harian Rata-rata (Waktu - Interval)")
    df_trend = df_filtered.groupby(['Tanggal', 'Kota'])['Suhu (°C)'].mean().reset_index()
    fig_line = px.line(
        df_trend, x='Tanggal', y='Suhu (°C)', color='Kota',
        color_discrete_sequence=COLOR_THEME
    )
    fig_line.update_layout(
        plot_bgcolor='#F8FAFC',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="", yaxis_title="Suhu (°C)"
    )
    st.plotly_chart(fig_line, use_container_width=True)

with c4:
    st.subheader("💧 Distribusi Tingkat Kelembaban (Ordinal)")
    df_lembab = df_filtered.groupby('Kategori_Kelembaban', observed=False).size().reset_index(name='Jumlah')
    fig_lembab = px.bar(
        df_lembab, x='Kategori_Kelembaban', y='Jumlah',
        text_auto=True, color_discrete_sequence=['#475569']
    )
    fig_lembab.update_layout(
        plot_bgcolor='#F8FAFC',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="Kategori Kelembaban", yaxis_title="Jumlah Pengamatan"
    )
    st.plotly_chart(fig_lembab, use_container_width=True)

c5, c6 = st.columns(2)

with c5:
    st.subheader("🌡️ Distribusi Suhu (Numerik Interval)")
    fig_hist = px.histogram(
        df_filtered, x='Suhu (°C)', nbins=20, color='Kota', marginal="box",
        color_discrete_sequence=COLOR_THEME
    )
    fig_hist.update_layout(
        plot_bgcolor='#F8FAFC',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="Suhu (°C)", yaxis_title="Jumlah"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

with c6:
    st.subheader("💦 Hubungan Suhu vs Kelembaban (Scatter Plot)")
    fig_scat = px.scatter(
        df_filtered, x='Suhu (°C)', y='Kelembaban (%)',
        color='Kota', hover_data=['Kondisi'], opacity=0.75,
        color_discrete_sequence=COLOR_THEME
    )
    fig_scat.update_layout(
        plot_bgcolor='#F8FAFC',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="Suhu (°C)", yaxis_title="Kelembaban (%)"
    )
    st.plotly_chart(fig_scat, use_container_width=True)

# ---------------------------------------------------------
# 7. TABEL LAPORAN RINGKASAN
# ---------------------------------------------------------
st.divider()
st.subheader("📋 Ringkasan Statistik Parameter Cuaca per Kota")

summary_df = df_filtered.groupby('Kota').agg(
    Jumlah_Pengamatan=('Suhu (°C)', 'count'),
    Suhu_Rata_Rata=('Suhu (°C)', 'mean'),
    Suhu_Min=('Suhu (°C)', 'min'),
    Suhu_Max=('Suhu (°C)', 'max'),
    Kelembaban_Rata_Rata=('Kelembaban (%)', 'mean')
).reset_index()

st.dataframe(
    summary_df.style.format({
        'Suhu_Rata_Rata': '{:.1f} °C',
        'Suhu_Min': '{:.1f} °C',
        'Suhu_Max': '{:.1f} °C',
        'Kelembaban_Rata_Rata': '{:.1f} %'
    }),
    use_container_width=True
)

with st.expander("📄 Lihat Data Mentah Cuaca (1.000 Baris)"):
    st.dataframe(df_filtered)

# ---------------------------------------------------------
# 8. FOOTER
# ---------------------------------------------------------
st.divider()
st.markdown(
    "<p style='text-align: center; color: #9CA3AF; font-size: 0.85rem;'>"
    "© 241051020 - <b>ANDRIQO MARIO IMANUEL MANOPO</b> | All Rights Reserved"
    "</p>",
    unsafe_allow_html=True
)