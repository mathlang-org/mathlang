help:
	# release: 发布
	# test: 单元测试
	# clean: 清除缓存

release:
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*

test:
	pytest -q tests.py

clean:
	rm -rf build dist
	rm -rf __pycache__
	rm -rf mathlang/__pycache__
	rm -rf mathlang.egg-info
