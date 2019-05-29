# Logparser, Udacity Fullstack Nanodegree Project One

This script queries the newsdata.sql Postgres database to answer the questions
asked on the [Project Description Page](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/b1bc900a-44ea-43e9-a51b-d3313705277f) for the project
and outputs the answers to the console in plain text.

## Getting started  
These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes. A larger project would have
a "deployment" section in this README for production systems, but that is
overkill for our purposes.  

Simply navigate to the directory where you downloaded the script and run it by
typing `python parser.py`  

### Prerequisites
```  
Postgres >= 9.5.17  
python >= 3.5.2  
```

### Installing  
1. Download sample Postgres database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).  
2. Extract the `newsdata.sql` file.  
3. In the directory where you just extracted the file, run `psql -d news -f newsdata.sql`  
4. Get this script onto your machine. clone this repository using   
`git clone https://github.com/isaac-friedman/fullstack-nanodegree-1.git` or download as a zip and extract.  
You can even open the script on GitHub and just copy-paste.

### Using  
Simply navigate to the directory where you downloaded the script and run it by
typing `python parser.py`  

### Authors  
* __Isaac Friedman__

### Acknowledgements
* Thanks to Clarence S. on the Udacity forum for help optimizing one of the queries.
