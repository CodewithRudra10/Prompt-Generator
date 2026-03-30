import streamlit as st

# 🔹 Title
st.title("NexaAI 🚀")
st.subheader("Helps Students Generate better AI prompts for Studies")

# 🔹 Goal selection
goal = st.selectbox(
    "What do you want to do?",
    ["Explain", "Summarize", "Create Notes", "Solve"]
)

# 🔹 Inputs
subject = st.text_input("Enter Subject (e.g. Science, Maths)")
topic = st.text_input("Enter Topic (e.g. Light, Algebra)")
style = st.text_input("Enter Style (Simple, Detailed, Step-by-step)")

# 🔹 Improve topic clarity
def improve_topic(topic):
    if len(topic.split()) < 2:
        return f"basic concepts of {topic}"
    return topic

# 🔹 Generate button
if st.button("Generate Prompt"):

    if not subject or not topic:
        st.warning("⚠️ Please fill all fields!")
    else:
        improved_topic = improve_topic(topic)

        # 🔹 Prompt logic
        if goal == "Explain":
            result = f"Explain {subject} topic '{improved_topic}' in a {style.lower()} way with examples."

        elif goal == "Solve":
            result = f"Solve {subject} problem '{improved_topic}' step-by-step."

        elif goal == "Summarize":
            result = f"Summarize {subject} topic '{improved_topic}' into key points."

        elif goal == "Create Notes":
            result = f"Create structured notes for {subject} topic '{improved_topic}'."

        # 🔹 Output
        st.success("✅ Generated Prompt")
        st.write(result)
        st.code(result)
