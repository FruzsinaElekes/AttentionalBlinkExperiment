import yaml
from ABTrialClass import ABTrial 
from ABExperiment import ABExperiment
from Presenter import Presenter
from Participant import Participant

def run_experiment():
    config = yaml.safe_load(open("config.yaml"))
    presenter = Presenter(config)
    participant = Participant(presenter.ask_for_participant_number(), config)
    print(participant.yes_key)
    print(participant.participant_number)

    exp = ABExperiment(config)

if __name__ == "__main__":
    run_experiment()