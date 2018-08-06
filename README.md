# api_ebi_client

### Tutorial for Install and Run the Client

- Installation and setting up the application
- Install python 3.6
- Install and IDE such as (Pycharm) or a code editor (Atom, Sublime)
- Install pip and dependencies
- Install pip using this instructions: https://pip.pypa.io/en/stable/installing/
- Install urllib3 using this command: pip install urllib3 (https://pypi.org/project/urllib3/)

### How to run the application

1. There are two ways to run the client:
  - The first using a console application
  - Open a console or cmd
  - Run the command python:
  - python application_ebi_technical_test.py

2. The second option is using each functionality calling each function.
  - Open a console or cmd in the root folder (The client folder)
  - Open a python console using the command:
    - python
  - Import the file and library:
    - from client_api_ebi import *
  - Call a function:
    - To get total number of samples
      - Api_client.total_number_of_samples()
    - To get the name by an accession.
      - Api_client.get_name_by_accession() and pass as a param the accession
    - To get the accessions using a attribute:value filter
      - Apli_client.get_accessions_by_filter() and pass two params. The first is the attribute and the second is the value


### Files included

1. Source code with the files: client_api_ebi.py, application_ebi_technical_test.py
2. File with documentation to install and run the client: tutorial_to_run_and_install_client.pdf
3. Source code in a Jupyter Notebook: api_client_ebi.ipnyb
