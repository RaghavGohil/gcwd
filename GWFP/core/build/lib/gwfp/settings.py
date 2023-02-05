name = 'gwfp'
version = '0.0.2'
description = 'Get Connected Wi-fi data easily.'
author = 'RaghavGohil'
author_email = 'raghavgohil2004@gmail.com'
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
install_requires = ['regex>=2022.3.15','readme_renderer >= 21.0']
include_package_data = True
python_requires='>=3.0'
