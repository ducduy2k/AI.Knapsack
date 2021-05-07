from ortools.algorithms import pywrapknapsack_solver
import resource
def memory_limit():
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (10, hard))

def get_memory():
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free_memory += int(sline[1])
    return free_memory
def readfile():
    f=open("test.txt")
    f.readline()
    a=f.readline()
    capacities=[int(f.readline())]
    f.readline()
    values=[]
    weights=[[]]
    for i in range(int(a)):
        x,y=f.readline().split()
        values.append(int(x)),weights[0].append(int(y))
    f.close()
    return capacities,values,weights
def main():
    # Create the solver.
    memory_limit()
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    capacities,values,weights=readfile()
    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    f=open('result.csv','a')
    f.write(','+str(total_weight)+','+str(computed_value))
    # print('Packed items:', packed_items)
    # print('Packed_weights:', packed_weights)
    f.close()


if __name__ == '__main__':
    main()