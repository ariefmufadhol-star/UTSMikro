import streamlit as st
from PIL import Image
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Electronics Web Project - UTS", page_icon="⚡", layout="centered")

# --- STYLE CSS UNTUK TEMA ELEKTRONIKA MODERN (DARK MODE) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
    }
    .highlight {
        color: #00ffcc;
        font-weight: bold;
    }
    .section-title {
        background-color: #1f2937;
        color: #00ffcc;
        padding: 6px 12px;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 20px;
        margin-bottom: 15px;
        border-left: 4px solid #38bdf8;
    }
    .item-title { color: #e2e8f0; font-weight: bold; font-size: 15px; margin-top: 10px; }
    .item-sub { color: #38bdf8; font-size: 13px; margin-bottom: 10px; }
    </style>
""", unsafe_allowed_html=True)

# --- NAVIGASI NAV/TAB TEMA ELEKTRO ---
tabs = st.tabs(["⌁ HOME", "⌁ PROFILE"])

# ==================== 1. TAB HOME ====================
with tabs[0]:
    st.markdown("<h1 style='text-align: center; color: #38bdf8;'>Welcome to the Core Node</h1>", unsafe_allowed_html=True)
    st.markdown("<p style='text-align: center; color: #00ffcc; font-weight: bold;'>STUDENT ID: 2420307004</p>", unsafe_allowed_html=True)
    st.write("")
    
    st.markdown("""
    This digital platform is fully driven by the <span class='highlight'>Streamlit Framework</span>, synthesized perfectly to fulfill the Web Programming Midterm Exam requirements.
    
    Think of this framework as the <span class='highlight'>Microcontroller</span> of this website, routing commands and managing signals efficiently.
    
    Execute the tab panel navigation above to switch the logic states of this application.
    """, unsafe_allowed_html=True)

# ==================== 2. TAB PROFILE ====================
with tabs[1]:
    st.markdown("<h1 style='text-align: center; color: #38bdf8;'>ARIEF MUFADHOL</h1>", unsafe_allowed_html=True)
    st.markdown("<p style='text-align: center; color: #00ffcc; font-weight: bold; letter-spacing: 1px;'>STUDENT ID: 2420307004 • G24' ELECTRONICS</p>", unsafe_allowed_html=True)
    
    col_left, col_right = st.columns([1.2, 2])
    
    # --- KOLOM KIRI (CONTACT & ABILITY) ---
    with col_left:
        st.markdown("<div class='section-title'>CONTACT</div>", unsafe_allowed_html=True)
        st.markdown("""
        📞 +62 8958 0033 0007  
        ✉ ariefmufadhol@gmail.com  
        📸 @arief_mfdhl  
        📍 Jl. Telaga Sari No.7  
        👶 Padang, 15/10/2005  
        ⚡ Active Student  
        📁 Streamlit Web Project v1.0
        """)
        
        st.markdown("<div class='section-title'>ABILITY</div>", unsafe_allowed_html=True)
        st.markdown("""
        - Embedded System Programming
        - Arduino
        - Wiring Diagram
        - Electronics Instrumentation
        - Layout Design Eagle Autodesk
        - Troubleshooting
        - Team Work
        """)
        
        st.markdown("<div class='section-title'>EXPERIENCE</div>", unsafe_allowed_html=True)
        st.markdown("<div class='item-title'>Magang di PT. Panasonic Manufacturing Indonesia</div>", unsafe_allowed_html=True)
        st.markdown("<div class='item-sub'>2022 | Refrigerator Injection Moulding Operator</div>", unsafe_allowed_html=True)

    # --- KOLOM KANAN (ABOUT ME, EDUCATION, ACHIEVEMENT) ---
    with col_right:
        st.markdown("<div class='section-title'>ABOUT ME</div>", unsafe_allowed_html=True)
        st.write("Experienced individuals specializing in research and technology. Experienced in robotics and excelling in developing innovations.")
        
        st.markdown("<div class='section-title'>EDUCATION</div>", unsafe_allowed_html=True)
        st.markdown("""
        <div class='item-title'>Politeknik Caltex Riau</div><div class='item-sub'>2024 - Now | Electronics Engineering</div>
        <div class='item-title'>Semen Padang Senior High School</div><div class='item-sub'>2021 - 2024 | Electronics Engineering</div>
        <div class='item-title'>11 Junior High School</div><div class='item-sub'>2018 - 2021</div>
        <div class='item-title'>Semen Padang Elementary School</div><div class='item-sub'>2012 - 2018</div>
        """, unsafe_allowed_html=True)
        
        st.markdown("<div class='section-title'>ACHIEVEMENT</div>", unsafe_allowed_html=True)
        st.markdown("""
        <div class='item-title'>National Student Competition</div><div class='item-sub'>2023 | Medallion For Excellence</div>
        <div class='item-title'>Provincial Student Competency Competition</div><div class='item-sub'>2023 | 1st Place</div>
        <div class='item-title'>City Level Student Competency Competition</div><div class='item-sub'>2023 | 1st Place</div>
        <div class='item-title'>Sumatra Level Robotic Line Follower Competition</div><div class='item-sub'>2025 | 2nd Place</div>
        <div class='item-title'>National Level Robotic Line Follower Competition</div><div class='item-sub'>2025 | Best Spirit And Best Design</div>
        """, unsafe_allowed_html=True)

    # --- SECTION BRAND (PORTFOLIO ROBOT) ---
    st.markdown("<div class='section-title' style='text-align: center;'>BRAND</div>", unsafe_allowed_html=True)
    st.markdown("<h3 style='text-align: center; color: #38bdf8;'>Competition Line Follower Robot</h3>", unsafe_allowed_html=True)
    st.markdown("""
    <p style='text-align: center; color: #9ca3af;'>
    This is an exclusive high-performance PCB hardware routing architecture designed for high-speed tracking optimization. 
    Featuring an aerodynamic <span class='highlight'>Aerodynamic Sensor Array Board</span> and an integrated 
    <span class='highlight'>IPS 240x240 Display Mainboard</span> for high-efficiency logic data streaming and hardware engineering layout customization.
    </p>
    """, unsafe_allowed_html=True)
    
    # Grid Gambar Portofolio PCB Elektronik Lu
    col_img1, col_img2 = st.columns(2)
    
    with col_img1:
        if os.path.exists("sensor.jpeg"):
            st.image("sensor.jpeg", caption="Sensor Array PCB", use_container_width=True)
        else:
            st.warning("File sensor.jpeg tidak ditemukan")
            
    with col_img2:
        if os.path.exists("mainboard.jpeg"):
            st.image("mainboard.jpeg", caption="Mainboard PCB", use_container_width=True)
        else:
            st.warning("File mainboard.jpeg tidak ditemukan")

    st.markdown("""
    <p style='font-size: 13px; font-style: italic; color: #6b7280; margin-top: 40px; text-align: center;'>
    "Programming code is just like electrical current, it always finds the path of least resistance."
    </p>
    """, unsafe_allowed_html=True)
