import yaml
from modules.Trial import Trial 
from modules.Experiment import Experiment
from modules.Presenter import Presenter
from modules.Participant import Participant
from modules.FileWriter import FileWriter

def main():
    config = yaml.safe_load(open("config.yaml"))
    presenter = Presenter(config)
    participant = Participant(
        presenter.ask_for_participant_number(), 
        *config["vars"]["part_keys"])
    file_writer = FileWriter(participant)

    exp = Experiment(participant, presenter, file_writer, config)
    exp.run()

if __name__ == "__main__":
    main()