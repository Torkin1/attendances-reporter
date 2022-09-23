#! /usr/bin/python

import csv
import os
import argparse

HOURS_PRIZE = None    # hours earned by a student if an attendance of theirs is considered valid
DURATION_MIN = None  # minimal duration in seconds for an attendance to be considered valid
REPORT_NAME = None # name of generated report

class Attendance:

    def __init__(self, conference):
        self.conference=conference

class Student:
    name=""
    surname=""
    attended=[]

def readStudents():
    students = []
    with open("students.txt", "r") as f:
        for line in f:
            students.append(line[:-1])
    return students


def areStudentNamesEqual(s1, s2):
    # student names written in the following ways are considered equal:
    # name and surname inverted,
    # caps instead of lowercase (and viceversa)
    
    s1_lowercase = s1.casefold()
    s2_lowercase = s2.casefold

    s1_tokens = s1.split(" ")
    for token in s1_tokens:
        if token not in s2:
            return False
    return True

def getRegisteredStudentName(students, s):
    for student in students:
        if areStudentNamesEqual(student, s):
            return student
    return None

def toSeconds(duration):
    tokens = duration.split(" ")
    seconds = 0
    for token in tokens:
        if "h" in token:
            seconds += 60 * 60 * int(token[:-1])
        elif "min" in token:
            seconds += 60 * int(token[:-3])
        elif "sec" in token:
            seconds += int(token[:-3])
    return seconds

def readAttendances(students, attendances, hours):
    for fileName in os.listdir("meetings/"):
        with open("meetings/" + fileName, "r") as f:
            reader = csv.DictReader(f, delimiter=',', quotechar=str(u'"'))
            for row in reader:
                try:
                    attendee = row["Nome e cognome"]
                    if toSeconds(row["Durata"]) >= DURATION_MIN:
                        registeredAttendee = getRegisteredStudentName(students, attendee)
                        if registeredAttendee is not None:
                            attendances[registeredAttendee].append(Attendance(fileName[:-4]))
                            hours[registeredAttendee] += HOURS_PRIZE
                except KeyError:    
                    pass    # Lines without student names and attendance timings are ignored

def formatAttendances(studentAttendances):
    formatted = ""
    for a in studentAttendances:
        formatted += ("- " + a.conference + "\n")
    return formatted

def printAttendances(students, attendances, hours):
    with open(REPORT_NAME + ".csv","w") as attendancesFile:
        writer = csv.writer(attendancesFile, delimiter=",")
        writer.writerow(["student", "meetings attended", "total hours computed"])
        for s in students:
            writer.writerow([s, formatAttendances(attendances[s]), hours[s]])


if __name__ == "__main__":
    
    # parses arguments from command line
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--duration", help="minimum duration of an attendance to be considered valid (in minutes). Default is 0", type=int, default=0)
    parser.add_argument("-p", "--prize", help="hours earned by a student if an attendance of theirs is considered valid. Default is 2", type=int, default=2)
    parser.add_argument("-o", "--output", help="name of generated report. Default is 'attendances.csv'", type=str, default="attendances")
    
    args = parser.parse_args()

    DURATION_MIN = args.duration * 60
    HOURS_PRIZE = args.prize
    REPORT_NAME = args.output
    
    # prepares table with student names and their attendances
    students = readStudents()
    attendances = {}
    hours = {}
    for s in students:
        attendances[s] = []
        hours[s] = 0

    # parses attendances from csv files and prints them in another csv file
    readAttendances(students, attendances, hours)
    printAttendances(students, attendances, hours)
