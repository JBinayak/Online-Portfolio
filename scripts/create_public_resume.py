"""Recreate a public resume from the supplied resume, omitting private contact data.
Requires reportlab. No source PDF is copied into the website.
"""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'downloads/Binayak_Gurubacharya_Resume.pdf'
styles = {
 'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=20, leading=24, alignment=TA_CENTER, textColor=HexColor('#202024'), spaceAfter=7),
 'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=8.3, leading=12, alignment=TA_CENTER, spaceAfter=6),
 'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=HexColor('#a8004e'), spaceBefore=10, spaceAfter=4),
 'role': ParagraphStyle('role', fontName='Helvetica-Bold', fontSize=9.4, leading=12.5, spaceBefore=6, spaceAfter=2),
 'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=12.3, spaceAfter=3),
 'small': ParagraphStyle('small', fontName='Helvetica', fontSize=8.3, leading=11, textColor=HexColor('#55525a'), spaceAfter=3)
}
story=[]
def p(text, style='body'): story.append(Paragraph(text, styles[style]))
def section(title):
 p(title,'section')
 story.append(HRFlowable(width='100%',thickness=.5,color=HexColor('#d6d0d4'),spaceAfter=3))
def role(title,org,date,body):
 p(title+' | '+org,'role');p(date,'small');p(body)
def project(title,tech,body,url=None):
 label=title + (f' <link href="{url}" color="#a8004e">[Code]</link>' if url else '')
 p(label+' | '+tech,'role');p(body)
p('BINAYAK GURUBACHARYA','name')
p('<link href="mailto:bgurubacharya23@augustana.edu">bgurubacharya23@augustana.edu</link> | <link href="https://www.linkedin.com/in/binayakgurubacharya">linkedin.com/in/binayakgurubacharya</link> | <link href="https://github.com/JBinayak">github.com/JBinayak</link>','contact')
section('EDUCATION')
p('Augustana College | Rock Island, Illinois | Expected May 2027','role')
p('Bachelor degree in Computer Science and Data Science | GPA: 3.2')
p('<b>Coursework:</b> Algorithms &amp; Computational Theory, Data Structures, Software Development, Web Programming, Data Engineering, Probability &amp; Statistics')
section('EXPERIENCE')
role('Game Developer Intern','Neoteric Nepal','June - August 2024 | Kathmandu, Nepal','Developed 2D and 3D games in Unity with C#. Created reusable character templates, state machines, and environment interaction modules across four gameplay levels. Collaborated on 3D assets, textures, renders, and models in Blender.')
role('Webpage Developer Intern','ConvergeTree','December 2022 - February 2023 | Kathmandu, Nepal','Designed responsive webpages for 5+ client projects. Contributed front-end and client-driven improvements within a full-cycle software development team and redesigned layouts to improve the user experience.')
role('English and Computer Science Tutor','Saathi Nepal','June - September 2022 | Kathmandu, Nepal','Taught English reading, writing, and speaking to 20+ secondary students weekly. Created a computer science curriculum and QBASIC course for 30+ high-school students.')
role('Front-End Developer Intern','PasaPay','March - June 2018 and March - April 2020 | Remote','Improved webpages and implemented front-end features for apps serving 200+ users, with attention to page performance and consistent functionality across platforms.')
section('PROJECTS')
project('Educational HAM Radio Simulator','Java, JavaFX, Gemini API','Contributed to a team-built simulator. Built server-side chatroom messaging (real-time send/receive and room broadcast) and integrated a Gemini chatbot that participates in chatrooms.','https://github.com/AugustanaCSC305Fall24/GallinuleRepo')
project('3D Shooter Game','Unity, C#','Built a single-player 3D shooter with reusable state machines, health tracking, raycast shooting, and ability systems. Public repository contains scripts.','https://github.com/JBinayak/First-Person-Shooter-3D')
project('2D RPG Game','Unity, C#','Created a level-based RPG with sprite animations, modular inventory systems, and scalable combat mechanics. Public repository contains scripts.','https://github.com/JBinayak/Chess-Game-2D')
project('Memory Game Webpage','JavaScript, HTML, CSS, Node.js, Express, MongoDB','Built a browser-based card-matching game with shuffled layouts and move counting. Includes an Express API and MongoDB model for recording player move counts.','https://github.com/JBinayak/Memory_Game')
project('Online Portfolio','HTML, CSS, JavaScript','Designed a responsive personal portfolio to showcase projects, internships, and career progression.','https://github.com/JBinayak/Online-Portfolio')
section('TECHNICAL SKILLS')
p('Python, Java, C#, PHP, CSS, JavaScript, TypeScript, JavaFX, Flutter, Node.js, MongoDB, Express.js, SQL, Unity, Firebase')
out.parent.mkdir(exist_ok=True)
SimpleDocTemplate(str(out),pagesize=(612,792),rightMargin=38,leftMargin=38,topMargin=30,bottomMargin=28,title='Binayak Gurubacharya - Public Resume',author='Binayak Gurubacharya').build(story)
print(out)
