import click
import fileinput
import subprocess
import math as m
from numpy import *


@click.command()
@click.version_option()
@click.argument("files",nargs=-1)
@click.option("-d","--delimiter",default=None,help="Use TEXT to split lines into columns.")
def avg_cmd(files,delimiter):
    """
    usage: clat-avg [FILE1 [FILE2 [...]] ]

    Computes the average of a list of numbers read from a list of files or standard input.
    
    If multiple columns of data exists (separated by the --delimiter option), the average for each
    column is computed.
    """
    sum = []
    num = []
    for line in fileinput.input(files=files if len(files) > 0  else ('-',) ):
      fields = line.split(delimiter)
      for i in range(len(fields)):
        try:
          x = float(fields[i])
          if i == len(sum):
            sum.append(0)
          if i == len(num):
            num.append(0)

          sum[i] += x
          num[i] += 1

        except:
          pass

    line = ""
    for i in range(len(sum)):
      line += " " + str(sum[i]/num[i])
    print(line.strip())



@click.command()
@click.version_option()
@click.argument("files",nargs=-1)
@click.option("-d","--delimiter",default=None,help="Use TEXT to split lines into columns.")
def sum_cmd(files,delimiter):
    """
    usage: clat-sum [FILE1 [FILE2 [...]] ]

    Computes the sum of a list of numbers read from a list of files or standard input.
    
    If multiple columns of data exists (separated by the --delimiter option), the sum for each
    column is computed.
    """
    sum = []
    for line in fileinput.input(files=files if len(files) > 0  else ('-',) ):
      fields = line.split(delimiter)
      for i in range(len(fields)):
        try:
          x = float(fields[i])
          if i == len(sum):
            sum.append(0)

          sum[i] += x

        except:
          pass

    line = ""
    for i in range(len(sum)):
      line += " " + str(sum[i])
    print(line.strip())



@click.command()
@click.version_option()
@click.argument("files",nargs=-1)
@click.option("-d","--delimiter",default=None,help="Use TEXT to split lines into columns.")
def rms_cmd(files,delimiter):
    """
    usage: clat-rms [FILE1 [FILE2 [...]] ]

    Computes the Root Mean Square (RMS) of a list of numbers read from a list of files or standard input.
    
    If multiple columns of data exists (separated by the --delimiter option), the RMS for each
    column is computed.
    """
    sum = []
    num = []
    for line in fileinput.input(files=files if len(files) > 0  else ('-',) ):
      fields = line.split(delimiter)
      for i in range(len(fields)):
        try:
          x = float(fields[i])
          if i == len(sum):
            sum.append(0)
          if i == len(num):
            num.append(0)

          sum[i] += x*x
          num[i] += 1

        except:
          pass

    line = ""
    for i in range(len(sum)):
      line += " " + str((sum[i]/num[i])**0.5 )
    print(line.strip())


@click.command()
@click.version_option()
@click.argument("files",nargs=-1)
@click.option("-d","--delimiter",default=None,help="Use TEXT to split lines into columns.")
@click.option("-b","--biased",is_flag=True,help="Use biased estimator (divide by n instead of n-1).")
def stddev_cmd(files,delimiter,biased):
    """
    usage: clat-stddev [FILE1 [FILE2 [...]] ]

    Computes the standard deviation of a list of numbers read from a list of files or standard input.
    
    If multiple columns of data exists (separated by the --delimiter option), the standard deviation for each
    column is computed.
    """
    avg = []
    sum = []
    num = []
    for line in fileinput.input(files=files if len(files) > 0  else ('-',) ):
      fields = line.split(delimiter)
      for i in range(len(fields)):
        try:
          x = float(fields[i])
          if i == len(avg):
            avg.append(0)
          if i == len(sum):
            sum.append(0)
          if i == len(num):
            num.append(0)

          num[i] += 1
          delta = x - avg[i]
          avg[i] += delta/num[i]
          delta2 = x - avg[i]
          sum[i] += delta*delta2

        except:
          pass

    line = ""
    for i in range(len(sum)):
      if num[i] < 2:
        line += "nan"
      else:
        N = num[i]
        if not biased:
          N = N - 1
        line += " " + str(m.sqrt(sum[i]/N))
    print(line.strip())


