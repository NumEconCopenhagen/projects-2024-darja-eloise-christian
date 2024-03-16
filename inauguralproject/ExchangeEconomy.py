from types import SimpleNamespace

class ExchangeEconomyClass:

    def __init__(self):

        par = self.par = SimpleNamespace()

        # a. preferences
        par.alpha = 1/3
        par.beta = 2/3
        par.p2 = 1

        # b. endowments
        par.w1A = 0.8
        par.w2A = 0.3

    def utility_A(self,x1A,x2A):
        return x1A**(self.par.alpha)*x2A**(1-self.par.alpha)

    def utility_B(self,x1B,x2B):
        return x1B**(self.par.beta)*x2B**(1-self.par.beta)

    def demand_A(self,p1):
        demand_x1 =  self.par.alpha * (p1*self.par.w1A + self.par.w2A)/p1  
        demand_x2 = (1-self.par.alpha) * (p1*self.par.w1A + self.par.w2A)
        return demand_x1, demand_x2
    def demand_B(self,p1):
        demand_x1 = self.par.beta * (p1* (1-self.par.w1A) + 1- self.par.w2A)/p1 
        demand_x2 = (1-self.par.beta) *(p1* (1-self.par.w1A) + (1-self.par.w2A))
        return demand_x1, demand_x2
    
    # Check for Pareto improvements
    #def is_pareto_improvement(self, xA1, xA2, x1B, x2B):
     #   return self.utility_A(self, xA1, xA2) >= self.utility_A(self,x1A = par.w1A, x2A = par.w2A) and\
     #   self.utility_B(self, x1B, x2B) >= self.utility_B(self, x1B = 1-par.w1A, x2B = 1-par.w2A)

    def check_market_clearing(self,p1):

        par = self.par

        x1A,x2A = self.demand_A(p1)
        x1B,x2B = self.demand_B(p1)

        eps1 = x1A-par.w1A + x1B-(1-par.w1A)
        eps2 = x2A-par.w2A + x2B-(1-par.w2A)

        return eps1,eps2

## negative utility function defined
    
    def negative_utility_A(self,p1):
        x1 = 1 - (self.par.beta * (p1* (1-self.par.w1A) + 1- self.par.w2A)/p1)
        x2 = 1 - ((1-self.par.beta) *(p1* (1-self.par.w1A) + (1-self.par.w2A)))
        return -(x1**(self.par.alpha)*x2**(1-self.par.alpha))

    