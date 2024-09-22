#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python based test rig and selected solutions for project euler"""

import os, sys
import click
import importlib.util
import pprint
import re
import time
import tomllib


__authors__ = "Ravi Pun, Ryan Miller"
__version__ = "0.0.1"


class tc:
    reset = '\033[0m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[34m'
    cyan = '\033[36m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'

# tomllib doesn't support writing toml files from objects,
# so this is raw toml text
DEFAULT_CONFIG = """
inputs = "./input_files"
solutions = "./solutions"
answers = "./answers"
"""

CONFIG_FILENAME = "pyeuler_config.toml"
SOLUTION_REGEX = r"\d+"

class Solution:
    def __init__(self, config, dir_entry):
        self.config = config
        self.dir_entry = dir_entry

    def __repr__(self):
        in_file = self.__input_file().name if self.__input_file() != None else '-'
        number = f'{self.number:04}' if self.number != None else '-'
        return f'Solution({number}, {self.dir_entry.name}, {in_file})'

    @staticmethod
    def __file_number(file_name):
        found = re.search(SOLUTION_REGEX, file_name)
        return int(found.group()) if found != None else None

    @property
    def number(self):
        return Solution.__file_number(self.dir_entry.name)

    def __input_file(self):
        input_file = None
        for de in os.scandir(self.config['inputs']):
            if Solution.__file_number(de.name) == self.number:
                input_file = de
        return input_file

    def __answer_file(self):
        answer_file = None
        for de in os.scandir(self.config['answers']):
            if Solution.__file_number(de.name) == self.number:
                answer_file = de
        return answer_file

    @property
    def answer(self):
        an_file = self.__answer_file()
        if an_file == None:
            return None
        with open(an_file.path, 'r') as an_data:
            answer_data = an_data.read().strip()
        return answer_data

    @property
    def path(self):
        return self.dir_entry.path

    @property
    def name(self):
        return self.dir_entry.name

    @property
    def input(self):
        in_file = self.__input_file()
        if in_file == None:
            return None
        with open(in_file.path, 'r') as in_data:
            input_data = in_data.read().strip()
        return input_data


@click.group()
def cli():
    pass


@cli.command()
def config():
    if not os.path.exists(CONFIG_FILENAME):
        print("No config found..")
        with open(CONFIG_FILENAME, 'w') as cf:
            cf.write(DEFAULT_CONFIG)
            print("created pyeuler_config.toml")
            return

    pprint.pprint(read_config())


def read_config():
    with open(CONFIG_FILENAME, 'r') as cf:
        return tomllib.loads(cf.read())


@cli.command()
@click.option('-p', '--problem')
def solve(problem=None, speed=None):
    config = read_config()
    solutions = get_solutions(config['solutions'])
    if problem != None:
        solutions = filter(lambda s: s.number == int(problem), solutions)
    for sol in sorted(solutions, key=lambda s: s.number):
        test_solution(sol)

def get_solutions(solution_path):
    solutions = []
    config = read_config()
    for item in os.scandir(solution_path):
        if item.is_file() and item.name.endswith('.py') \
                and re.match(r"\D*\d+", item.name):
            solutions.append(Solution(config, item))
    return solutions


def test_solution(sol):
    print(f"{sol.name} ..", end="")
    try:
        loader = importlib.machinery.SourceFileLoader(sol.name, sol.path)
        spec = importlib.util.spec_from_loader(sol.name, loader)
        solmodule = importlib.util.module_from_spec(spec)
        loader.exec_module(solmodule)

        if solmodule.solution != None:
            start = time.time()
            result = solmodule.solution(sol.input)
            end = time.time()
            taken = end - start
            taken_str = f"{tc.yellow}{taken:.4f}s{tc.reset}"
            if result == sol.answer:
                print(f" {tc.green}{result}{tc.reset} in {taken_str}")
            else:
                print(f"got {tc.red}result{tc.reset}, wanted {tc.lightblue}{sol.answer}{tc.reset} in {taken_str}")
    except Exception as e:
        print(e)



if __name__ == "__main__":
    cli()