@click.command()
@click.version_option()
@click.argument("files",nargs=-1)
@click.option("-d","--delimiter",default=None,help="Use TEXT to split lines into columns.")
def unc_cmd(files,delimiter):
    """
    usage: clat-unc [FILE1 [FILE2 [...]] ]

    Computes the uncertainty (standard error of the mean) of a list of numbers read from a list of files or standard input.
    
    If multiple columns of data exists (separated by the --delimiter option), the uncertianty for each
    column is computed.
    """
    avg = []
    sum = []
    num = []
    for line in fileinput.input(files=files if len(files) > 0  else ('-',) ):
      fields = line.split(delimiter)
      for i in range(len(fields)):
        try:
          x = float(fields[i])
          if i == len(avg):
            avg.append(0)
          if i == len(sum):
            sum.append(0)
          if i == len(num):
            num.append(0)

          num[i] += 1
          delta = x - avg[i]
          avg[i] += delta/num[i]
          delta2 = x - avg[i]
          sum[i] += delta*delta2

        except:
          pass

    line = ""
    for i in range(len(sum)):
      if num[i] < 2:
        line += "nan"
      else:
        N = num[i]
        line += " " + str(m.sqrt(sum[i]/(N-1))/m.sqrt(N))
    print(line.strip())




@click.command()
@click.version_option()
@click.argument("files",nargs=-1)
@click.option("-n","--num-bins",type=int,help="Set the number of bins that will be used. If not given, a reasonable bin number is automatically calculated.")
@click.option("-N","--normalize",is_flag=True,help="Normalize the histogram so that it represents a probability distribution.")
def histogram_cmd(files,num_bins,normalize):
    """
    usage: clat-histogram [FILE1 [FILE2 [...]] ]

    Computes a histogram of from a list of numbers read from a list of files or standard input.
    """

    data = []

    for line in fileinput.input(files=files if len(files) > 0  else ('-',) ):
      try:
        x = float(line)
        data.append(x)
      except:
        pass

    n = len(data)
    min_ = min(data)
    max_ = max(data)


    def bin(data,min,max_,n):
      # bin width
      dx = (max_ - min_)/n # number of bins *is* number of intervals
      x = [ min_ + dx*(i+0.5) for i in range(n) ]
      count = [0]*n

      for d in data:
        i = int( (d - min_)/dx )
        if i >= n:
          i = n-1
        count[i] += 1

      return x,count



    # if the number of bins is not defined,
    # try to determine what the best bin count would be
    nbins = num_bins
    if num_bins is None:
      num_bins = int(n / 10)+1

    x,count = bin(data,min_,max_,num_bins)
    norm = 1
    if normalize:
      norm = sum(count)*(max_ - min_)/num_bins

    for i in range(len(x)):
      print(x[i],count[i]/norm)





@click.command()
@click.version_option()
@click.argument("files",nargs=-1)
def response_cmd(files):
    """
    usage: clat-response [FILE1 [FILE2 [...]] ]

    Counts yes/no responses to a stimuli.

    Data consists of two columns, a "dose" and a "response". Example:

    0.11 0
    0.11 1
    0.68 1
    0.11 0
    0.23 1
    0.23 0
    0.11 0
    0.23 1
    0.23 0
    0.68 1
    0.68 1
    0.68 1


    Would output


    0.11 1 4
    0.23 2 4
    0.68 4 4

    This is useful for analyzing damage threshold data.
    """


    data = {}

    for line in fileinput.input(files=files if len(files) > 0  else ('-',) ):
      tokens = line.split()
      try:
        x = float(tokens[0])
        if not x in data:
          data[x] = {'yes' : 0, 'total' : 0 }
        c = 1
        if len(tokens) > 1:
          c = int(tokens[1])
        data[x]['yes'] += c
        data[x]['total'] += 1
      except:
        pass

    for k in data:
      print(k,data[k]['yes'],data[k]['total'])


