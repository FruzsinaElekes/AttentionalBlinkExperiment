import yaml
from ABTrialClass import ABTrial 

def run_experiment():
    config = yaml.safe_load(open("config.yaml"))
    trial = ABTrial(1, 3, 2, config)

if __name__ == "__main__":
    run_experiment()