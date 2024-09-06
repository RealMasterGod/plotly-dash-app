# Instructions to run locally
1. Clone this repo (You may delete the pycache folder after cloning).
   ```bash
   git clone https://github.com/RealMasterGod/plotly-dash-app.git
   cd plotly-dash-app-main
   ```
2. I did not create a virtual environment(venv) but you may if you want to.
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   for windows change the second command above to:
   ```bash
   venv\Scripts\activate
   ```
   OR Refer to this link to learn how to set up venv in python https://docs.python.org/3/library/venv.html
4. Install the dependencies (I am using python version 3+, If you are having trouble with command below you can manually install dependencies like: pip install dependencyname)
   ```bash
   pip install -r requirements.txt
   ```
5. There's an initialize_db.py file. Run this before you start the app.py file. This will initialize the tables in example db.
   ```bash
   python initialize_db.py
   ```
6. Run the app.py file
   ```bash
   python app.py
7. There should be no errors in console. Now go to http://127.0.0.1:8085 or whatever link it is showing in the console.
   
