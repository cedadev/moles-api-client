import json
import datetime
from pathlib import Path

ROLLBACK_FILE = Path(__file__).resolve().parent / 'files' / 'rollback.json'
MAX_SESSIONS = 20

class Rollback:
    current_session = ''
    sessions = None
    
    @classmethod
    def load_sessions(cls):
        with open(ROLLBACK_FILE) as f:
            cls.sessions = json.loads(f)
            
    
    @classmethod
    def create_new_session(cls, session_id):
        if len(cls.sessions) == 20:
            cls.sessions.pop()
        
        cls.sessions[session_id] = {}
    