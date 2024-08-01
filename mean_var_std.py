import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    calculations = np.array(list)
    calculations = calculations.reshape(3,3)
    
    mean_calculations = [np.mean(calculations,axis=0).tolist(),np.mean(calculations,axis=1).tolist(),np.mean(calculations).tolist()]
    variance_calculations = [np.var(calculations,axis=0).tolist(),np.var(calculations,axis=1).tolist(),np.var(calculations).tolist()]
    sd_calculations = [np.std(calculations,axis=0).tolist(),np.std(calculations,axis=1).tolist(),np.std(calculations).tolist()]
    max = [np.max(calculations,axis=0).tolist(),np.max(calculations,axis=1).tolist(),np.max(calculations).tolist()]
    min = [np.min(calculations,axis=0).tolist(),np.min(calculations,axis=1).tolist(),np.min(calculations).tolist()]
    sum = [np.sum(calculations,axis=0).tolist(),np.sum(calculations,axis=1).tolist(),np.sum(calculations).tolist()]
    

    values = [mean_calculations,variance_calculations,sd_calculations,max,min,sum]
    keys = ['mean','variance','standard deviation','max','min','sum']

    calculations = {keys[i]: values[i] for i in range(len(values))}

    return calculations
