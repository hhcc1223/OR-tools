"""
Packing problem OR tools
"""


from ortools.algorithms import pywrapknapsack_solver
from ortools.linear_solver import pywraplp

def Knapsackpackingsolution_single():
    data = {}
    data['Value'] =[
                    360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147, 
                    78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
                    87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
                    312]
    #a sequence
    data['Volumn'] = [[
                    7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
                    42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
                    3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]]
    data['limitation'] = [850]
    solver = pywrapknapsack_solver.KnapsackSolver(pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,'kNAPSACK')
    
    solver.Init(data['Value'], data['Volumn'], data['limitation'])
    computed_value = solver.Solve()
    packed_items = []
    packed_weights = []
    total_weight = 0
    print('Total value =', computed_value)
    for i in range(len(data['Value'])):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(data['Volumn'][0][i])
            total_weight += data['Volumn'][0][i]
    print('Total weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed_weights:', packed_weights)

def Knapsackpackingsolutio_multiple():
    data = {}
    data['Value'] =[10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25]
    data['Volumn'] = [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36]
    data['items']=list(range(len(data['Volumn'])))
    data['num_items'] = len(data['Volumn'])
    data['bin_limitation'] = [100,100,100,100,100]
    data['bins'] = list(range(len(data['bin_limitation'])))

    solver = pywraplp.Solver('multiple(knapsact', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING) 
    x = {}
    for i in data['items']:
        for j in data['bins']:
            x[(i, j)] = solver.IntVar(0, 1, 'x_%i_%i' % (i, j))
            
    # Constraints
    # Each item can be in at most one bin.
    for i in data['items']:
        solver.Add(sum(x[i, j] for j in data['bins']) <= 1)
    # The amount packed in each bin cannot exceed its capacity.
    for j in data['bins']:
        solver.Add(
            sum(x[(i, j)] * data['Volumn'][i]
                for i in data['items']) <= data['bin_limitation'][j])
    objective = solver.Objective()

    for i in data['items']:
        for j in data['bins']:
            objective.SetCoefficient(x[(i, j)], data['Value'][i])
    objective.SetMaximization()
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('Total packed value:', objective.Value())
        total_weight = 0
        for j in data['bins']:
            bin_weight = 0
            bin_value = 0
            print('Bin ', j, '\n')
            for i in data['items']:
                if x[i, j].solution_value() > 0:
                    print('Item', i, '- Volumn:', data['Volumn'][i], ' value:',
                          data['Value'][i])
                    bin_weight += data['Volumn'][i]
                    bin_value += data['Value'][i]
            print('Packed bin Volumn:', bin_weight)
            print('Packed bin value:', bin_value)
            print()
            total_weight += bin_weight
        print('Total packed Volumn:', total_weight)
    else:
        print('The problem does not have an optimal solution.')
    
    
    
    
if __name__ == '__main__':
    Knapsackpackingsolutio_multiple()