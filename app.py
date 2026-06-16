from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# --- ROUTE STANDARD AMAN UNTUK BACA GAMBAR ---
@app.route('/gambar/<filename>')
def ambil_gambar(filename):
    return send_from_directory(os.getcwd(), filename)

# --- STYLE CSS KREATIF TEMA ELEKTRONIKA MODERN ---
HTML_LAYOUT_ATAS = '''
<!DOCTYPE html>
<html>
<head>
    <title>Electronics Web Project - UTS</title>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            margin: 40px; 
            background-color: #0b0f19; 
            color: #e2e8f0; 
        }
        .container { 
            max-width: 900px; 
            margin: auto; 
            background: #111827; 
            padding: 40px; 
            border-radius: 15px; 
            border: 2px solid #00ffcc;
            box-shadow: 0 0 20px rgba(0, 255, 204, 0.2); 
        }
        nav { 
            text-align: center;
            margin-bottom: 30px; 
        }
        nav a { 
            margin: 0 10px; 
            text-decoration: none; 
            font-weight: bold; 
            color: #4b5563; 
            font-size: 18px;
            letter-spacing: 1px;
            padding: 8px 16px;
            border-radius: 8px;
            transition: 0.3s;
        }
        nav a:hover { 
            color: #38bdf8; 
        }
        nav a.active {
            color: #00ffcc;
            background-color: #1f2937;
            border: 1px solid #00ffcc;
            box-shadow: 0 0 12px rgba(0, 255, 204, 0.6);
            text-shadow: 0 0 5px rgba(0, 255, 204, 0.8);
        }
        h1, h2, h3 { 
            color: #38bdf8; 
            text-shadow: 0 0 8px rgba(56, 189, 248, 0.5);
        }
        h1 { text-align: center; font-size: 32px; margin-bottom: 5px; }
        .subtitle { text-align: center; color: #00ffcc; font-weight: bold; margin-bottom: 25px; letter-spacing: 1px; }
        
        p { font-size: 15px; line-height: 1.6; color: #9ca3af; }
        .highlight { color: #00ffcc; font-weight: bold; }
        
        /* Layout Pembagian Kolom Profile */
        .profile-layout {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .column-left {
            width: 35%;
            vertical-align: top;
            padding-right: 30px;
            border-right: 1px dashed #374151;
        }
        .column-right {
            width: 65%;
            vertical-align: top;
            padding-left: 30px;
        }
        
        /* Styling Sub-Section di Profile */
        .section-title {
            background: #1f2937;
            color: #00ffcc;
            padding: 6px 12px;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            letter-spacing: 1px;
            margin-top: 25px;
            margin-bottom: 15px;
            border-left: 4px solid #38bdf8;
            text-transform: uppercase;
        }
        
        ul { margin: 0; padding-left: 20px; color: #9ca3af; }
        li { margin-bottom: 8px; font-size: 14px; }
        
        .item-title { color: #e2e8f0; font-weight: bold; font-size: 15px; }
        .item-sub { color: #38bdf8; font-size: 13px; margin-bottom: 10px; }

        /* Style untuk Grid Gambar */
        .image-grid {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin-top: 25px;
        }
        .pcb-box {
            width: 48%;
            text-align: center;
        }
        .pcb-image {
            width: 100%;
            height: auto;
            border-radius: 10px;
            border: 2px solid #374151;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
            transition: 0.3s;
        }
        .pcb-image:hover {
            border-color: #00ffcc;
            box-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
        }
        .img-caption {
            font-size: 14px;
            color: #9ca3af;
            margin-top: 8px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
'''

HTML_LAYOUT_BAWAH = '''
    </div>
</body>
</html>
'''

# --- 1. HOME PAGE ---
@app.route('/')
def home():
    nav_home = '''
        <nav>
            <a href="/" class="active">⌁ HOME</a>
            <a href="/profile">⌁ PROFILE</a>
        </nav>
        <hr style="border: 0; height: 1px; background: #374151; margin-bottom: 30px;">
    '''
    konten_home = '''
        <h1>Welcome</h1>
        <div style="margin-top: 25px;"></div>
        <p>This digital platform is fully driven by the <span class="highlight">Flask Framework</span>, synthesized perfectly to fulfill the Web Programming Midterm Exam requirements.</p>
        <p>Think of this framework as the <span class="highlight">Microcontroller</span> of this website, routing commands and managing signals efficiently.</p>
        <p>Execute the links on the control panel navigation above to switch the logic states of this application.</p>
    '''
    return HTML_LAYOUT_ATAS + nav_home + konten_home + HTML_LAYOUT_BAWAH

