import random

class AccelerometerSensor:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def simulate_reading(self):  # 센서 값 시뮬레이션 메서드
        self.x = random.uniform(-10.0, 10.0)
        self.y = random.uniform(-10.0, 10.0)
        if random.random() < 0.4:  # 확률
            self.z = random.choice([-9.8, 9.8]) + random.uniform(-0.5, 0.5)
        else:
            self.z = random.uniform(-10.0, 10.0)  # 그 외 연속값 시뮬레이션
        print(f"[AccelerometerSensor] x={self.x:.2f}, y={self.y:.2f}, z={self.z:.2f}")

    def get_reading(self):
        return self.x, self.y, self.z
