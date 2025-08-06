# Grok Chatbot

A simple Python chatbot that uses the Grok API (x.ai) to provide conversational AI capabilities.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Grok API key:
   - Option 1: Edit the `.env` file and replace the API key
   - Option 2: Set as environment variable: `export GROK_API_KEY=your-key-here`

3. Run the chatbot:
```bash
python apibot.py
```

## Usage

- Type your message and press Enter
- Type 'exit' to quit the chatbot
- The bot will respond using Grok's AI capabilities

## API Configuration

- **Model**: grok-beta
- **Max Tokens**: 1000
- **Temperature**: 0.7

## Troubleshooting

- Ensure you have a valid Grok API key
- Check your internet connection
- Verify the API key has sufficient credits
