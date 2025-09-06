import tkinter as tk
from tkinter import messagebox
import google.generativeai as genai
import json

# 🔑 Configure Gemini
genai.configure(api_key="YOUR API KEY")

asked_questions = []
current_qdata = None  # latest question (English or translated)
score = {"correct": 0, "wrong": 0}


def generate_unique_question(topic, difficulty):
    """Generate unique quiz question using Gemini"""
    model = genai.GenerativeModel("gemini-1.5-flash")

    for _ in range(5):
        response = model.generate_content(
            f"""
            Create one unique multiple-choice question about "{topic}".
            Difficulty: {difficulty}.
            Do not repeat common textbook questions.
            Return ONLY JSON in this format:
            {{
              "question": "....",
              "options": ["opt1","opt2","opt3","opt4"],
              "answer": "correct_option_text"
            }}
            """,
            generation_config=genai.types.GenerationConfig(temperature=0.9)
        )

        text = response.text.strip()
        if text.startswith("```"):
            text = text.strip("`")
            if text.lower().startswith("json"):
                text = text[4:]
            text = text.strip()

        try:
            qdata = json.loads(text)
        except:
            continue

        if qdata["question"] not in asked_questions:
            asked_questions.append(qdata["question"])
            return qdata

    return None


def check_answer(choice_text, correct_text, buttons):
    """Check if selected answer is correct"""
    global score
    for btn in buttons:
        btn.config(state="disabled")
    if choice_text == correct_text:
        for btn in buttons:
            if btn["text"] == choice_text:
                btn.config(bg="green")
        score["correct"] += 1
    else:
        for btn in buttons:
            if btn["text"] == choice_text:
                btn.config(bg="red")
            if btn["text"] == correct_text:
                btn.config(bg="green")
        score["wrong"] += 1

    update_score()


def start_quiz():
    """Generate and display new quiz question"""
    global current_qdata
    topic = entry.get()
    difficulty = selected_difficulty.get()

    if not topic:
        messagebox.showwarning("Warning", "Enter a topic first")
        return

    try:
        qdata = generate_unique_question(topic, difficulty)
        if not qdata:
            messagebox.showerror("Error", "Could not generate a unique question.")
            return
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    current_qdata = qdata
    display_question(qdata)


def display_question(qdata):
    """Show question + options on screen"""
    question_label.config(text=qdata["question"])
    for i, opt in enumerate(qdata["options"]):
        buttons[i].config(
            text=opt,
            state="normal",
            bg="SystemButtonFace",
            command=lambda c=opt: check_answer(c, qdata["answer"], buttons)
        )


def translate_question_and_options(qdata, lang):
    """Translate quiz into selected language (includes correct answer)"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        f"""
        Translate the following quiz into {lang}.
        Keep the same correct answer but translate it too.
        Return ONLY JSON in this format:
        {{
          "question": "translated_question",
          "options": ["opt1","opt2","opt3","opt4"],
          "answer": "translated_correct_option"
        }}

        Quiz:
        Question: {qdata["question"]}
        Options: {qdata["options"]}
        Correct Answer: {qdata["answer"]}
        """
    )

    text = response.text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
        text = text.strip()

    try:
        return json.loads(text)
    except:
        return None


def translate_quiz():
    """Translate current question + options + answer"""
    global current_qdata
    if not current_qdata:
        messagebox.showwarning("Warning", "Generate a question first")
        return

    lang = selected_lang.get()
    tqdata = translate_question_and_options(current_qdata, lang)

    if tqdata:
        current_qdata = tqdata  # replace with translated version
        display_question(tqdata)
    else:
        messagebox.showerror("Error", f"Could not translate to {lang}")


def update_score():
    """Update score label"""
    score_label.config(
        text=f"✅ Correct: {score['correct']}   ❌ Wrong: {score['wrong']}"
    )


# ---------------- Tkinter GUI ----------------
root = tk.Tk()
root.title("AI Quiz App - Gemini Powered")
root.geometry("650x580")

tk.Label(root, text="Enter Topic:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Difficulty dropdown
difficulties = ["Easy", "Medium", "Hard"]
selected_difficulty = tk.StringVar(value="Medium")

tk.Label(root, text="Select Difficulty:", font=("Arial", 12)).pack(pady=5)
diff_menu = tk.OptionMenu(root, selected_difficulty, *difficulties)
diff_menu.pack(pady=5)

tk.Button(root, text="Generate Question", font=("Arial", 12), command=start_quiz).pack(pady=10)

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=600, justify="center")
question_label.pack(pady=20)

buttons = []
for i in range(4):
    b = tk.Button(
        root,
        text="",
        font=("Arial", 12),
        wraplength=500,   
        justify="center",
        anchor="center", 
        relief="raised",
        padx=10, pady=5
    )
    b.pack(pady=5, fill="x", padx=20)  # Stretch buttons horizontally
    buttons.append(b)


# Next Question button
tk.Button(root, text="Next Question", font=("Arial", 12), command=start_quiz).pack(pady=10)

# Score Label
score_label = tk.Label(root, text="✅ Correct: 0   ❌ Wrong: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Language selection
languages = ["Hindi", "Marathi", "Tamil", "Telugu", "Gujarati", "Bengali"]
selected_lang = tk.StringVar(value="Hindi")

tk.Label(root, text="Select Language:", font=("Arial", 12)).pack(pady=5)
lang_menu = tk.OptionMenu(root, selected_lang, *languages)
lang_menu.pack(pady=5)

tk.Button(root, text="Translate Question", font=("Arial", 12), command=translate_quiz).pack(pady=10)

root.mainloop()
