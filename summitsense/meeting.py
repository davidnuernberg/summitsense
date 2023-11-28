# meeting.py

import msgraph
importmicrosoftteams # Bibliothek für MS Teams API

class Meeting:

  def __init__(self, meeting_id):
    
    # Attribute
    self.meeting_id = meeting_id
    self.client = ms_teams.TeamsClient() # Client für MS Graph API
    
    # Konfiguration
    self.graph_token = os.getenv("GRAPH_TOKEN")

  def start_meeting(self):
    
    # Authentifizieren an MS Graph
    self.client.authentication_provider.set_token(self.graph_token)  
    
    # Starten des Meetings über die API
    meeting = self.client.meetings(self.meeting_id).start()
    
    print("Meeting started")
    
    # Rückgabe des Meeting-Objekts
    return meeting

  def stop_meeting(self):
    
    # Beenden des Meetings
    self.client.meetings(self.meeting_id).end()
    
    print("Meeting ended")