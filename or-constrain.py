''' 
Google OR tool Constrain Optimization
for feasible solutions

May-28-2020
'''

from ortools.sat.python import cp_model

model = cp_model.CpModel()

num_vals = 3
x = model.NewIntVar(0, 2,'1')
y = model.NewIntVar(0, 2,'2')
z = model.NewIntVar(0, 2,'3')

model.Add(x!=y)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
    print('x = %i' % solver.Value(x))
    print('y = %i' % solver.Value(y))
    print('z = %i' % solver.Value(z))