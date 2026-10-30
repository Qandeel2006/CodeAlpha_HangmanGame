<h1 align="center">🎮 Hangman Game</h1>

<p align="center">
  <b>A simple text-based word guessing game written in Python.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/CodeAlpha-Task%201-6C47FF" alt="CodeAlpha">
  <img src="https://img.shields.io/badge/Level-Beginner-orange" alt="Level">
</p>

---

## 💡 About

This is **Task 1** of my [CodeAlpha](https://www.codealpha.tech) Python Programming Internship.
The computer picks a secret word and you try to guess it one letter at a time. Make **6 wrong guesses** and the game is over!

## ✨ Features

- 🎲 Picks a **random word** from a list of 5 words
- 🔤 Shows `_` for letters you have not guessed yet
- ❤️ You get **6 wrong guesses**, and the game tells you how many are left
- 🚫 Ignores repeated guesses and invalid input

## 🕹️ How to Play

1. Run the game
2. Type **one letter** and press Enter
3. Guess every letter before you run out of wrong guesses to win

## 🖥️ Example

```text
Welcome to Hangman!
You can make 6 wrong guesses.

Word: _ _ _ _ _ _
Guess a letter: p
Correct!

Word: p _ _ _ _ _
Guess a letter: z
Wrong! You have 5 guesses left.
```

## ⚙️ Getting Started

**Requirements:** Python 3 (nothing else to install)

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_HangmanGame.git
cd CodeAlpha_HangmanGame
python hangman.py
```

> On some computers the command is `python3` instead of `python`.

## 🧠 Concepts Used

| Concept | Where it is used |
|---------|------------------|
| `random` | Choosing the secret word |
| `while` loop | Keeping the game running |
| `if-else` | Checking each guess |
| Strings | Building the word display |
| Lists | Storing words and guessed letters |

## 📁 Project Structure

```text
CodeAlpha_HangmanGame/
├── hangman.py
└── README.md
```

---

## 👤 Author

**Your Name**
Python Programming Intern at [CodeAlpha](https://www.codealpha.tech)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/YOUR_PROFILE)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?logo=github&logoColor=white)](https://github.com/YOUR_USERNAME)

<p align="center">
  ⭐ If you liked this project, give it a star! ⭐<br>
  Made with ❤️ during the <b>CodeAlpha</b> internship
</p>
