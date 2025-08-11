import fileinput
import math as m
import re
import subprocess
import sys

import click
import scipy.interpolate
import scipy.optimize
from numpy import *
from scipy.special import *


@click.command()
@click.version_option()
@click.argument("files", nargs=-1)
@click.option(
    "-d", "--delimiter", default=None, help="Use TEXT to split lines into columns."
)
@click.option(
    "-o", "--output-delimiter