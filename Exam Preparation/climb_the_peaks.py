from collections import deque

daily_portions = [int(x) for x in input().split(", ")]
daily_stamina = deque(int(x) for x in input().split(", "))

mountain_peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70,
}

climbed_peaks = {}

while daily_stamina and daily_portions:
    portion = daily_portions.pop()
    stamina = daily_stamina.popleft()
    sum_of_both = portion + stamina
    is_climbed = False
    current_mountain = ""
    for name, difficulty in mountain_peaks.items():
        if sum_of_both >= difficulty:
            climbed_peaks[name] = difficulty
            current_mountain = name
            is_climbed = True
            break
        else:
            break

    if is_climbed:
        del mountain_peaks[current_mountain]

if mountain_peaks:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

if climbed_peaks:
    print("Conquered peaks:")
    for name in climbed_peaks.keys():
        print(name)
