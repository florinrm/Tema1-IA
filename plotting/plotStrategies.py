import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sc

def plotCosts():
    pass

def plotTime():
    x = np.array([1, 2, 3, 4, 5, 6])

    # DFS optimized
    y = np.array([0.782970666885376,
                  2.1262640953063965,
                  2.0796091556549072,
                  5.955679893493652,
                  11.619966745376587,
                  77.69423866271973])

    xnew = np.linspace(x.min(), x.max(), 6)
    spl = sc.make_interp_spline(x, y, k=3)  # BSpline object
    power_smooth = spl(xnew)

    plt.plot(xnew, power_smooth, label = "Depth-First Search - time (seconds)")
    plt.legend(title='Strategy')
    plt.show()

def main():
    plotTime()

if __name__ == '__main__':
    main()