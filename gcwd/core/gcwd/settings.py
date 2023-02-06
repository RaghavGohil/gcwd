name = 'gcwd'
version = '1.0.0'
description = 'Get connected wi-fi data easily.'
author = 'RaghavGohil'
author_email = 'raghavgohil2004@gmail.com'
project_url = 'https://github.com/RaghavGohil/GCWD'
classifiers = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft',
]
entry_points = '''
        [console_scripts]
        gcwd=gcwd.gcwd:main
    '''
exclude_packages = ('tests')
license = 'MIT LICENSE'
license_files = ('LICENSE.txt')
keywords = 'Get connected wi-fi data easily'
install_requires = ['regex>=2022.3.15','readme_renderer >= 21.0']
include_package_data = True
python_requires='>=3.0'
