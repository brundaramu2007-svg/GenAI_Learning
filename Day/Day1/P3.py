# pip, virtual environment, .env file
# pip: it installs packages. Package manager
# virtual environment: A 'venv' is a directory that contains 
# 1. A copy of the python compiler
# 2. Its is own 'pip'
# 3. its own site-packages directory. Default target location
# where python installs third party libraries # site-packages meaning
# 4. Activation scripts that modify PATH

python  --version
python -m venv .venv # to create the virtual environment

# Activate
.venv\Scripts\activate.bat

# deactivate
deactivate

# pip installation (install dependencies/libraries)
pip install package_name #syntax
pip  install python-dotenv 

