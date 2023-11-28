# transcription.py

from azure.cognitiveservices.speech import AudioConfig, SpeechConfig
from azure.cognitiveservices.speech.audio import AudioInputStream

class Transcription:

  def __init__(self):
    
    # Speech SDK Konfiguration
    self.speech_config = SpeechConfig(subscription="YOUR_KEY", region="..")

  def audio_stream(self):
    
    # Audio-Stream öffnen
    audio_input = AudioInputStream(filename_or_stream)  
    
    return audio_input

  def transcribe(self, audio_input):

    # Transkription starten
    speech_recognizer = self.speech_config.speech_recognizer()
    
    result = speech_recognizer.recognize_once_async(audio_input).get()
    
    # Transkript zurückgeben 
    return result.text

  def recognize_speaker(self, result):
    
    # Ist noch nicht implementiert, da hier Speziallogik nötig ist
    # Zurückgeben welcher Teilnehmer spricht
    return speaker