@click.command()
@click.version_option()
@click.argument("files",nargs=-1)
@click.option("-m","--modifiers",default="",help="Appends TEXT to the plot command.")
@click.option("-r","--pre",default="",help="Excecutes commands in TEXT before the plot command.")
@click.option("-o","--post",default="",help="Excecutes commands in TEXT after the plot command.")
@click.option("-i","--interactive",is_flag=True,help="Keep gnuplot running while plot is displayed so that you can interact with the window still.")
def plot_cmd(files,modifiers,pre,post,interactive):
    """
    usage: clat-plot [FILE1 [FILE2 [...]] ]

    Plot data read from FILES or standard input using Gnuplot.

    Example:

    This script essentailly builds a gnuplot command string that will plot data
    from the standard input. For example:

    > $0 -pre "set xrange[0:5]; set yrange[-1.5:1.5]" -pos "set term png; set output 'example.png'; rep" -modifiers "with linespoints title 'data'"

    will execute the following command.

    gnuplot -persist -e "set xrange[0:5]; set yrange[-1.5:1.5]; $cmd '-' with linespoints title 'data'; set term png; set output 'example.png'; rep"

    which will create a plot that is displayed on the screen and a file named example.png.

    """

    gnuplot_cmd = f"{pre}; plot '-' {modifiers}; {post};"
    if interactive:
        gnuplot_cmd += "pause mouse close;"


    subprocess.run( ["gnuplot","--persist", "-e", gnuplot_cmd])






@click.command()
@click.version_option()
@click.option(
    "-o",
    "--output",
    default="-",
    help="Write to file named TEXT instead of stdout.",
)
@click.option(
    "--n",
    type=str,
    default="10",
    help="EXPRESSION giving the number of nodes to evaluate the function at.",
)
@click.option(
    "--x",
    type=str,
    help="EXPRESSION that computes the the value of x (independent variable) for the i'th element. e.g. '0.1*{i} + 1.",
)
@click.option(
    "--x-min",
    type=str,
    default="0",
    help="EXPRESSION giving the minimum x value.",
)
@click.option(
    "--x-max",
    type=str,
    default="10",
    help="EXPRESSION giving the maximum x value.",
)
@click.option(
    "--y",
    type=str,
    default="{x}",
    help="EXPRESSION that computes the value of y (dependent variable) for a given x value. e.g. 'sin({x})'.",
)
def func_cmd(output,n,x_min,x_max,x,y):
    """
    WARNING: This tool runs `eval(...)` on almost all user input. You should NOT use it on input that is not 100% trusted!

    For example, this command

    $ func --x-min 'exec("import os; print(os.getcwd())")'

    will print the current working directory before erroring out with a TypeError.

    You have been warned...

    =========================

    Generate discretized functions from the command line.

    For example

    $ func -N 100 --x-min -2 --x-max 2 --y "exp(-({x}/0.1)**2)"

    Will print 100 points from a Gaussian function evauated between -2 and 2.

    All options identified as EXPRESSION are evaluated with eval(...), and the result is taken as the parameter's value.
    This allows the user to 'compute' the value for every parameter. For example, so output sin from 0 to 2 pi

    $ func -N 100 --x-min 0 --x-max 2*pi --y "sin({x})"

    The expression evaluation for the --x and --y options are first formatted with string.format(), so you can refer to a few special variables
    inside the expressing using the {varname} syntax. The special variables are:

    {N}     the total number of points that will be evaluated.

    {i}     the current loop index value. runs from 0 to N.

    {x_min} the value for x-min.

    {x_max} the value for x-max.

    {dx}    distance between evaluation points, dx = (x_max-xmin)/(N-1) (this is only true if the --x option has not been used to override the default).

    {x}     (only passed to --y expression) the current x value for the function to be evaluated.

    """

    if output == "-":
        output = "/dev/stdout"


    with open(output,"w") as f:
    
        xmin=eval(x_min)
        xmax=eval(x_max)
        N=eval(n)
        dx = (xmax-xmin)/(N-1)
        for i in range(N):
            if x:
                xval = eval(x.format(i=i,N=N,x_min=x_min,x_max=x_max,dx=dx))
            else:
                xval = eval("{x_min} + {dx}*{i}".format(i=i,N=N,x_min=xmin,x_max=xmax,dx=dx))

            yval = eval(y.format(i=i,N=N,x=xval,x_min=xmin,x_max=xmax,dx=dx))

            f.write(f"{xval} {yval}\n")
        



    





