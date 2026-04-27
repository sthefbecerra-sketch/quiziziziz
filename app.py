import streamlit as st
import random

st.set_page_config(page_title="Trivia PRO", page_icon="🎮", layout="centered")

# 🎨 ESTILO
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: white;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 20px;
}

.card {
    background: rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 25px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}

button[kind="secondary"] {
    width: 100%;
    margin-top: 10px;
    border-radius: 12px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎮 Trivia PRO 💖</div>", unsafe_allow_html=True)

# 🔊 sonidos ONLINE
def play_sound(url):
    st.markdown(f"""
    <audio autoplay>
    <source src="{url}" type="audio/mp3">
    </audio>
    """, unsafe_allow_html=True)

# URLs de sonidos (gratis)
CLICK = "https://www.soundjay.com/buttons/sounds/button-16.mp3"
WIN = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"
FAIL = "https://www.soundjay.com/button/sounds/beep-10.mp3"

# 🧠 preguntas
preguntas = [
    {"q": "💍 ¿Cuál es mi aniversario?", "o": ["4 de julio","15 de marzo","22 de agosto","1 de enero"], "r": "4 de julio"},
    {"q": "🎂 ¿Cuál es mi cumpleaños?", "o": ["7 de octubre","12 de mayo","30 de diciembre","9 de abril"], "r": "7 de octubre"},
    {"q": "📅 ¿En qué año nos conocimos?", "o": ["2022","2020","2021","2023"], "r": "2022"},
    {"q": "🎨 ¿Color favorito?", "o": ["Negro","Rojo","Azul","Verde"], "r": "Negro"},
    {"q": "🎧 ¿Qué me gusta más?", "o": ["Viajar","Dormir","Comer","Escuchar música"], "r": "Escuchar música"}
]

# 🎮 estado
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.preguntas = random.sample(preguntas, len(preguntas))

# 🏁 si terminó
if st.session_state.index >= len(preguntas):

    st.progress(1.0)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(f"🏆 Puntaje: {st.session_state.score}/5")

    if st.session_state.score == 5:
        play_sound(WIN)
        st.balloons()
        st.snow()
        st.success("🔥 PERFECTO 💖")
    elif st.session_state.score >= 3:
        st.info("👍 Bien jugado")
    else:
        play_sound(FAIL)
        st.warning("💀 Puedes mejorar")

    if st.button("🔄 Volver a jugar"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.preguntas = random.sample(preguntas, len(preguntas))
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

else:
    # 📊 progreso
    st.progress(st.session_state.index / len(preguntas))

    p = st.session_state.preguntas[st.session_state.index]

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(p["q"])

    opciones = p["o"].copy()
    random.shuffle(opciones)

    for op in opciones:
        if st.button(op):
            play_sound(CLICK)

            if op == p["r"]:
                st.session_state.score += 1
                st.success("✅ Correcto!")
            else:
                play_sound(FAIL)
                st.error("❌ Incorrecto")

            st.session_state.index += 1
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
