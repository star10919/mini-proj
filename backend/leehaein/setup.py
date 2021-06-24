from setuptools import setup, find_packages


setup_requires = [
    ]




install_requires = [
    'django==3.2.4',      #common, crime, gasstaion과 동급인 __init__에 있는 버전으로 적어주기
    'html5lib==1.1',
    'wheel==0.36.2',    # 인터넷에'pip install wheel' 검색해서 버전에 맞게 넣어주기
    ]




dependency_links = [
    'git+https://github.com/django/django.git@stable/1.6.x#egg=Django-1.6b4',
    ]




setup(
    name='Root App',
    version='0.1',
    description='Root App',
    author='root',
    author_email='root@root.com',
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    scripts=['manage.py'],
    entry_points={
        'console_scripts': [
            'publish = leehaein.common.script:main',
            'scan = leehaein.crime.script:main',
            'update = leehaein.gas_station.script:main',
            ],
        },
    )