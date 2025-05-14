import math

class OrientationDetector:  # 방향 판단 클래스
    FACE_THRESHOLD = 0.9

    def __init__(self, sensor):  # 클래스 초기화 메서드
        self.sensor = sensor 

    def is_face_down(self):  # 뒤집힘 판단 메서드
        x, y, z = self.sensor.get_reading()
        magnitude = math.sqrt(x*x + y*y + z*z)
        ratio = z / magnitude if magnitude else 0
        print(f"[OrientationDetector] magnitude={magnitude:.2f}, ratio={ratio:.2f}")
        return ratio < -self.FACE_THRESHOLD

    def is_face_up(self):  # 정상(윗방향) 판단 메서드
        x, y, z = self.sensor.get_reading()
        magnitude = math.sqrt(x*x + y*y + z*z)
        ratio = z / magnitude if magnitude else 0
        return ratio > self.FACE_THRESHOLD
