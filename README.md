# Rule-Based Chatbot (Python)

A simple command-line chatbot built with Python. It greets the user based on the time of day and answers basic questions using keyword matching.

## Features
- Time-based greeting (morning, afternoon, evening, night)
- Keyword-based replies from a dictionary
- Type `bye` to exit

## How to run
1. Install Python 3
2. Download `chatbot.py`
3. Run: `python chatbot.py`

## Limitations
- Uses simple keyword matching, so it can misread sentences (for example, "I am not happy" matches "happy")
- Replies come from a fixed dictionary, so it cannot understand new questions
- It is not an AI model

## Next steps
- Build an LLM-based version of this chatbot
