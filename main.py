import yaml
from ABTrialClass import ABTrial 
from ABExperiment import ABExperiment
from Presenter import Presenter
from Participant import Participant
from FileWriter import FileWriter

def main():
    config = yaml.safe_load(open("config.yaml"))
    presenter = Presenter(config)
    participant = Participant(
        presenter.ask_for_participant_number(), 
        *config["vars"]["part_keys"])
    file_writer = FileWriter(participant)

    exp = ABExperiment(participant, presenter, file_writer, config)
    exp.run()

if __name__ == "__main__":
    main()