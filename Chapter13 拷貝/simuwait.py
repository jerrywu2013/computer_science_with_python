# L-13 MCS 260 : simuwait.py
"""
Simulate processing of jobs to compute waiting times.
"""

def form(data):
    """
    Given in data a list of floats, returns a string
    that contains the floats in %.2f format.
    """
    result = '[ ' + '%.2f' % data[0]
    for i in range(1, len(data)):
        result += ', ' + '%.2f' % data[i]
    return result + ' ]'

def ask():
    """
    Prompts the user for the parameters of the simulation:
    nbjobs : the number of jobs,
    time : the length of simulation time,
    mean : the average time per job,
    sigma : the deviation in procesing times.
    Returns the tuple (nbjobs, time, mean, sigma).
    """
    nbjobs = int(input('number of jobs : '))
    time = int(nput('length of time : '))
    mean = float(input(' mean time/job : '))
    sigma = float(input(' deviation/job : '))
    return (nbjobs, time, mean, sigma)

def make_jobs(nbjobs, time, mean, sigma):
    """
    Given the parameters of the simulation,
    returns tuple of two lists with arrival
    and process times for each job.
    """
    atime = [] # arrival times of jobs
    ptime = [] # time to process each job
    import random
    for i in range(0, nbjobs):
        atime.insert(0, random.uniform(0, time))
        ptime.insert(0, random.gauss(mean, sigma))
        print('job', i, ':', atime[0], ptime[0])
    atime.sort()
    return (atime, ptime)

def simulate(arr, prc):
    """
    Given a list of arrivals and process times,
    returns a list of wait times for each job.
    """
    result = [0]   # no wait for first job
    busy = prc[0]  # time busy for job
    for i in range(1, len(arr)):
        elp = arr[i] - arr[i-1] # elapsed time
        if elp >= busy:         # idle printer
            busy = 0            # no wait
        else:                   # busy printer
            busy = busy - elp   # wait
        result.append(busy)     # store wait
        busy = busy + prc[i]    # update busy
    return result

def avgdev(wait):
    """
    Returns a tuple with the average and
    standard deviation of the numbers in wait.
    """
    from math import sqrt
    avg = sum(wait)/len(wait)
    dev = 0
    for i in range(0, len(wait)):
        dev += (wait[i] - avg)**2
    dev = sqrt(dev)
    return (avg, dev)

def main():
    """
    Simulation of waiting times.
    """
    (dim, dur, mean, sigma) = ask()
    (arv, prc) = make_jobs(dim, dur, mean, sigma)
    print(' arrivals : ' + form(arv))
    print('job times : ' + form(prc))
    wait = simulate(arv, prc)
    print('wait times : ' + form(wait))
    (avg, dev) = avgdev(wait)
    print('average wait : %.2f' % avg)
    print('   deviation : %.2f' % dev)

main()
