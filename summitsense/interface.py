# interface.py

import tkinter as tk

class Interface:

  def __init__(self):

    # Fenster erstellen
    self.window = tk.Tk()
    
    # Widgets definieren
    self.transcript_text = tk.Text(self.window)
    self.current_speaker = tk.Label(self.window)

  def setup_ui(self):

    # Widgets anordnen
    self.transcript_text.grid(row=0, column=0)
    self.current_speaker.grid(row=1, column=0)

    # Fenstergröße etc. festlegen

  def display_transcript(self, text):

    # Transkript in Textfeld anzeigen  
    self.transcript_text.delete(1.0, "end")
    self.transcript_text.insert(1.0, text)

  def highlight_speaker(self, name):

    # Aktiven Sprecher im Label setzen
    self.current_speaker["text"] = name

  def run(self):

    # Schleife für Updates starten
    self.window.mainloop()