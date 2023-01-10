'''
Name: Code.
Author: Monarchdos
Date: 2023-01-05
'''
import io
import sys

import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(name="nonebot_plugin_cloudsignx",
                version="2.0.0",
                author="Monarchdos",
                author_email="admin@ayfre.com",
                keywords=("pip", "nonebot2", "nonebot", "nonebot_plugin"),
                description="""Cloud sign in""",
                long_description=long_description,
                long_description_content_type="text/markdown",
                url="https://github.com/Monarchdos/nonebot_plugin_cloudsign",
                packages=setuptools.find_packages(),
                include_package_data=True,
                platforms="any",
                install_requires=[
                    'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
                    'nonebot2>=2.0.0-beta.1,<3.0.0', 'requests'
                ])
