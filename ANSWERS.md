# System

For reproducability, the code was run on Ubuntu 24.04.3 LTS

# Setup

I begin with setting up a bash script to install all the relevant programs and packages

The setup scipt also creates an empty sqlite database that I will use for storing the data

run it by using 
```
./setup_environment.sh
```

# Question 1. 

Goal is to save the data from the API in a database. We start with the measurements:

- create a sqlite database in the repo
- create a table for the measurements with all the relevant columns
- create extract.py
- create transform.py
- create load.py
- check data in notebook
