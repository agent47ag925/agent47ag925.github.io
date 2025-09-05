# app.py
# Streamlit 포트폴리오 기본 뼈대 코드 작성함

import streamlit as st
from datetime import datetime

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="Portfolio | Your Name",
    page_icon="📁",
    layout="wide"
)

# 간단한 스타일 커스터마이즈 적용함
st.markdown("""
<style>
/* 본문 최대 폭 제한 해제 */
.block-container {max-width: 1200px;}
/* 카드 스타일 */
.card {
  padding: 1rem; border-radius: 14px; border: 1px solid #E5E7EB;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04);
  background: white;
}
.badge {
  display: inline-block; padding: 2px 8px; border-radius: 999px;
  background: #EEF2FF; color: #3730A3; font-size: 12px; margin-right: 6px;
}
.small-muted {color:#6B7280; font-size: 13px;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 데이터 예시 정의
# -----------------------------
PROFILE = {
    "name": "Your Name",
    "title": "AI Engineer · Educator",
    "summary": "실무 중심의 AI/ML 및 컴퓨터 비전 프로젝트 수행과 교육을 병행함. 연구와 제품화를 잇는 브릿지를 지향함.",
    "location": "Seoul, Korea",
    "email": "you@example.com",
    "links": {
        "GitHub": "https://github.com/yourname",
        "LinkedIn": "https://www.linkedin.com/in/yourname/",
        "Homepage": "https://yourname.dev",
    }
}

SKILLS = {
    "Languages": ["Python", "JavaScript/TypeScript", "SQL"],
    "AI/ML": ["PyTorch", "OpenCV", "Hugging Face", "LangChain"],
    "Web": ["FastAPI", "Streamlit", "React (기초)"],
    "Cloud/DevOps": ["Docker", "GCP", "GitHub Actions"]
}

PROJECTS = [
    {
        "title": "Haveit: Skin Analysis Microservices",
        "period": "2024",
        "desc": "YOLO 기반 피부 분석 파이프라인 및 FastAPI/Spring Boot 마이크로서비스 구성함.",
        "tags": ["Computer Vision", "FastAPI", "Docker"],
        "link": "https://github.com/yourname/haveit",
    },
    {
        "title": "Silver Lining: YouTube Summarizer",
        "period": "2024",
        "desc": "영상 자막/오디오를 활용한 요약 및 키워드 추출, 검색 연동 RAG 파이프라인 구현함.",
        "tags": ["RAG", "LangChain", "Whisper"],
        "link": "https://github.com/yourname/silver-lining",
    },
    {
        "title": "Handwriting Emotion (EMOTHAW)",
        "period": "2025",
        "desc": "필적 기반 감정 추정 벡터라이제이션 기법 연구 및 실험 파이프라인 구축함.",
        "tags": ["Research", "Time-series", "OpenCV"],
        "link": "https://github.com/yourname/emothaw",
    },
]

PUBLICATIONS = [
    {
        "title": "A Flow-based Vectorization Approach for Emotion Recognition from Handwriting",
        "venue": "CSA 2025 (under review)",
        "link": "https://arxiv.org/abs/xxxx.xxxxx",
        "authors": "Your Name, Coauthor A, Coauthor B",
        "year": 2025
    }
]

TEACHING = [
    {"title": "Deep Learning Foundations", "org": "Univ. / Corp.", "year": "2024–2025", "hours": 32},
    {"title": "OpenCV for AI Engineers", "org": "Corp. Training", "year": "2024", "hours": 16},
]

# -----------------------------
# 유틸 함수
# -----------------------------
def draw_header():
    left, right = st.columns([3,1])
    with left:
        st.title(PROFILE["name"])
        st.write(PROFILE["title"])
        st.write(PROFILE["summary"])
        st.caption(f"{PROFILE['location']} · {PROFILE['email']}")
    with right:
        st.download_button(
            "Resume (PDF) 다운로드",
            data=b"",  # 실제 PDF 바이트로 교체하려 함
            file_name="resume.pdf",
            mime="application/pdf",
            help="이력서를 첨부한 경우에만 동작함"
        )

    # 링크 배지 렌더링함
    link_html = " ".join(
        [f'<a class="badge" href="{url}" target="_blank">{name}</a>'
         for name, url in PROFILE["links"].items()]
    )
    st.markdown(link_html, unsafe_allow_html=True)
    st.markdown("---")

def show_about():
    st.subheader("About")
    st.write("""
- 연구와 서비스화를 동시에 고려하여 문제를 정의하고 해결책을 설계하려 함  
- 컴퓨터 비전, RAG/에이전트, 교육 콘텐츠 제작 경험을 융합하여 현실 적용 사례를 만드는 데 강점 보유함
""")

def show_skills():
    st.subheader("Skills")
    cols = st.columns(2)
    with cols[0]:
        for k in ["Languages", "AI/ML"]:
            st.markdown(f"**{k}**")
            st.write(", ".join(SKILLS[k]))
    with cols[1]:
        for k in ["Web", "Cloud/DevOps"]:
            st.markdown(f"**{k}**")
            st.write(", ".join(SKILLS[k]))

def project_card(p):
    st.markdown(f"""
<div class="card">
  <h4 style="margin:0">{p['title']} <span class="small-muted">· {p['period']}</span></h4>
  <p style="margin:6px 0">{p['desc']}</p>
  <p>{" ".join([f"<span class='badge'>{t}</span>" for t in p['tags']])}</p>
  <a href="{p['link']}" target="_blank">Repository / Link</a>
</div>
""", unsafe_allow_html=True)

def show_projects():
    st.subheader("Projects")
    cols = st.columns(3)
    for i, p in enumerate(PROJECTS):
        with cols[i % 3]:
            project_card(p)

def show_publications():
    st.subheader("Publications")
    for pub in PUBLICATIONS:
        st.markdown(f"**{pub['title']}**  \n*{pub['venue']}*, {pub['year']}  \n{pub['authors']}  \n[Link]({pub['link']})")

def show_teaching():
    st.subheader("Teaching")
    for c in TEACHING:
        st.write(f"- {c['title']} · {c['org']} · {c['year']} · {c['hours']}h")

def show_contact():
    st.subheader("Contact")
    st.write("협업, 강의, 연구 제안 관련 문의 환영함")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message", height=160)
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("메시지를 접수함. 실제 전송 로직은 백엔드 연동 필요함")

# -----------------------------
# 앱 레이아웃
# -----------------------------
with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Go to",
        ["Home", "Projects", "Skills", "Publications", "Teaching", "Contact"],
        label_visibility="collapsed"
    )
    st.caption(f"Last updated: {datetime.now().date()}")

draw_header()

if page == "Home":
    show_about()
    st.markdown("---")
    show_projects()
elif page == "Projects":
    show_projects()
elif page == "Skills":
    show_skills()
elif page == "Publications":
    show_publications()
elif page == "Teaching":
    show_teaching()
elif page == "Contact":
    show_contact()
