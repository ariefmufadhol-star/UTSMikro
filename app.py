import streamlit as st
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Electronics Web Project - UTS", page_icon="⚡", layout="centered")

# --- STYLE CSS AMAN (STRIP HTML UNTUK PYTHON 3.14) ---
st.html("""
    <style>
    /* Paksa Background Aplikasi Jadi Hitam Pekat */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #0b0f19 !important;
        color: #e2e8f0 !important;
    }
    /* Warna Teks Judul Utama */
    h1, h2, h3 {
        color: #38bdf8 !important;
    }
    /* Kotak Info di Tab Home */
    div.stAlert {
        background-color: #1f2937 !important;
        border-left: 5px solid #00ffcc !important;
        color: #e2e8f0 !important;
    }
    /* Sekat Kotak untuk Setiap Sub-Judul (Profile) */
    .sub-section {
        background-color: #1f2937;
        color: #00ffcc;
        padding: 8px 15px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 16px;
        margin-top: 20px;
        margin-bottom: 15px;
        border-left: 4px solid #38bdf8;
    }
    /* Teks Sorotan Neon */
    .neon-text {
        color: #00ffcc;
        font-weight: bold;
    }
    </style>
""")

# --- NAVIGASI TAB ---
tab1, tab2 = st.tabs(["⌁ HOME", "⌁ PROFILE"])

# ==================== 1. TAB HOME ====================
with tab1:
    st.markdown("<h1 style='text-align: center;'>Welcome to the Core Node</h1>", unsafe_allowed_html=True)
    st.markdown("<p style='text-align: center; color: #00ffcc; font-weight: bold;'>STUDENT ID: 2420307004</p>", unsafe_allowed_html=True)
    st.write("")
    
    st.info("""
    This digital platform is fully driven by the **Streamlit Framework**, synthesized perfectly to fulfill the Web Programming Midterm Exam requirements.
    
    Think of this framework as the **Microcontroller** of this website, routing commands and managing signals efficiently.
    
    Execute the tab panel navigation above to switch the logic states of this application.
    """)

# ==================== 2. TAB PROFILE ====================
with tab2:
    st.markdown("<h1 style='text-align: center;'>ARIEF MUFADHOL</h1>", unsafe_allowed_html=True)
    st.markdown("<p style='text-align: center; color: #00ffcc; font-weight: bold;'>STUDENT ID: 2420307004 • G24' ELECTRONICS</p>", unsafe_allowed_html=True)
    
    col_left, col_right = st.columns([1.2, 2])
    
    # --- KOLOM KIRI (CONTACT & ABILITY) ---
    with col_left:
        st.markdown("<div class='sub-section'>📌 CONTACT</div>", unsafe_allowed_html=True)
        st.write("""
        📞 +62 8958 0033 0007  
        ✉ ariefmufadhol@gmail.com  
        📸 @arief_mfdhl  
        📍 Jl. Telaga Sari No.7  
        👶 Padang, 15/10/2005  
        ⚡ <span class='neon-text'>Active Student</span>  
        📁 Streamlit Web Project v1.0
        """, unsafe_allowed_html=True)
        
        st.markdown("<div class='sub-section'>🛠️ ABILITY</div>", unsafe_allowed_html=True)
        st.write("""
        - Embedded System Programming
        - Arduino
        - Wiring Diagram
        - Electronics Instrumentation
        - Layout Design Eagle Autodesk
        - Troubleshooting
        - Team Work
        """)
        
        st.markdown("<div class='sub-section'>💼 EXPERIENCE</div>", unsafe_allowed_html=True)
        st.markdown("**Magang di PT. Panasonic Manufacturing Indonesia**")
        st.caption("2022 | Refrigerator Injection Moulding Operator")

    # --- KOLOM KANAN (ABOUT ME, EDUCATION, ACHIEVEMENT) ---
    with col_right:
        st.markdown("<div class='sub-section'>ℹ️ ABOUT ME</div>", unsafe_allowed_html=True)
        st.write("Experienced individuals specializing in research and technology. Experienced in robotics and excelling in developing innovations.")
        
        st.markdown("<div class='sub-section'>🎓 EDUCATION</div>", unsafe_allowed_html=True)
        st.markdown("**Politeknik Caltex Riau** \n*2024 - Now | Electronics Engineering*")
        st.markdown("**Semen Padang Senior High School** \n*2021 - 2024 | Electronics Engineering*")
        st.markdown("**11 Junior High School** \n*2018 - 2021*")
        st.markdown("**Semen Padang Elementary School** \n*2012 - 2018*")
        
        st.markdown("<div class='sub-section'>🏆 ACHIEVEMENT</div>", unsafe_allowed_html=True)
        st.markdown("- **National Student Competition (2023)**: Medallion For Excellence")
        st.markdown("- **Provincial Student Competency Competition (2023)**: 1st Place")
        st.markdown("- **City Level Student Competency Competition (2023)**: 1st Place")
        st.markdown("- **Sumatra Level Robotic Line Follower Competition (2025)**: 2nd Place")
        st.markdown("- **National Level Robotic Line Follower Competition (2025)**: Best Spirit And Best Design")

    st.divider()

    # --- SECTION BRAND (PORTFOLIO ROBOT) ---
    st.markdown("<div class='sub-section' style='text-align: center;'>🤖 BRAND - Competition Line Follower Robot</div>", unsafe_allowed_html=True)
    st.write("""
    This is an exclusive high-performance PCB hardware routing architecture designed for high-speed tracking optimization. 
    Featuring an aerodynamic <span class='neon-text'>Aerodynamic Sensor Array Board</span> and an integrated 
    <span class='neon-text'>IPS 240x240 Display Mainboard</span> for high-efficiency logic data streaming and hardware engineering layout customization.
    """, unsafe_allowed_html=True)
    
    # Grid Gambar Portofolio PCB Elektronik Lu
    col_img1, col_img2 = st.columns(2)
    
    with col_img1:
        if os.path.exists("sensor.jpeg"):
            st.image("sensor.jpeg", caption="Sensor Array PCB")
        else:
            st.warning("File sensor.jpeg tidak ditemukan")
            
    with col_img2:
        if os.path.exists("mainboard.jpeg"):
            st.image("mainboard.jpeg", caption="Mainboard PCB")
        else:
            st.warning("File mainboard.jpeg tidak ditemukan")

    st.caption('"Programming code is just like electrical current, it always finds the path of least resistance."')
