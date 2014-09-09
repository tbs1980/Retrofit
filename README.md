# Retrofit


Code for Retrofit data analysis

## How to run the script

* Download the zip file from [repository](https://github.com/tbs1980/Retrofit)
* Unzip

Now you will see the script under the directory called `source`. To run the script go the directory `source` and type

  $ cd source
  $ python comparison_to_cibse.py PATH_TO_DATA COMUMN_DATE COLUMN_TEMP ROOM_TYPE

where `PATH_TO_DATA` is the path to data e.g `C:/data/TSB001.xlsx`, `COMUMN_DATE` is the column number corresponding to the date, `COLUMN_TEMP` is the column number of the temperature data and `ROOM_TYPE` the room type e.g. `livingroom`

For example you may type

  $ python comparison_to_cibse.py C:/data/TSB001.xlsx 0 1 livingroom

  file name : ./data/TSB001.xlsx
  date column : 0
  temperature column : 1
  room : livingroom
  output file : ./data/TSB001.xlsx.stats_1_livingroom.txt

  opening the file  ./data/TSB001.xlsx

  Done. Now computing the averages...

  Skipping the value  0 Device UUID
  Skipping the value  1 Reading type
  Skipping the value  2 Customer ref
  Skipping the value  3 Description
  Skipping the value  4 Location
  Skipping the value  5 Unit
  Skipping the value  6 Accuracy (percent)
  Skipping the value  7 Sample interval (seconds)
  Skipping the value  8 Frequency
  Skipping the value  9 Period
  Skipping the value  10 Parent UUID
  Skipping the value  11 Sensor range max
  Skipping the value  12 Sensor range min
  Skipping the value  97357 min
  Skipping the value  97358 max
  Skipping the value  97359 average
  Skipping the value  97360
  Skipping the value  97361
  Skipping the value  97362 Summer (May to beginning of October)
  Skipping the value  97363 min
  Skipping the value  97364 max
  Skipping the value  97365 average
  Skipping the value  97366
  Skipping the value  97367
  Skipping the value  97368 Heating season (October to end of April)
  Skipping the value  97369 min
  Skipping the value  97370 max
  Skipping the value  97371 average
  Skipping the value  97372
  Skipping the value  97373 Reading type
  Skipping the value  97374 Customer ref
  Skipping the value  97375 Description
  Skipping the value  97376
  Skipping the value  97377
  Skipping the value  97378
  Skipping the value  97379
  Skipping the value  97380 Min internal temperature (heating season)
  Skipping the value  97381 Max internal temperature (heating season)
  Skipping the value  97382 Average internal temperature (heating season)
  Skipping the value  97383 Average internal temperature (heating season) - living room
  Skipping the value  97384 Average internal temperature (heating season) - bedroom
  Skipping the value  97385 Min internal temperature (summer)
  Skipping the value  97386 Max internal temperature (summer)
  Skipping the value  97387 Average internal temperature (summer)
  Skipping the value  97388 Average humidity (internal)

  month mean min max thr-min thr-max greater-than-max% less-than-min%
  1 18.9963786455 16.4 21.5 22.0 23.0 100.0 0.0
  2 18.0162063714 15.7 21.7 22.0 23.0 100.0 0.0
  3 17.9597862323 14.83 22.6 22.0 23.0 99.707341901 0.0
  4 20.4728694045 17.1 23.89 22.0 23.0 74.3694704873 7.02495708438
  5 23.0729263566 19.6 25.8 -100.0 25.0 0.0 5.51679586563
  6 25.9710567043 23.0 30.37 -100.0 25.0 0.0 67.0937460358
  7 26.7476406089 23.12 30.1 -100.0 25.0 0.0 85.2296181631
  8 24.9880563344 20.3 26.9 -100.0 25.0 0.0 51.3892429263
  9 21.5436655168 13.3 25.27 -100.0 25.0 0.0 0.702695796602
  10 22.5641405044 20.0 25.3 22.0 23.0 26.4668039115 28.512609367
  11 20.7603119384 18.7 24.9 22.0 23.0 84.1463414634 4.83953786906
  12 19.8993683939 17.4 22.7 22.0 23.0 98.1567414282 0.0
