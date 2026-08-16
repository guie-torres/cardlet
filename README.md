# 📚 Cardlet

**Cardlet** is an AI-powered flashcard application built with Python and Streamlit. It allows users to create, organise, and practice flashcards, while using AI to generate complete decks from a topic.

The purpose of this project was for me to learn Python and experiment with using the OpenAI API.

> **Note:** Cardlet currently runs locally and requires an OpenAI API key for AI features.

## Preview

Coming soon.

## Features

- Manage cards
- Manage decks
- Practice
- Create decks using AI
- Export decks to Quizlet
  
## Technologies
- **Python**
- **Streamlit**
- **OpenAI API**
- **Pydantic**
- **JSON**
- **CSS**
- **python-dotenv**

## Project Structure

```text
Cardlet/
│
├── models/
│   ├── card.py
│   └── deck.py
│
├── storage/
│   ├── storage.py
│   ├── cards.json
│   └── decks.json
├── utils/
│   ├── ui.py
│   └── session.py
│
├── pages/
│   ├── 1_Manage.py
│   ├── 2_Practice.py
│   └── 3_AI_Deck_Maker.py
│
├── styles/
│   ├── general.css
│   ├── AI_maker.css
│   ├── main_style.css
│   └── practice_style.css
│
├── logic.py
├── ai.py
├── Main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Running Cardlet

Cardlet currently runs locally using Streamlit.

### Clone the repository

```bash
git clone https://github.com/guie-torres/cardlet/
cd Cardlet
```
**Using a virtual environment is recommended:**

```bash
python -m venv .venv
```

**Activate it on Windows:**

```bash
.venv\Scripts\activate
```

**Then install the dependencies:**

```bash
pip install -r requirements.txt
```

### Set up the OpenAI API key

Cardlet's AI functionality requires an OpenAI API key.

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

### Start Cardlet

Run:

```bash
streamlit run Main.py
```

Streamlit will open Cardlet in your browser.


## AI Architecture

Cardlet uses the OpenAI API to generate structured flashcard decks.

Instead of relying on unstructured text responses, AI output is parsed into Pydantic models:

```python
class AICard(BaseModel):
    front: str
    back: str


class AIDeck(BaseModel):
    name: str
    cards: list[AICard]
    error: bool = False
    error_message: str = ""
```

This allows Cardlet to validate the structure of AI-generated content before adding it to the application.

AI errors are handled separately from normal application data so that failed generations do not create invalid decks or cards.

---

## Quizlet Export

Cardlet can convert your AI generated or manually created decks into a suitable Quizlet format, allowing for simple cross-platform deck transfers.

Cardlet generates a copyable/downloadable text file which can be copied into Quizlet as follows:

1) Open Quizlet
2) Press the blue "+" button
3) Press the "flashcard set" button
4) Press the "+ Import" button
5) Between term and definition: **Tab**
6) Between cards: **New line**
7) Open Cardlet
8) Select your deck
9) Click export
10) Copy the generated text into Quizlet
11) Press the "Import" button

> **Note:** Quizlet's interface may change over time, so the exact steps may differ in future versions.

The OpenAI API key is provided through an environment variable rather than being stored directly in the source code.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

This file together with the key are not included in the repository. Hence one has to create it on their own if they wish to use the AI features.

> **Never commit your `.env` file or API key to GitHub.**
## What I Learned

Cardlet was my first project made in Python, so the main purpose of the project was to become comfortable with Python and its ecosystem.

Additionally, this was my first time working with the OpenAI API. Through Cardlet, I learned how to integrate an external API, work with structured AI responses using Pydantic, handle API errors, and connect AI-generated data with an existing application.

## Future Improvements

Possible future improvements include:
- Spaced repetition
- More advanced practice modes
- Keyboard shortcuts
- Database storage
- Additional export formats
- Improved mobile support
- More advanced AI generation controls

## License
This project was created as a personal programming and portfolio project.