# --- 2. PROFILE PAGE ---
@app.route('/profile')
def profile():
    nav_profile = '''
        <nav>
            <a href="/">⌁ HOME</a>
            <a href="/profile" class="active">⌁ PROFILE</a>
        </nav>
        <hr style="border: 0; height: 1px; background: #374151; margin-bottom: 30px;">
    '''
    konten_profile = '''
        <h1>ARIEF MUFADHOL</h1>
        <p style="text-align: center;" class="subtitle">STUDENT ID: 2420307004 &bull; G24' ELECTRONICS</p>
        
        <table class="profile-layout">
            <tr>
                <td class="column-left">
                    <div class="section-title">Contact</div>
                    <p style="font-size: 14px; margin-bottom: 8px;">📞 +62 8958 0033 0007</p>
                    <p style="font-size: 14px; margin-bottom: 8px;">✉ ariefmufadhol@gmail.com</p>
                    <p style="font-size: 14px; margin-bottom: 8px;">📸 @arief_mfdhl</p>
                    <p style="font-size: 14px; margin-bottom: 8px;">📍 Jl. Telaga Sari No.7</p>
                    <p style="font-size: 14px; margin-bottom: 8px;">👶 Padang, 15/10/2005</p>
                    <p style="font-size: 14px; margin-bottom: 8px;">⚡ Active Student</p>
                    <p style="font-size: 14px; margin-bottom: 8px;">📁 Python Flask Web Project v1.0</p>

                    <div class="section-title">Ability</div>
                    <ul>
                        <li>Embedded System Programming</li>
                        <li>Arduino</li>
                        <li>Wiring Diagram</li>
                        <li>Electronics Instrumentation</li>
                        <li>Layout Design Eagle Autodesk</li>
                        <li>Troubleshooting</li>
                        <li>Team Work</li>
                    </ul>
                </td>
                
                <td class="column-right">
                    <div class="section-title">About Me</div>
                    <p style="margin-top: 0;">
                        Experienced individuals specializing in research and technology. Experienced in robotics and excelling in developing innovations.
                    </p>
                    
                    <div class="section-title">Education</div>
                    <div>
                        <div class="item-title">Politeknik Caltex Riau</div>
                        <div class="item-sub">2024 - Now | Electronics Engineering</div>
                        
                        <div class="item-title">Semen Padang Senior High School</div>
                        <div class="item-sub">2021 - 2024 | Electronics Engineering</div>
                        
                        <div class="item-title">11 Junior High School</div>
                        <div class="item-sub">2018 - 2021</div>
                        
                        <div class="item-title">Semen Padang Elementary School</div>
                        <div class="item-sub">2012 - 2018</div>
                    </div>
                    
                    <div class="section-title">Experience</div>
                    <div>
                        <div class="item-title">Magang di PT. Panasonic Manufacturing Indonesia</div>
                        <div class="item-sub">2022 | Refrigerator Injection Moulding Operator</div>
                    </div>
                    
                    <div class="section-title">Achievement</div>
                    <div>
                        <div class="item-title">National Student Competition</div>
                        <div class="item-sub">2023 | Medallion For Excellence</div>
                        
                        <div class="item-title">Provincial Student Competency Competition</div>
                        <div class="item-sub">2023 | 1st Place</div>
                        
                        <div class="item-title">City Level Student Competency Competition</div>
                        <div class="item-sub">2023 | 1st Place</div>
                        
                        <div class="item-title">Sumatra Level Robotic Line Follower Competition</div>
                        <div class="item-sub">2025 | 2nd Place</div>
                        
                        <div class="item-title">National Level Robotic Line Follower Competition</div>
                        <div class="item-sub">2025 | Best Spirit And Best Design</div>
                    </div>
                </td>
            </tr>
        </table>
        
        <div class="section-title" style="text-align: center;">Brand</div>
        <h3 style="text-align: center; margin-top: 10px; font-size: 20px; letter-spacing: 0.5px;">Competition Line Follower Robot</h3>
        <p style="text-align: center; max-width: 800px; margin: auto; margin-bottom: 25px;">
            This is an exclusive high-performance PCB hardware routing architecture designed for high-speed tracking optimization. Featuring an aerodynamic <span class="highlight">Aerodynamic Sensor Array Board</span> and an integrated <span class="highlight">IPS 240x240 Display Mainboard</span> for high-efficiency logic data streaming and hardware engineering layout customization.
        </p>

        <div class="image-grid">
            <div class="pcb-box">
                <img src="/gambar/sensor.jpeg" alt="Sensor Array PCB" class="pcb-image">
                <div class="img-caption">Sensor Array PCB</div>
            </div>
            <div class="pcb-box">
                <img src="/gambar/mainboard.jpeg" alt="Mainboard PCB" class="pcb-image">
                <div class="img-caption">Mainboard PCB</div>
            </div>
        </div>

        <p style="font-size: 13px; font-style: italic; color: #6b7280; margin-top: 40px; text-align: center;">
            "Programming code is just like electrical current, it always finds the path of least resistance."
        </p>
    '''
    return HTML_LAYOUT_ATAS + nav_profile + konten_profile + HTML_LAYOUT_BAWAH

if __name__ == '__main__':
    app.run(debug=True)