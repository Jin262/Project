from accelerometer_sensor import AccelerometerSensor
from orientation_detector import OrientationDetector
from sound_controller import SoundController

def main():
    sensor = AccelerometerSensor()
    detector = OrientationDetector(sensor)
    controller = SoundController()

    print("[System] Running orientation check...")
    sensor.simulate_reading()

    if detector.is_face_down():  # 뒤집힘 판단
        controller.set_silent_mode()  # 무음 모드 설정
    elif detector.is_face_up():  # 정상(윗방향) 판단
        controller.restore_sound_mode()  # 소리 모드 복원
    else:
        print("[System] Device is tilted; no mode change.")

    print(f"[System] Current mode: {controller.get_mode()}")
    print("[System] Program finished.")

if __name__ == "__main__":
    main()
