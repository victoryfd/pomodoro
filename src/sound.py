import winsound

def notification_sound():
    winsound.PlaySound("alert.wav", winsound.SND_FILENAME)