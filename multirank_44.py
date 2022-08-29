import openseespy.opensees as os
import matplotlib.pyplot as plt
import math
import pickle
import os as osys
import numpy as np
import time
from analysis import eq_analysis

pid = os.getPID()
npC = os.getNP()

f_ro = [0.8, 1.0]  # no ref
f_concrete = [0.75, 1.00, 1.51]  # lower bound no ref, upper bound from our study IUSS Bal et al., 2008
f_steel = [0.76, 1.00, 1.24]  # from Bal et al. 2008 IUSS CoV 0.24
f_span = [1.00, 1.38]  # from Bal et al. 2008 IUSS CoV 0.38
# This frame has some small spans, so we did not use here he lower bound
f_ground_height = [1.00, 1.50]  # no ref, but ooking at some Bayrakli buildings
f_upper_height = [0.87, 1.00, 1.13]  # from Bal et al. 2008 IUSS CoV 0.13 for PFN frames

filelist = osys.listdir("GMfile/")
file_len = len(filelist)
combination_set = [(a, b, c, d, e, f, g) for a in f_ro for b in f_concrete for c in f_steel for d in f_span for e in
                   f_ground_height for f in f_upper_height for g in filelist]

remainer = len(combination_set) % npC

equal_parts = (len(combination_set) - remainer) / (npC)

parts_array = [equal_parts] * (npC - 1)
parts_array.append(remainer + equal_parts)
for i in range(len(parts_array)):
    parts_array[i] = parts_array[i] + (i * parts_array[0])

if pid == 0:
    record_no = 0
    print(f"Process started in PID{pid}. :")
    print("-" * 20)
    for i in combination_set[:int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 1:
    record_no = 0
    print(f"Process started in PID{pid}. :")
    print("-" * 20)
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 2:
    record_no = 0
    print(f"Process started in PID{pid}. :")
    print("-" * 20)
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 3:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 4:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 5:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 6:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 7:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 8:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 9:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 10:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 11:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 12:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 13:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 14:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 15:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 16:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 17:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 18:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 19:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 20:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 21:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 22:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 23:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 24:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 25:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 26:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 27:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 28:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 29:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 30:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 31:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 32:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 33:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 34:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 35:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 36:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 37:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 38:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 39:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 40:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 41:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 42:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")

if pid == 43:
    record_no = 0
    print("-" * 20)
    print(f"Process started in PID{pid}. :")
    for i in combination_set[int(parts_array[pid - 1]):int(parts_array[pid])]:
        dt = float(i[-1][:-4].split("+")[-1])
        eq_analysis(i[:-1], i[-1], pid, record_no, dt)
        record_no = record_no + 1
    print("\n")
