# clat

Command Line Analysis Tools: A collection of tools for doing data analysis.

This project started out as a small collection of example scripts to learn about using Python for simple
data analysis at the command line and grew into a collection of utilities I have found useful.

## Installation

Install this tool using `pip`:

    $ pip install clat

## Usage

`clat` consists of several different commands, all named with the `clat-` prefix. For example, `clat-avg` computes the average of a set of numbers. It behaves like a standard UNIX filter program.

```bash
set 10 | clat-avg
5.5
```

There are scripts for computing the sum, standard deviation, generating histograms, plotting, and more. To see a list of available tools, just type `clat-` and then press `<TAB>` a couple of times. All commands
accept the `--help` option.
