"""Running CapsGNN."""

from fxcn import tab_printer
from capsgnn import CapsGNNTrainer
from param_parser import parameter_parser

def main():

    args = parameter_parser()
    tab_printer(args)
    model = CapsGNNTrainer(args)
    model.fit()
    model.score()
    model.save_predictions()

if __name__ == "__main__":
    main()
