clean:
	find . -iname '*.pyc' -delete

test-py2:
	python2 -m unittest discover -s test/ -p 'test_*.py'

test-py3:
	python3 -m unittest discover -s test/ -p 'test_*.py'
