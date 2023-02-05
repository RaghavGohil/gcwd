from importlib.metadata import entry_points
from gwfp import settings
from setuptools import setup,find_packages

ld_type = 'text/x-rst'

with open('README.rst') as rm:
    ld = rm.read()

setup(
    name = settings.name,
    version = settings.version,
    description = settings.description,
    long_description = ld,
    long_description_content_type = ld_type,
    author = settings.author,
    author_email = settings.author_email,
    packages = find_packages(exclude=settings.exclude_packages),
    url = settings.project_url,
    entry_points = settings.entry_points,
    classifiers = settings.classifiers,
    license = settings.license,
    license_files = settings.license_files,
    keywords = settings.keywords,
    install_requires = settings.install_requires,
    python_requires = settings.python_requires,
    include_package_data = settings.include_package_data,
)
