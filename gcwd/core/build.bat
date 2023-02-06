pip uninstall gcwd
python setup.py sdist
python setup.py bdist_wheel
cd dist
pip install gcwd-1.0.0-py3-none-any.whl
cd ..