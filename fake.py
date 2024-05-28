import os
from gtts import gTTS
msg = " Sure, 1. Orientation: slightly turn to your right. Move Forward: Travel about 1 to 2 steps straight forward until you sense that you are near a softer object. You should feel a bean bag chair in front of you after those steps. 4. Locate the Table: The glass of water is on a small table that should be to your right once you find the bean bag. You may extend your right hand slightly outward and to the right side of the bean bag. 5. Feel for the Glass: Slide your hand along the surface of the table until you reach the glass of water. Your glass of water will be on the table right next to the bean bag chair."
tts = gTTS(text=msg, lang='en', slow=False)

tts.save("./output.mp3")

os.system("mpv ./output.mp3 --no-video")

