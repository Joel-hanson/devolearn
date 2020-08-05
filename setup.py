import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devolearn",
    version="0.1.2",
    author="Mayukh Deb, Ujjwal Singh, Bradley Alicea", #To be decided, also there can be name of "DevoWorm | OpenWorm Foundation"
    author_email="mayukhmainak2000@gmail.com, ujjwal18113@iiitd.ac.in, balicea@openworm.org", #Subject to change, we can also use Devolearn official Email address.
    description="Accelerate data driven research on embryos with Pre-Trained deep learning models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DevoLearn/devolearn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
        "cycler==0.10.0",
        "efficientnet-pytorch==0.6.3",
        "future==0.18.2",
        "imutils==0.5.3",
        "joblib==0.16.0",
        "kiwisolver==1.2.0",
        "matplotlib==3.3.0",
        "munch==2.5.0",
        "numpy==1.19.1",
        "opencv-python==4.3.0.36",
        "pandas==1.1.0",
        "Pillow==7.2.0",
        "pretrainedmodels==0.7.4",
        "pyparsing==2.4.7",
        "python-dateutil==2.8.1",
        "pytz==2020.1",
        "scikit-learn==0.23.2",
        "scipy==1.5.2",
        "segmentation-models-pytorch==0.1.0",
        "six==1.15.0",
        "sklearn==0.0",
        "threadpoolctl==2.1.0",
        "torch==1.6.0",
        "torchvision==0.7.0",
        "tqdm==4.48.2"
      ],
    python_requires='>=3.6',   
    include_package_data=True   
)
