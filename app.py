import streamlit as st
import random
import base64

st.set_page_config(page_title="Trivia PRO", page_icon="🎮", layout="centered")

# 🎨 ESTILO ULTRA PRO
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
    animation: fadeIn 1s ease-in-out;
}

.card {
    background: rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 25px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
    animation: fadeInUp 0.5s ease;
}

.option-btn {
    display: block;
    width: 100%;
    padding: 15px;
    margin-top: 10px;
    border-radius: 15px;
    border: none;
    font-size: 16px;
    font-weight: bold;
    background: linear-gradient(90deg, #ff758c, #ff7eb3);
    color: white;
    cursor: pointer;
    transition: 0.3s;
}

.option-btn:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #43cea2, #185a9d);
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

@keyframes fadeInUp {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎮 Trivia PRO 💖</div>", unsafe_allow_html=True)

# 🔊 sonido
def play_sound(file):
    with open(file, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}">
        </audio>
        """, unsafe_allow_html=True)

# 🧠 preguntas
preguntas = [
    {"q": "💍 ¿Cuál es nuestro aniversario?", "o": ["4 de julio","15 de marzo","22 de agosto","1 de enero"], "r": "4 de julio"},
    {"q": "🎂 ¿Cuál es mi cumpleaños?", "o": ["17 de octubre","12 de mayo","30 de diciembre","9 de abril"], "r": "17 de octubre"},
    {"q": "📅 ¿En qué año nos conocimos?", "o": ["2022","2020","2021","2023"], "r": "2022"},
    {"q": "🎨 ¿Color favorito?", "o": ["Negro","Rojo","Azul","marron"], "r": "marron"},
    {"q": "🎧 ¿Qué me gusta más?", "o": ["Viajar","Dormir","Comer","Escuchar música"], "r": "Escuchar música"}
]

# 🎮 estado juego
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.preguntas = random.sample(preguntas, len(preguntas))

p = st.session_state.preguntas[st.session_state.index]

# 📊 progreso
st.progress((st.session_state.index) / len(preguntas))

# 🎴 tarjeta pregunta
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader(p["q"])

opciones = p["o"].copy()
random.shuffle(opciones)

# 🎯 botones en lugar de radio
for op in opciones:
    if st.button(op, key=op):
        play_sound("sounds/click.mp3")

        if op == p["r"]:
            st.session_state.score += 1
            st.success("✅ Correcto!")
        else:
            play_sound("sounds/fail.mp3")
            st.error("❌ Incorrecto")

        st.session_state.index += 1
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# 🏁 FINAL
if st.session_state.index >= len(preguntas):
    st.progress(1.0)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(f"🏆 Puntaje: {st.session_state.score}/5")

    if st.session_state.score == 5:
        play_sound("sounds/win.mp3")
        st.balloons()
        st.snow()
        st.success("🔥 PERFECTO, nivel DIOS 💖")
    elif st.session_state.score >= 3:
        st.info("👍 Bien jugado")
    else:
        st.warning("💀 Te falta entrenamiento 😭")

    if st.button("🔄 Volver a jugar"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.preguntas = random.sample(preguntas, len(preguntas))
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
