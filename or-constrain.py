''' 
Google OR tool Constrain Optimization
for feasible solutions

May-28-2020
'''

from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count
    
    
def co1():
    model = cp_model.CpModel()
    
    x = model.NewIntVar(0, 25,'x')
    y = model.NewIntVar(0, 7, 'y')
    z = model.NewIntVar(0, 16,'z')
    
    model.Add(2*x+ 7*y+3*z<=50)
    model.Add(3*x - 5*y + 7*z <= 45)
    model.Add(5*x + 2*y - 6*z <= 37)
    
    model.Maximize(2*x+2*y+3*z)
    
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL:
        print('x = %i, y = %i, z = %i' %(solver.Value(x),solver.Value(y),solver.Value(z)))


    
def crypuzzles():
    
    model = cp_model.CpModel()
    
    c = model.NewIntVar(1,9,'c')
    p = model.NewIntVar(0,9,'p')
    i = model.NewIntVar(1,9,'i')
    s = model.NewIntVar(0,9,'s')
    f = model.NewIntVar(1,9,'f')
    u = model.NewIntVar(0,9,'u')
    n = model.NewIntVar(0,9,'n')
    t = model.NewIntVar(1,9,'t')
    r = model.NewIntVar(0,9,'r')
    e = model.NewIntVar(0,9,'e')
    
    viarables = [c,p,i,s,f,u,n,t,r,e]
    model.AddAllDifferent(viarables)
    model.Add(c*10 + p + i*10 + s + f*100 + u*10 + n == t*10**3 + r*100 + u*10 + e)
    
    solver = cp_model.CpSolver()
    solution = VarArraySolutionPrinter(viarables)
    solver.SearchForAllSolutions(model, solution)
    
    print("Total number solution: %i" %(solution.solution_count()))
    print('wall time:%f s' % solver.WallTime() )
    
crypuzzles()
    
    