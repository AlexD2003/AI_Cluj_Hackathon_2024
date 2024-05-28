from gtts import gTTS
from pydub import AudioSegment
import io

# Text to be converted to speech
text = "Hello, how are you?"

# Create gTTS object
tts = gTTS(text)

# Save the speech as a temporary file-like object
speech_file = io.BytesIO()
tts.write_to_fp(speech_file)
speech_file.seek(0)

# Load speech from file-like object
speech = AudioSegment.from_file(speech_file)

# Adjust the volume (change the dB level as needed)
speech_with_adjusted_volume = speech + 10  # Increase volume by 10dB

# Export the adjusted speech to a file (or do whatever you want with it)
speech_with_adjusted_volume.export("output.mp3", format="mp3")
