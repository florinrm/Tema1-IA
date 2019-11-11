import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sc


def plotTime():
    x = np.array([1, 2, 3, 4, 5, 6])

    # DFS optimized

    optimized = np.array([1016,
                        1071,
                            1071,
                            1046,
                            1088,
                            1073])


    unoptimized = np.array([1016,
                            1071,
                            1071,
                            1046,
                            1088,
                            1073])

    xnew = np.linspace(x.min(), x.max(), 4)

    spl_optimized = sc.make_interp_spline(x, optimized, k=3)  # BSpline object
    power_smooth_optimized = spl_optimized(xnew)
    

    plt.plot(xnew, power_smooth_optimized, label="Manhattan")
    #plt.legend(title='A Star - Manhattan')
    # plt.show()


    spl_unoptimized = sc.make_interp_spline(x, unoptimized, k=3)  # BSpline object
    power_smooth_unoptimized = spl_unoptimized(xnew)

    plt.plot(xnew, power_smooth_unoptimized, label="Euclidian")
    plt.legend(title='A Star Search - cost')
    plt.show()
# -no-fuel


def main():
    plotTime()


if __name__ == '__main__':
    main()
