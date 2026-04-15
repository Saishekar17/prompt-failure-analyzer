import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="LLM Debugger", layout="wide")

# Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.write("Local LLM: Ollama (llama3)")
st.sidebar.write("Mode: Prompt Debugger")

# Title
st.title("🧠 Prompt Failure Analyzer (Local AI)")

st.markdown("Analyze → Improve → Score → Learn")

# Input
col1, col2 = st.columns(2)

with col1:
    prompt = st.text_area("📝 Prompt", height=150)

with col2:
    output = st.text_area("❌ Bad Output", height=150)

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Button
if st.button("🚀 Analyze & Improve"):

    if not prompt or not output:
        st.warning("Please fill both fields")
    else:
        with st.spinner("Running AI pipeline..."):
            res = requests.post(API, json={
                "prompt": prompt,
                "output": output
            })

        if res.status_code == 200:
            data = res.json()

            st.success("✅ Completed")

            # Results Layout
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🔍 Failure Analysis")
                st.write(data["failure"])

                st.subheader("🛠 Improved Prompt")
                st.code(data["improved_prompt"])

            with col2:
                st.subheader("🤖 New Output")
                st.write(data["new_output"])

                st.subheader("📊 Scores")
                st.metric("Old", data["scores"]["old_score"])
                st.metric("New", data["scores"]["new_score"])
                st.metric("Improvement %", f"{data['scores']['improvement_%']}%")

            # Save history
            st.session_state.history.append({
                "prompt": prompt[:30],
                "improvement": data["scores"]["improvement_%"]
            })

        else:
            st.error("❌ API error")

# 📈 Chart
if st.session_state.history:
    st.subheader("📈 Improvement Trend")

    df = pd.DataFrame(st.session_state.history)
    st.line_chart(df["improvement"])

# 📜 Sidebar history
st.sidebar.subheader("🕘 Recent Runs")

for item in st.session_state.history[-5:]:
    st.sidebar.write(f"{item['prompt']} → {item['improvement']}%")