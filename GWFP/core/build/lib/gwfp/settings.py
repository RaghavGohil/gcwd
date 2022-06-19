name = 'gwfp'
version = '0.0.1'
description = 'Get forgotten connected wifi passwords directly.'
author = 'RaghavGohil'
author_email = 'raghav15102004@gmail.com'
project_url = 'https://github.com/RaghavGohil/GWFP'
classifiers = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft',
]
entry_points = '''
        [console_scripts]
        gwfp=gwfp.gwfp:main
    '''
exclude_packages = ('tests')
license = 'MIT LICENSE'
license_files = ('LICENSE.txt')
keywords = 'Forgotten wifi password get'
install_requires = ['regex>=2022.3.15']
include_package_data = True
python_requires='>=3.0'
