import sys

    # Sample Input
    # 2 - Number of Instances
    # 1 - Number of jobs
    # 1 4 - (# #)
    # 3
    # 1 2
    # 3 4
    # 2 6

def myFunc(e):
  return e[1]

def main():
    ans = ""
    sysnext = next(sys.stdin)
    num_instances = int(sysnext.strip())
    while num_instances > 0:
        sysnext = next(sys.stdin)
        num_jobs = int(sysnext.strip())
        jobs = []
        for _i in range(num_jobs):
            sysnext = next(sys.stdin)
            start_time = int(sysnext.strip().split()[0])
            end_time = int(sysnext.strip().split()[1])
            job = [start_time, end_time]
            jobs.append(job)
        jobs.sort(key=myFunc)
        # time to find out how many jobs :)
        instance = []
        for job in jobs:
            # only deal with valid job start/end times i.e. 5 0 is invalid
            if job[0] < job[1]:
                if len(instance) == 0:
                    instance.append(job)
                else:
                    if job[0] > instance[-1][1]:
                        instance.append(job)
        ans += str(len(instance)) + '\n'
        num_instances -= 1
    print(ans.strip())
# Using the special variable 
# __name__
if __name__=="__main__":
    main()