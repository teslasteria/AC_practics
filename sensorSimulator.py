import csv
import random
import time
from datetime import datetime

class SensorSimulator:
    def __init__(self, metric_name, unit, min_value, max_value):
        self.metric_name = metric_name
        self.unit = unit
        self.min_value = min_value
        self.max_value = max_value
        self.values = []

    def generate_value(self):
        return random.uniform(self.min_value, self.max_value)

    def record_value(self):
        while True:
            # Генерация значения каждую секунду
            value = self.generate_value()
            self.values.append(value)

            # Усреднение значений за минуту
            if len(self.values) >= 60:
                avg_value = sum(self.values) / len(self.values)
                self.save_to_csv(avg_value)
                self.values = []  # Сброс значений для следующей минуты

            time.sleep(1)

    def save_to_csv(self, avg_value):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = [timestamp, self.metric_name, avg_value, self.unit]

        with open('sensor_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

        print(f"Recorded: {timestamp}, {self.metric_name}, {avg_value:.2f} {self.unit}")

if __name__ == "__main__":
    # Параметры датчика
    metric_name = "Температура"
    unit = "°C"
    min_value = 20.0
    max_value = 30.0

    # Инициализация симулятора
    sensor = SensorSimulator(metric_name, unit, min_value, max_value)

    # Запуск записи данных
    sensor.record_value()