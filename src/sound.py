from pathlib import Path
import sys
import os


root = Path(__file__).parent.parent 
sound_file = root / "assets" / "alert.wav"

def notification_sound():
    if sys.platform == "win32":
        _play_windows()
    else:
        _play_linux()
    

def _play_windows():
    import winsound
    winsound.PlaySound(str(sound_file), winsound.SND_FILENAME)

def _play_linux():
    os.system(f"paplay {sound_file}")

# def _play_macOS():