# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based AI Agent project focused on OpenAI integration. The codebase is organized into chapters for learning/tutorial purposes.

## Environment Setup

- Python virtual environment is located at `./myenv/`
- OpenAI API key is configured in `.env` file (OPENAI_API_KEY)
- To activate the virtual environment: `source myenv/bin/activate`
- Dependencies can be installed with: `pip install openai`

## Project Structure

- `chapter3/` - Contains OpenAI chat completion implementations
  - `chat_completions.py` - Basic OpenAI GPT-4o-mini chat completion example
- `myenv/` - Python virtual environment (do not modify)
- `.env` - Environment variables including OpenAI API key

## Running Code

To run the chat completion example:
```bash
source myenv/bin/activate
cd chapter3
python chat_completions.py
```

## Development Notes

- This appears to be a learning/tutorial project structured by chapters
- Each chapter likely contains different AI/ML concepts or implementations
- The project uses OpenAI's Python client library for API interactions
- Environment variables are used for API key management