from state_manager import save_mode, load_mode

class SoundController:  # 사운드 모드 제어 클래스
    def __init__(self):
        self.mode = load_mode()
        print(f"[SoundController] Loaded previous mode: {self.mode}")

    def set_silent_mode(self):  # 무음 모드 설정 메서드
        if self.mode != "silent":
            self.mode = "silent"
            save_mode(self.mode)
            print("[SoundController] Switched to SILENT mode.")

    def restore_sound_mode(self):  # 소리 모드 복원 메서드
        if self.mode != "sound_on":
            self.mode = "sound_on"
            save_mode(self.mode)
            print("[SoundController] Restored to SOUND mode.")

    def get_mode(self):
        return self.mode