import streamlit as st
import random

st.set_page_config(page_title="Trivia Villanas Disney", page_icon="🦹‍♀️")

# Banco de preguntas
preguntas = [
    {
        "pregunta": "¿Cómo se llama la villana de La Sirenita?",
        "opciones": ["Úrsula", "Maléfica", "Cruella", "Jafar"],
        "respuesta": "Úrsula"
    },
    {
        "pregunta": "¿Qué villana odia a los dálmatas?",
        "opciones": ["Cruella de Vil", "Reina Grimhilde", "Yzma", "Madre Gothel"],
        "respuesta": "Cruella de Vil"
    },
    {
        "pregunta": "¿Quién es la villana de Blancanieves?",
        "opciones": ["Reina Grimhilde", "Maléfica", "Lady Tremaine", "Úrsula"],
        "respuesta": "Reina Grimhilde"
    },
    {
        "pregunta": "¿Qué villana tiene cuernos y se convierte en dragón?",
        "opciones": ["Maléfica", "Yzma", "Cruella", "Gothel"],
        "respuesta": "Maléfica"
    },
    {
        "pregunta": "¿Qué villana secuestra a Rapunzel?",
        "opciones": ["Madre Gothel", "Yzma", "Cruella", "Úrsula"],
        "respuesta": "Madre Gothel"
    }
]

# Estado
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntaje = 0
    st.session_state.preguntas_mezcladas = random.sample(preguntas, len(preguntas))
    st.session_state.opciones_mezcladas = []

st.title("🦹‍♀️ Trivia: Villanas de Disney")

# Función para mezclar opciones

def obtener_opciones():
    pregunta_actual = st.session_state.preguntas_mezcladas[st.session_state.indice]
    opciones = pregunta_actual["opciones"][:]
    random.shuffle(opciones)
    return opciones

# Mostrar pregunta
if st.session_state.indice < len(preguntas):
    pregunta_actual = st.session_state.preguntas_mezcladas[st.session_state.indice]
    st.subheader(f"Pregunta {st.session_state.indice + 1} de {len(preguntas)}")
    st.write(pregunta_actual["pregunta"])

    opciones = obtener_opciones()
    respuesta_usuario = st.radio("Elige una opción:", opciones, key=st.session_state.indice)

    if st.button("Responder"):
        if respuesta_usuario == pregunta_actual["respuesta"]:
            st.success("¡Correcto!")
            st.session_state.puntaje += 1
        else:
            st.error(f"Incorrecto. La respuesta correcta es {pregunta_actual['respuesta']}")

        st.session_state.indice += 1
        st.rerun()

# Resultado final
else:
    st.subheader("Resultado final")
    st.write(f"Obtuviste {st.session_state.puntaje} de {len(preguntas)} correctas")

    if st.session_state.puntaje == len(preguntas):
        st.balloons()
        st.success("¡Perfecto! ¡Eres un experto en villanas de Disney! 🎉")
    else:
        st.info("Intenta nuevamente para obtener puntaje perfecto")

    if st.button("Reiniciar"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
