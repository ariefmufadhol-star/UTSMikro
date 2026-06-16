import streamlit as st
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Electronics Web Project - UTS", page_icon="⚡", layout="centered")

# --- NAVIGASI TAB ---
tab1, tab2 = st.tabs(["⌁ HOME", "⌁ PROFILE"])

# ==================== 1. TAB HOME ====================
with tab1:
    st.title("Welcome to the Core Node")
    st.subheader("STUDENT ID: 2420307004")
    
    st.info("""
    This digital platform is fully driven by the **Streamlit Framework**, synthesized perfectly to fulfill the Web Programming Midterm Exam requirements.
    
    Think of this framework as the **Microcontroller** of this website, routing commands and managing signals efficiently.
    
    Execute the tab panel navigation above to switch the logic states of this application.
    """)

# ==================== 2. TAB PROFILE ====================
with tab2:
    st.header("ARIEF MUFADHOL")
    st.caption("STUDENT ID: 2420307004 • G24' ELECTRONICS")
    
    col_left, col_right = st.columns([1.2, 2])
    
    # --- KOLOM KIRI (CONTACT & ABILITY) ---
    with col_left:
        st.subheader("📌 CONTACT")
        st.write("""
        📞 +62 8958 0033 0007  
        ✉ ariefmufadhol@gmail.com  
        📸 @arief_mfdhl  
        📍 Jl. Telaga Sari No.7  
        👶 Padang, 15/10/2005  
        ⚡ Active Student  
        📁 Streamlit Web Project v1.0
        """)
        
        st.subheader("🛠️ ABILITY")
        st.write("""
        - Embedded System Programming
        - Arduino
        - Wiring Diagram
        - Electronics Instrumentation
        - Layout Design Eagle Autodesk
        - Troubleshooting
        - Team Work
        """)
        
        st.subheader("💼 EXPERIENCE")
        st.markdown("**Magang di PT. Panasonic Manufacturing Indonesia**")
        st.caption("2022 | Refrigerator Injection Moulding Operator")

    # --- KOLOM KANAN (ABOUT ME, EDUCATION, ACHIEVEMENT) ---
    with col_right:
        st.subheader("ℹ️ ABOUT ME")
        st.write("Experienced individuals specializing in research and technology. Experienced in robotics and excelling in developing innovations.")
        
        st.subheader("🎓 EDUCATION")
        st.markdown("**Politeknik Caltex Riau** \n*2024 - Now | Electronics Engineering*")
        st.markdown("**Semen Padang Senior High School** \n*2021 - 2024 | Electronics Engineering*")
        st.markdown("**11 Junior High School** \n*2018 - 2021*")
        st.markdown("**Semen Padang Elementary School** \n*2012 - 2018*")
        
        st.subheader("🏆 ACHIEVEMENT")
        st.markdown("- **National Student Competition (2023)**: Medallion For Excellence")
        st.markdown("- **Provincial Student Competency Competition (2023)**: 1st Place")
        st.markdown("- **City Level Student Competency Competition (2023)**: 1st Place")
        st.markdown("- **Sumatra Level Robotic Line Follower Competition (2025)**: 2nd Place")
        st.markdown("- **National Level Robotic Line Follower Competition (2025)**: Best Spirit And Best Design")

    st.divider()

    # --- SECTION BRAND (PORTFOLIO ROBOT) ---
    st.subheader("🤖 BRAND - Competition Line Follower Robot")
    st.write("""
    This is an exclusive high-performance PCB hardware routing architecture designed for high-speed tracking optimization. 
    Featuring an aerodynamic **Aerodynamic Sensor Array Board** and an integrated 
    **IPS 240x240 Display Mainboard** for high-efficiency logic data streaming and hardware engineering layout customization.
    """)
    
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
