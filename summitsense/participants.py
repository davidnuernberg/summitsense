# participants.py

import msgraph

class Participants:

  def __init__(self):

    # MS Graph Client 
    self.client = MsGraphClient()

    # Liste zur Teilnehmerspeicherung
    self.participants = []  

  def list_participants(self, meeting_id):

    # Teilnehmer vom Graph API holen
    participants = self.client.meeting(meeting_