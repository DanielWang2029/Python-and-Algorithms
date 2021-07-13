import multiprocessing
from multiprocessing import Pool
import os, time

# target function
def target(n):
    print('Target:', n)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(10):
        mtp = multiprocessing.Process(target=target, args=(i,))
        jobs.append(mtp)
        mtp.start()
 
# Since target function is multiprocessed, the output of the above program might overlap with each other

# for example: 
# Target: 0Target:
#  1
# Target: 2
# Target: 3
# Target: 4Target:
#  5
# Target: 6
# Target: 7Target:
#  8
# Target: 9

# Without multiprocessing, the output should have been:
# Target: 0
# Target: 1
# Target: 2
# Target: 3
# Target: 4
# Target: 5
# Target: 6
# Target: 7
# Target: 8
# Target: 9


# pool
def target(name):
    print(f'Runing sub-process {name} ({os.getpid()}).')
    start = time.time()
    time.sleep(2)
    end = time.time()
    print(f'Sub-process {name} runs {(end - start):0.2f} seconds.')

if __name__=='__main__':
    print(f'Parent process {os.getpid()}.')
    p = Pool()
    for i in range(10):
        p.apply_async(target, args=(i,))
    print('Waiting for sub-processing to be finished.')
    p.close()
    p.join()
    print('All sub-processing done.')

# The above code prints:
# Parent process 135.
# Runing sub-process 1 (11717).Runing sub-process 2 (11718).Runing sub-process 0 (11716).Runing sub-process 3 (11719).Runing sub-process 5 (11721).Runing sub-process 4 (11720).Runing sub-process 6 (11722).Runing sub-process 7 (11723).Runing sub-process 8 (11724).Runing sub-process 9 (11725).
# Waiting for sub-processing to be finished.
# Sub-process 1 runs 2.00 seconds.Sub-process 3 runs 2.00 seconds.Sub-process 5 runs 2.00 seconds.Sub-process 8 runs 2.00 seconds.Sub-process 7 runs 2.00 seconds.
# Sub-process 9 runs 2.00 seconds.
# Sub-process 2 runs 2.00 seconds.Sub-process 0 runs 2.00 seconds.
# Sub-process 6 runs 2.00 seconds.Sub-process 4 runs 2.00 seconds.
# All sub-processing done.

# Without multiprocessing, the output should have been (something like):
# Parent process 135.
# Runing sub-process 0 (11716).
# Runing sub-process 1 (11717).
# Runing sub-process 2 (11718).
# Runing sub-process 3 (11719).
# Runing sub-process 4 (11721).
# Runing sub-process 5 (11720).
# Runing sub-process 6 (11722).
# Runing sub-process 7 (11723).
# Runing sub-process 8 (11724).
# Runing sub-process 9 (11725).
# Sub-process 0 runs 2.00 seconds.
# Sub-process 1 runs 2.00 seconds.
# Sub-process 2 runs 2.00 seconds.
# Sub-process 3 runs 2.00 seconds.
# Sub-process 4 runs 2.00 seconds.
# Sub-process 5 runs 2.00 seconds.
# Sub-process 6 runs 2.00 seconds.
# Sub-process 7 runs 2.00 seconds.
# Sub-process 8 runs 2.00 seconds.
# Sub-process 9 runs 2.00 seconds.
