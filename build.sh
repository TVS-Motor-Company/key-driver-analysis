rm requirements.txt
pipreqs .
rm -r build
rm -r key_driver_analysis.egg-info
rm -r dist
python setup.py sdist bdist_wheel
twine check dist/*
#twine upload --repository testpypi dist/*
#twine upload --repository pypi dist/*