import time
from accelerometer_sensor import AccelerometerSensor
from orientation_detector import OrientationDetector
from sound_controller import SoundController

CHECK_INTERVAL = 1.0 # 센서 읽기 주기 설정 (초)

def main():
    sensor = AccelerometerSensor()
    detector = OrientationDetector(sensor)
    controller = SoundController()
    last_state = controller.get_mode()
    print(f"[Service] Starting background mode, initial state: {last_state}")

    try:
        while True: # 무한 루프 시작
            sensor.simulate_reading()
            is_down = detector.is_face_down()

            if is_down and last_state != "silent":
                controller.set_silent_mode()
                last_state = "silent"
            elif not is_down and last_state != "sound_on":
                controller.restore_sound_mode()
                last_state = "sound_on"

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("[Service] Stopped by user.")

if __name__ == "__main__":
    main()
