# need to import torch first, otherwise we get an error on perlmutter when we import get_trials
import torch
from spaceray.spaceray import get_trials
from skopt import Optimizer
from pebble imort concurrent
from uuid import uuid4

class SlurmHPOManager:
    def __init__(self, json_file, db_file, objective_func, check_interval=60, n_trials=10):
        # initialization of hyperspace/skopt trials
        self.json_file = json_file
        self.spaces, self.bounds = get_trials(json_file)
        # create database file
        self.db_file = db_file

        self.optimizers = []
        for s in self.spaces:
            optimizer = Optimizer(s, random_state=0, n_initial_points=10)
            optimizer_manager = OptimizerManager(optimizer, self.bounds)
            self.optimizers.append(optimizer_manager)
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
        params = opt.get_trial()
        # TODO: submit a slurm job with those options
        # TODO: check periodicially for result of slurm job
        # TODO: fetch slurm result and update optimizer with the result, then return -
        #  update with opt.optimizer.tell(x, y)


    def run(self):
        # check each optimizer in serial - can be in parallel but probably not super necessary
        pass


class OptimizerManager:
    def __init__(self, optimizer, bounds):
        self.optimizer = optimizer
        self.bounds = bounds
        self.current_trial = None
        self.num_trials_run = 0
        self.results = {}
        self.trial_names = {}

    def get_trial(self):
        x = self.optimizer.ask()
        # convert to dictionary
        y = dict(zip(self.bounds.keys(), x))
        # get a unique trial name
        trial_name = str(uuid4())
        self.results[trial_name] = None
        self.trial_names[trial_name] = y
        self.current_trial = trial_name
        return y, trial_name

    def check_result(self):
        pass

    def run(self):
        # get an option and submit it to slurm
        # periodically check if the job has completed

