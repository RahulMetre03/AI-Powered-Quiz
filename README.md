````markdown
# 🎓 AI-Powered Quiz App  

An AI-driven interactive quiz application built with Python (Tkinter) and Google Gemini API.  
Users can enter a topic → get unique multiple-choice questions → answer interactively with instant feedback → track scores → switch languages → adjust difficulty levels.  

---

## ✨ Features  
- 🔹 AI Question Generation – Uses Google Gemini LLM to create unique, topic-based MCQs.  
- 🔹 Multiple Difficulty Levels – Easy / Medium / Hard modes supported.  
- 🔹 Instant Feedback – Correct answers turn green, wrong answers turn red.  
- 🔹 Score Tracking – Keeps track of correct/incorrect answers.  
- 🔹 Regional Language Support – Translate questions & options into Hindi, Marathi, Tamil, Telugu, Gujarati, Bengali.  
- 🔹 Switch Back to English – Instantly revert to original English without re-calling the API.  
- 🔹 Responsive GUI – Built in Tkinter, auto-wraps long text for readability.  

---

## 🖼️ Screenshots  
Will be added soon


---

## 🚀 Tech Stack  
- Language: Python  
- GUI Framework: Tkinter  
- AI Model: Google Gemini (via `google-generativeai`)  
- Other: JSON handling, dynamic GUI updates  

---

## 📦 Installation & Setup  

### 1️⃣ Clone the repo  
```bash
git clone https://github.com/your-username/ai-quiz-app.git
cd ai-quiz-app
````

### 2️⃣ Install dependencies

```bash
pip install google-generativeai
```

### 3️⃣ Add your Gemini API key

In the code, replace:

```python
genai.configure(api_key="YOUR_API_KEY")
```

with your actual API key.

### 4️⃣ Run the app

```bash
python quiz_app.py
```

---

## 🎯 Usage

1. Enter a topic (e.g., Chemistry, World History, Python).
2. Choose difficulty (Easy/Medium/Hard).
3. Click Generate Question.
4. Select an option → get instant feedback (✅ correct, ❌ incorrect).
5. Track your score as you play.
6. Switch to a regional language or back to English anytime.

---

## 🔮 Future Enhancements

* Leaderboard & multi-user support.
* Option to export quiz results to PDF/CSV.
* Integration with text-to-speech for accessibility.
* Mobile-friendly version (Kivy or Flutter).

---

## 👨‍💻 Author

Rahul Metre

* 🎓 B.Tech CSE @ MIT WPU
* 🌐 [LinkedIn](https://linkedin.com/in/rahulmetre) | [GitHub](https://github.com/rahulmetre)

---

⚡ If you like this project, star ⭐ the repo and share it!

```
```
