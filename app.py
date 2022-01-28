#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser, Namespace
from chris_plugin import chris_plugin

parser = ArgumentParser(description='cli description')
parser.add_argument('-e', '--example', default='jelly',
                    help='argument which does not do anything')


# documentation: https://fnndsc.github.io/chris_plugin/
@chris_plugin(
    parser=parser,
    title='My ChRIS plugin',
    category='',                 # ref. https://chrisstore.co/plugins
    min_memory_limit='100Mi',    # supported units: Mi, Gi
    min_cpu_limit='1000m',       # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0              # set min_gpu_limit=1 to enable GPU
)
def main(options: Namespace, inputdir: Path, outputdir: Path):
    print(f'Option: {options.example}')


if __name__ == '__main__':
    main()
