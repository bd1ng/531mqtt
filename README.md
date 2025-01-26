# 531mqtt
MQTT Demo. Publisher randomly generates a set of temperature and humidity conditions. Based on these conditions, the subscriber queries Gemini 1.5 Flash for the ideal animal that lives in these conditions

# Install
pip install -r requirements.txt

/* Ensure that you put your API key in a .env file. With the format of KEY=your-api-key-here-no-quotes.

# Run Publisher
python pub.py

# Run Subscriber
python sub.py