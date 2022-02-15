  $ clat-avg --version
  clat-avg, version .* (re)
  $ echo 1 1 1 > data.txt
  $ echo 2 2 3 >> data.txt
  $ echo 3 4 4 >> data.txt
  $ cat data.txt | clat-avg
  2\.0[^\s]* 2\.33[^\s]* 2\.66[^\s]* (re)
  $ cat data.txt | clat-sum
  6\.0[^\s]* 7\.0[^\s]* 8\.0[^\s]* (re)
  $ cat data.txt | clat-stddev
  1\.0[^\s]* 1\.527525[^\s]* 1\.527525[^\s]* (re)
  $ cat data.txt | clat-stddev -b
  0\.816496[^\s]* 1\.24721[^\s]* 1\.24721[^\s]* (re)
  $ cat data.txt | clat-unc
  0\.57735[^\s]* 0\.88191[^\s]* 0\.88191[^\s]* (re)
  $ cat data.txt | clat-rms
  2\.160246[^\s]* 2\.64575131[^\s]* 2\.943920[^\s]* (re)


  $ seq 0 5 | clat-histogram
  2.5 6.0
  $ seq 0 5 | clat-histogram -n 5
  0.5 1.0
  1.5 1.0
  2.5 1.0
  3.5 1.0
  4.5 2.0
  $ seq 0 5 | clat-histogram --normalize
  2.5 0.2
  $ seq 0 5 | clat-histogram -n 5 --normalize
  0.5 0.166.* (re)
  1.5 0.166.* (re)
  2.5 0.166.* (re)
  3.5 0.166.* (re)
  4.5 0.333.* (re)

  $ clat-func --x-min -1 --x-max 1 --n 5 --y '({x})**2'
  -1.0 1.0
  -0.5 0.25
  0.0 0.0
  0.5 0.25
  1.0 1.0

  $ cat data.txt | clat-transform '$1'
  1
  2
  3

  $ cat data.txt | clat-transform '$1,$2*$3'
  1 1
  2 6
  3 16

  $ cat data.txt | clat-filter '$1 > 2'
  3 4 4
  $ cat data.txt | clat-filter '$1 > 2' -n
  1 1 1
  2 2 3
  $ cat data.txt | clat-filter '$3 > 3 or $1 < 2'
  1 1 1
  3 4 4

  $ cat data.txt | clat-plot
  $ cat data.txt | clat-plot -i



