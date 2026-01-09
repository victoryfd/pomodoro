from pathlib import Path
import winsound

root = Path(__file__).parent.parent 
sound_file = root / "assets" / "alert.wav"

def notification_sound():
    winsound.PlaySound(str(sound_file), winsound.SND_FILENAME)