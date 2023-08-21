# ArchUI -- How to Use

ArchUI is the web application interface part of Maestro, implementing the search engine, database and ML pipeline and allowing the user to access these elements in a visually structured manner.

## Installation and Running

### Run Directly through Commandline

This software runs with Python version 3.10.

The requirements to run the UI can be installed through running `pip install -r requirements.txt` in the `flask` folder of the repository.

To run the UI, run `flask run` in the `flask` folder.

### Run through Docker

To run the UI through Docker, go down into the `flask` folder, open a commandline, and run `docker-compose up --build -d`.

## Usage

After starting the UI, you can access it in a browser at `http://localhost:5000`.

On the UI's home page, detailed information on usage is displayed.