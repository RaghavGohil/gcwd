name = 'gwfp'
version = '0.0.2'
description = 'This package is made to acqire all the forgotten wifi passwords and related data and store it in your desired place.\nYou can even store it in your pendrive.\nUsually, if the location and name of the file is not specifed, the output file containing the data will be stored in the downloads folder with the name \'out.txt\'.\nYou can go full-on hacker mode and clone the data from a target-pc in mere seconds.'
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
install_requires = ['regex>=2022.3.15']
include_package_data = True
python_requires='>=3.0'
