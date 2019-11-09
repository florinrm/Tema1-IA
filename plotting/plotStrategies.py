import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sc


def plotTime():
    x = np.array([1, 2, 3, 4, 5, 6])

    # DFS optimized
    '''
    optimized = np.array([136,
                          493,
                          493,
                          869])
                          '''

    unoptimized = np.array([10,
                            15,
                            35,
                            12,
                            12,
                            32])

    xnew = np.linspace(x.min(), x.max(), 4)
    '''
    spl_optimized = sc.make_interp_spline(x, optimized, k=3)  # BSpline object
    power_smooth_optimized = spl_optimized(xnew)
    

    plt.plot(xnew, power_smooth_optimized, label="Optimized")
    plt.legend(title='A Star - number of states')
    # plt.show()
    '''

    spl_unoptimized = sc.make_interp_spline(x, unoptimized, k=3)  # BSpline object
    power_smooth_unoptimized = spl_unoptimized(xnew)

    plt.plot(xnew, power_smooth_unoptimized, label="cost")
    plt.legend(title='A Star Search')
    plt.show()
# -no-fuel


def main():
    plotTime()


if __name__ == '__main__':
    main()
