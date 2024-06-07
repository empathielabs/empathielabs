from setuptools import setup, find_packages

setup(
    name="empathielabs",
    version="0.0.0",
    description="empathielabs",
    author="empathielabs",
    maintainer="empathielabs",
    url="www.empathielabs.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    install_requires=[
        "accelerate>=0.20.0",
        "datasets>=2.8.0",
        "einops>=0.7.0",
        "ipywidgets>=8.0.3",
        "jsonlines>=3.1.0",
        "jupyter>=1.0.0",
        "matplotlib>=2.2.0",
        "numpy>=1.21.0",
        "omegaconf>=2.0.0",
        "Pillow>=9.0.1",
        "pip-chill==1.0.3",
        "python-dotenv>=0.21.0",
        "torchvision>=0.11.1",
        "transformers>=4.30.0",
        "tqdm>=4.60.0",
        "vllm>=0.4.3"
    ],
    packages=find_packages(include=['empathielabs', 'empathielabs.*']),
    entry_points={
        "console_scripts": [
            # add your scripts here, for example:
            # "my-script = module_name:main"
            "run-test = empathielabs.test:test",
        ]
    },
    python_requires=">=3.8",
)