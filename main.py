import math
import time
import matplotlib.pyplot as plt
import random

def generate_rand_signal(N):
    xt = list(range(0, N))
    start = time.time()
    time.sleep(1)
    harmonics = []
    for i in range(n_harm):
        A = random.randint(1, 100)
        fi = random.randint(1, 100)
        harmonics.append(list(map(
                        lambda x: A*math.sin(w_freq/(i+1)*xt.index(x) + fi),
            xt)))
    smth = list(zip(*harmonics))
    signal = []
    for el in smth:
        signal.append(sum(el))
    end = time.time() - start - 1
    return signal, harmonics, end


def get_Mx(rand_signal: list):
    start = time.time()
    time.sleep(1)
    Mx = sum(rand_signal)/N
    end = time.time() - start - 1
    return Mx, end


def get_Dx(rand_signal: list, mx: float):
    start = time.time()
    time.sleep(1)
    Dx = 0
    for i in range(N):
        Dx += (rand_signal[i] - mx)**2
    Dx = Dx/(N-1)
    end = time.time() - start - 1
    return Dx, end


def get_Rxx_func(rand_signal: list, mx: float, dx: float):
    start = time.time()
    time.sleep(1)
    func = []
    for tau in range((N - 1) // 2):
        cov_xx = 0
        for t in range((N-1)//2):
            cov_xx += (rand_signal[t] - mx)*(rand_signal[t+tau] - mx)
        cov_xx /= (N - 1)
        Rxx = cov_xx / (math.sqrt(dx) ** 2)
        func.append(Rxx)
    end = time.time() - start - 1
    return func, end


def get_Rxy_func(rand_signal1: list, mx1: float, dx1: float,
            rand_signal2: list, mx2: float, dx2: float):
    start = time.time()
    time.sleep(1)
    func = []
    for tau in range((N - 1) // 2):
        cov_xy = 0
        for t in range((N-1)//2):
            cov_xy += (rand_signal1[t] - mx1) * (rand_signal2[t + tau] - mx2)
        cov_xy /= (N - 1)
        Rxy = cov_xy /(math.sqrt(dx1)*math.sqrt(dx2))
        func.append(Rxy)
    end = time.time() - start - 1
    return func, end


n_harm = 10
w_freq = 1500
N = 256
x_t = list(range(0, N))

# Calculating
(res1, harmonics1, t1) = generate_rand_signal(N)
(res2, harmonics2, t2) = generate_rand_signal(N)
(res3, harmonics3, t3) = generate_rand_signal(N)

(Mx1, Mx1_time) = get_Mx(res1)
(Mx2, Mx2_time) = get_Mx(res2)
(Mx3, Mx3_time) = get_Mx(res3)
(Dx1, Dx1_time) = get_Dx(res1, Mx1)
(Dx2, Dx2_time) = get_Dx(res2, Mx2)
(Dx3, Dx3_time) = get_Dx(res3, Mx3)

Rxy = get_Rxy_func(res1, Mx1, Dx1, res2, Mx2, Dx2)[0]
Rxx = get_Rxx_func(res3, Mx3, Dx3)[0]

# Plotting
gridsize = (3, 2)
ax1 = plt.subplot2grid(gridsize, (0, 0))
ax2 = plt.subplot2grid(gridsize, (0, 1))
ax3 = plt.subplot2grid(gridsize, (1, 0))
ax4 = plt.subplot2grid(gridsize, (1, 1))
ax5 = plt.subplot2grid(gridsize, (2, 0))
ax6 = plt.subplot2grid(gridsize, (2, 1))

ax1.set_title('Harmonics 1')
ax2.set_title('Random signal 1')
ax3.set_title('Harmonics 2')
ax4.set_title('Random signal 2')
ax5.set_title('Harmonics 3')
ax6.set_title('Random signal 3')

for i in range(len(harmonics1)):
    ax1.plot(x_t, harmonics1[i])
ax2.plot(x_t, res1)

for i in range(len(harmonics2)):
    ax3.plot(x_t, harmonics2[i])
ax4.plot(x_t, res2)

for i in range(len(harmonics3)):
    ax5.plot(x_t, harmonics3[i])
ax6.plot(x_t, res3)

plt.show()

gridsize = (1, 2)
ax1 = plt.subplot2grid(gridsize, (0, 0))
ax2 = plt.subplot2grid(gridsize, (0, 1))

ax1.set_title('Correlation function')
ax2.set_title('Autocorrelation function')

ax1.plot(list(range(len(Rxy))), Rxy)
ax2.plot(list(range(len(Rxx))), Rxx)

plt.show()

print("1 сигнал ({0:.10} s) parameters\n"
      "Mx1 = {1:.5}  Mx1_time: {2:.10} seconds\n"
      "Dx1 = {3:.5}  Dx1_time: {4:.10} seconds\n".format(t1, Mx1, Mx1_time, Dx1, Dx1_time))

print("2 сигнал ({0:.10} s) parameters\n"
      "Mx2 = {1:.5}  Mx2_time: {2:.10} seconds\n"
      "Dx2 = {3:.5}  Dx2_time: {4:.10} seconds\n".format(t2, Mx2, Mx2_time, Dx2, Dx2_time))

print("3 сигнал ({0:.10} s) parameters\n"
      "Mx3 = {1:.5}  Mx3_time: {2:.10} seconds\n"
      "Dx3 = {3:.5}  Dx3_time: {4:.10} seconds".format(t3, Mx3, Mx3_time, Dx3, Dx3_time))