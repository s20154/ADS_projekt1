# Porownywanie czasu wykonania quicksort vs justload

by uruchomic w bashu wpisujemy
```
time python3 justLoad.py; time python3 quickSort.py; time python3 heapSort.py;
```

po uruchomienu dostajemy
```
python3 justLoad.py  0.06s user 0.01s system 85% cpu 0.084 total
python3 quickSort.py  0.99s user 0.01s system 99% cpu 0.999 total
python3 heapSort.py  1.27s user 0.01s system 99% cpu 1.282 total
```

| Program       | Czas          |
| ------------- |:-------------:|
| justLoad.py   | 0.06s         |
| quickSort.py  | 0.99s         |
| heapSort.py   | 1.27s         |