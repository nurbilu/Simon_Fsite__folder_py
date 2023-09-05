# Create Virtual Environment :
   pip install virtualenv
   python -m virtualenv venv
   venv\scripts\activate
   deactivate
# create Requirements:
   pip freeze > Requirements.txt

# Install : 
   pip install -r Requirements.txt

# Run : 
  py file_name.py 
  flask run (if file_name == app)