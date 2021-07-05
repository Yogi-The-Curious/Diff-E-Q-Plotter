class SlopeField:
    ivp_solutions = {} # add ivp solutions here, not sure what we are gonna do for this

    def __init__(self):
        pass

    '''
    Takes in necessary parameters for plotting slope field and plots field accordingly, 
    '''
    def plot_field(self):
        pass

    '''
    adds ivp info to the dictionary, not sure if the dict is the best source for this but it will hold the place for the proper
    data type for now.   
    '''

    def add_ivp(self, ivp):
        self.ivp_solutions[len(self.ivp_solutions)+1] = ivp
        pass

    '''
    Reloads all IVP's onto the slope field. 
    '''
    def update_all_ivp(self):
        pass

    '''
    private function that clears the ivp 
    '''
    def clear_ivp(self):
        pass