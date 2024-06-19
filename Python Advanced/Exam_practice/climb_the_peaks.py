from collections import deque

conquered_peaks = []

peaks_values = deque([80, 90, 100, 60, 70])
peaks_names = deque(['Vihren', 'Kutelo', 'Banski Suhodol', 'Polezhan', 'Kamenitza'])

food_portions = [int(x) for x in input().split(', ')]
stamina = deque(int(x) for x in input().split(', '))

while food_portions and stamina and peaks_values:
    result = food_portions[-1] + stamina[0]

    if result >= peaks_values[0]:
        peaks_values.popleft()
        name = peaks_names.popleft()
        conquered_peaks.append(name)

    food_portions.pop()
    stamina.popleft()

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks: ")
    for peak in conquered_peaks:
        print(peak)