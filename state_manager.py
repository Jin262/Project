import json  
from pathlib import Path  

STATE_FILE = Path("state.json") 

def save_mode(mode: str):  # 현재 모드를 저장하는 함수 정의
    with STATE_FILE.open("w") as f:
        json.dump({"mode": mode}, f)

def load_mode(default: str = "sound_on") -> str:  # 저장된 모드를 로드하는 함수 정의
    if STATE_FILE.exists():
        data = json.loads(STATE_FILE.read_text())
        return data.get("mode", default)
    return default