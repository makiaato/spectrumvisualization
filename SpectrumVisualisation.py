from scipy.io import wavfile
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def fourierCoefficient(n, v, k):
    sum = 0.0
    for i in range(n):
        sum += v[i] * complex(math.cos(2 * math.pi * k * i / n),-math.sin(2 * math.pi * k * i / n))
    return sum / n

def roundComplex(m, n = 5):
    d = []
    for i in range(len(m)):
        d.append( complex( round(m[i].real,n) , round(m[i].imag,n)))
    return d

def extractRealnumbers(d):
    r = []
    for i in range(len(d)):
        r.append(d[i].real)
    return r

joji = wavfile.read('SpectrumVisualisation/peep.wav')
# print(joji[0]) # Sample-Rate 44,1 kHz
seconds = 44100
# print(joji[1][60*seconds]) Data Chunks; Make to mono?

# Sample too much, then our result is rough. Sample too few, then our result is inaccurate
# To get full spectrum visualisation, sample double the frequency. But only Smaple-Rate of the
# file as maximum
# wav[Smaple Rate, Data Chunks][Data Chunk Index][Channel]
# 16384 samples?
# 8192 samples is waiting long enough
sample = []
for i in range(1024):
    sample.append(joji[1][0 * seconds + i][0]) # Sample one channel for convenience

c = []
for i in range(len(sample)):
    c.append(fourierCoefficient(len(sample), sample, i))

cLen = int(len(c) / 2)
e = []
for i in range(cLen):
    z = 2 * math.sqrt(c[i].real * c[i].real + c[i].imag * c[i].imag)
    e.append(z)
del e[0]

xAxis = []
for i in range(len(e)):
    xAxis.append(math.log10(i + 1))

fig, ax = plt.subplots()
ax.plot(xAxis, e)
ax.set(xlabel='Frequency (Hz)', ylabel='Amplitute (dB)')
ax.grid()
# fig.savefig("doesitwork.png")
plt.show()
