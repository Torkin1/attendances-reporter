# attendances-reporter

THE SOFTWARE IS PROVIDED "AS IS," AND MAKES NO EXPRESS OR IMPLIED WARRANTY OF ANY KIND. ALL INDIRECT OR IMPLIED WARRANTIES ARE DISCLAIMED TO THE FULL EXTENT ALLOWED BY APPLICABLE LAW, INCLUDING WITHOUT LIMITATION ALL IMPLIED WARRANTIES OF, NON-INFRINGEMENT, MERCHANTABILITY, TITLE OR FITNESS FOR ANY PARTICULAR PURPOSE.

This program reads students names from `students.txt` file, and reports which ones among them attended a meeting. The report generated also includes the name of the meetings the student attended and how many hours have been awarded for the attendances.

Attendances are checked searching for corresponding student names in meeting report csv files put in `meetings/` folder. Each meeting report must have the columns described in `meetings/template.csv`. The program can handle csv files with some arbitary rows (i.e. useless heading rows generated by MS Teams)

The report generated is stored in a csv file.

# How to use

1) Download the reporter clicking [here](https://github.com/Torkin1/attendances-reporter/archive/refs/heads/main.zip) and extract it (or check out the repo if you are a pro player)

2) Populate the `attendances-reporter-main/meetings` folder with attendances report csv files 

3) Populate the `students.txt` file with the Name and Surname of the students you want to check attendances for, one student per line (i.e. Mario La Rossa)

4) Launch the program `main.py`

```
$ ./main.py -h
usage: main.py [-h] [-d DURATION] [-p PRIZE] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -d DURATION, --duration DURATION
                        minimum duration of an attendance to be considered valid (in minutes). Default is 0
  -p PRIZE, --prize PRIZE
                        hours earned by a student if an attendance of theirs is considered valid. Default is 2
  -o OUTPUT, --output OUTPUT
                        name of generated report. Default is 'attendances.csv'
```

# Support

Contact me using the mail in my profile or on MS Teams at daniele.laprova@students.uniroma2.eu . You can also use the [Github Issue Tracker](https://github.com/Torkin1/attendances-reporter/issues) 
