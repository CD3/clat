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
  2.5 5
  $ seq 0 5 | clat-histogram -n 5
  0.5 1.0
  1.5 1.0
  2.5 1.0
  3.5 1.0
  4.5 1.0
  $ seq 0 5 | clat-histogram --normalize
  2.5 1.0
  $ seq 0 5 | clat-histogram -n 5 --normalize
  0.5 1.0
  1.5 1.0
  2.5 1.0
  3.5 1.0
  4.5 1.0






