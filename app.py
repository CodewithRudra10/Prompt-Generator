import streamlit as st
import os
from openai import OpenAI

# 🔹 Setup OpenAI (from Streamlit Secrets)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔹 Title
st.title("NexaAI 🚀")
st.subheader("Turn your ideas into perfect AI prompts")

# 🔹 Goal selection
goal = st.selectbox(
    "What do you want to do?",
    ["Explain", "Summarize", "Create Notes for", "Solve"]
)

# 🔹 Inputs
subject = st.text_input("Enter Subject")
topic = st.text_input("Enter Topic")
style = st.text_input("Enter Style (Simple, Detailed, etc.)")

# 🔹 AI toggle
use_ai = st.checkbox("Enhance with AI")

# 🔹 Smart improvement
def improve_topic(topic):
    if len(topic.split()) < 2:
        return f"basic concepts of {topic}"
    return topic

# 🔹 LLM function
def enhance_prompt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Improve this prompt for students. Make it clear, detailed, and effective."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {e}"

# 🔹 Generate button
if st.button("Generate Prompt"):

    if not subject or not topic:
        st.warning("Please fill all fields!")
    else:
        improved_topic = improve_topic(topic)

        # 🔹 Base prompt
        if goal == "Explain":
            result = f"Explain {subject} topic '{improved_topic}' in a {style.lower()} way with examples."

        elif goal == "Solve":
            result = f"Solve {subject} problem '{improved_topic}' step-by-step."

        elif goal == "Summarize":
            result = f"Summarize {subject} topic '{improved_topic}' into key points."

        elif goal == "Create Notes for":
            result = f"Create structured notes for {subject} topic '{improved_topic}'."

        # 🔹 Show base result
        st.success("✅ Generated Prompt")
        st.write(result)

        # 🔹 AI Enhancement
        if use_ai:
            enhanced = enhance_prompt(result)

            st.success("🚀 Enhanced Prompt")
            st.write(enhanced)
            st.code(enhanced)
        else:
            st.code(result)
