import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sc


def plotTime():
    x = np.array([1, 2, 3, 4, 5, 6])

    # DFS optimized

    optimized = np.array([0.06131577491760254,
                            0.2790355682373047,
                            0.27101755142211914,
                            0.7714240550994873,
                            1.0099232196807861,
                            3.621021032333374])


    unoptimized = np.array([0.06203269958496094,
                            0.25005030632019043,
                            0.25218701362609863,
                            0.7016632556915283,
                            0.9390418529510498,
                            3.5696239471435547])

    xnew = np.linspace(x.min(), x.max(), 4)

    spl_optimized = sc.make_interp_spline(x, optimized, k=3)  # BSpline object
    power_smooth_optimized = spl_optimized(xnew)
    

    plt.plot(xnew, power_smooth_optimized, label="Manhattan")

    spl_unoptimized = sc.make_interp_spline(x, unoptimized, k=3)  # BSpline object
    power_smooth_unoptimized = spl_unoptimized(xnew)

    plt.plot(xnew, power_smooth_unoptimized, label="Euclidian")
    plt.legend(title='Recursive Best First Search - time')
    plt.show()
# -no-fuel


def main():
    plotTime()


if __name__ == '__main__':
    main()
