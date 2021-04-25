# Cryptocurrency-Analysis-Repo


## Overview

*This project is created as a final year project for University. It is 100% python and executes in the Jupyter Notebook. This is not commercial and please dont use it as a market indicator, it is not a financial influencing tool, it is merely meant to be used for research and analysis.*

## Installation Guide
1. The project folder needs to be downloaded. This can be done directly from this Github repository. A simple clone is sufficient. Move this folder to somewhere on your drive. Remember the location as you will need to navigate to it at a later time.
2. Anaconda needs to be installed into any machine that wishes to run the code. The full installation guide for conda can be found at [Anaconda](https://docs.anaconda.com/anaconda/install/)
3. Creating and activating the environment file - once anaconda is installed on your machine, you then need to create the environment from the `.yml` file (which is located inside the project folder). To do this:
	1. Open conda prompt or command prompt from windows explorer.
	2. Navigate to the project folder using `cd`.
	3. run `conda env create -f environment.yml` . This will download libraries and should take a few minutes. After this, a new environment will be created named **pycrypto**.
4. To run the jupyter notebook follow these steps:
    1. run `conda activate pycrypto`. The pycrypto name should be seen in brackets on the left hand side of the command prompt, this indicates that the environment is active.
    2. run `jupyter notebook`. This will open up a web broswer tab with a directory of the project folder.
5. Open the `.ipynb` file and follow the instructions.