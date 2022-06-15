# need to import torch first, otherwise we get an error on perlmutter when we import get_trials
import torch
from spaceray.spaceray import get_trials
from skopt import Optimizer
from pebble imort concurrent

class SlurmHPOManager:
    def __init__(self, json_file, db_file, objective_func, check_interval=60, n_trials=10):
        # initialization of hyperspace/skopt trials
        self.json_file = json_file
        self.space, self.bounds = get_trials(json_file)
        # create database file
        self.db_file = db_file
        self.optimizers = []
        for s in self.space:
            optimizer = Optimizer(s, random_state=0, n_initial_points=10)
            self.optimizers.append(optimizer)
        # parameters
        self.check_interval = check_interval
        self.n_trials = n_trials

    def submit(self):
        pass

    def run_spaces(self):
        # for each space, submit potential options
        pass

    def run_trial(self, optimizer_index):
        opt = self.optimizers[optimizer_index]
        # get a set of parameters to try
        params = opt.ask()
        # TODO: submit a slurm job with those options
        # TODO: check periodicially for result of slurm job
        # TODO: fetch slurm result and update optimizer, then return


    def run(self):
        # run each optimizer in parallel
        pass


class OptimizerManager:
    def __init__(self, optimizer):
        self.optimizer = optimizer
