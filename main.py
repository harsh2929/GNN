"""Running CapsGNN."""

from fxcn import tab_printer
from capsgnn import CapsGNNTrainer
from param_parser import parameter_parser

def main():
    # Parse command line arguments
    args = parameter_parser()

    # Print table of parameters
    tab_printer(args)

    # Initialize CapsGNN trainer
    trainer = CapsGNNTrainer(args)

    # Fit the model
    trainer.fit()

    # Evaluate the model
    trainer.score()

    # Save model predictions
    trainer.save_predictions()

if __name__ == "__main__":
    main()
