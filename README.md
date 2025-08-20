# Simple NLP-based Rule-Based Chatbot

## Overview
This project is a **rule-based chatbot** built in Python that uses **basic NLP techniques**  
to preprocess user input and match it against predefined intents.  

The chatbot uses simple **if-elif-else** structures, but with preprocessing and grouping of synonyms to make it more natural.

---

## Objective
- Understand the **basic structure of NLP** (text preprocessing, intent detection).
- Learn how to simulate chatbot conversations using **rule-based logic**.
- Explore how input/output loops and conditionals can simulate intelligent behavior.

---

## Tools
- Python 3.x
- Built-in libraries: `datetime`, `random`, `string`

---

## How It Works
1. User input is **preprocessed** (lowercased, punctuation removed).
2. The chatbot checks input against **intent groups**:
   - Greetings (hi, hello, hey, etc.)
   - Farewell (bye, exit, etc.)
   - Asking about the bot
   - Asking current time/date
   - "How are you?" type questions
3. If input matches, a **random response** from the intent group is returned.
4. If no intent is matched, a default fallback response is used.

---
