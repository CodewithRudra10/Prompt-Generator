import streamlit as st
import os
from openai import OpenAI

# 🔹 Setup OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔹 Title
st.title("NexaAI 🚀")
st.subheader("Turn your ideas into perfect AI prompts & study content")

# 🔹 Mode selection
mode = st.selectbox(
    "Choose Mode",
    ["Generate Prompt", "Generate Content"]
)

# 🔹 Common Functions
def improve_topic(topic):
    if len(topic.split()) < 2:
        return f"basic concepts of {topic}"
    return topic

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
    except Exception:
        return "⚠️ Error enhancing prompt"

def generate_content(topic, student_class, content_type):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful teacher creating educational content. Keep it simple, clear, and suitable for students."
                },
                {
                    "role": "user",
                    "content": f"Create {content_type} for Class {student_class} on topic '{topic}'."
                }
            ]
        )
        return response.choices[0].message.content
    except Exception:
        return "⚠️ Error generating content"

# =========================
# 🔹 PROMPT GENERATOR MODE
# =========================
if mode == "Generate Prompt":

    goal = st.selectbox(
        "What do you want to do?",
        ["Explain", "Summarize", "Create Notes for", "Solve"]
    )

    subject = st.text_input("Enter Subject")
    topic = st.text_input("Enter Topic")
    style = st.text_input("Enter Style (Simple, Detailed, etc.)")

    use_ai = st.checkbox("Enhance with AI")

    if st.button("Generate Prompt"):

        if not subject or not topic:
            st.warning("Please fill all fields!")
        else:
            improved_topic = improve_topic(topic)

            if goal == "Explain":
                result = f"Explain {subject} topic '{improved_topic}' in a {style.lower()} way with examples."

            elif goal == "Solve":
                result = f"Solve {subject} problem '{improved_topic}' step-by-step."

            elif goal == "Summarize":
                result = f"Summarize {subject} topic '{improved_topic}' into key points."

            elif goal == "Create Notes for":
                result = f"Create structured notes for {subject} topic '{improved_topic}'."

            st.success("✅ Generated Prompt")

            if use_ai:
                enhanced = enhance_prompt(result)
                st.write(enhanced)
                st.code(enhanced)
            else:
                st.write(result)
                st.code(result)

# =========================
# 🔹 CONTENT GENERATOR MODE
# =========================
elif mode == "Generate Content":

    st.subheader("📚 Generate Study Content")

    topic = st.text_input("Enter Topic")
    student_class = st.selectbox("Select Class", [str(i) for i in range(1, 13)])

    content_type = st.selectbox(
        "Content Type",
        ["Explanation", "Notes", "Questions & Answers", "Summary"]
    )

    if st.button("Generate Content"):

        if topic:
            result = generate_content(topic, student_class, content_type)

            st.success("✅ Generated Content")
            st.write(result)
            st.code(result)
        else:
            st.warning("Please enter a topic")
