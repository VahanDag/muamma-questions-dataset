import matplotlib.pyplot as plt
import numpy as np


def twing_algorithm(data, threshold=3, k=2):
    n = len(data)
    s = np.zeros(n)  # İkişer adımlı toplam sinyali
    cusum = np.zeros(n)  # Kumulatif toplam sinyali
    alarm = np.zeros(n)  # Alarm sinyali

    for i in range(2, n):
        s[i] = data[i] - data[i - 2]
        cusum[i] = cusum[i - 1] + s[i]
        
        # Alarm durumu kontrolü
        if np.abs(cusum[i]) > threshold * np.std(s[:i]):
            alarm[i] = 1
            # Cusum sıfırlama
            cusum[i] = 0
    
    return alarm

# Örnek zaman serisi oluştur
np.random.seed(42)
time_series = np.random.normal(loc=0, scale=1, size=100)

# TWING algoritması uygula
alarms = twing_algorithm(time_series, threshold=3, k=2)

# Zaman serisi ve alarm sinyalini görselleştir
plt.figure(figsize=(10, 6))
plt.plot(time_series, label='Zaman Serisi')
plt.plot(alarms, label='Alarm Sinyali', linestyle='--', marker='o')
plt.title('TWING Algorithm')
plt.xlabel('Zaman')
plt.ylabel('Değer')
plt.legend()
plt.show()