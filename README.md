# testForJenkins

python -m venv venv
. venv/bin/activate
python -m unittest discover -s . -p 'test\_\*.py'
