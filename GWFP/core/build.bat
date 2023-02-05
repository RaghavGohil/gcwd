pip uninstall gwfp
python setup.py sdist
python setup.py bdist_wheel
cd dist
pip install gwfp-0.0.2-py3-none-any.whl
cd ..