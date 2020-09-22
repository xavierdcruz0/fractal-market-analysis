import argparse
import matplotlib.pyplot as plt; plt.style.use('ggplot')
from fma.mmar.timeseries import __compute_multiplicative_cascade

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='get options for multifractal measure generator')
    parser.add_argument('--iters',dest='iters',type=int,help='number of iterations',default=4)
    parser.add_argument('--alloc',dest='alloc',type=float, nargs='+', help='M-1 allocations of mass',default=[0.6])
    parser.add_argument('--randomize',dest='randomize',type=bool,nargs='?',help='Randomize order of M',const=True)
    args=parser.parse_args()

    M = np.append(args.alloc, 1 - np.sum(args.alloc))
    x, y = __compute_multiplicative_cascade(args.iters, M, args.randomize)
    plt.step(x, y, where='post')
    plt.ylim(bottom=0)
    plt.xlim(0)
    # plt.xticks(x)
    plt.show()