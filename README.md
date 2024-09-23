[![CI](https://github.com/nogibjj/Rishika_Randev_Mini_4/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Rishika_Randev_Mini_4/actions/workflows/hello.yml)

# Rishika Randev's Mini Project 4 (GH Actions matrix) for IDS706

This repository demonstrates a GitHub Actions workflow which tests a basic Python script across multiple Python versions and Ubuntu versions. In order to accomplish this, a workflow yml file is set up with a GH Actions matrix build.

* A Makefile, which runs required installations, and then formats using Black, lints using Pylint, and tests the code using pytest.

* A requirements.txt file, which lists out some basic DevOps and Data Science packages pinned to specific versions for installation.

* A devcontainer folder.

* Github Actions workflows directory and yml file for CI/CD integration and a matrix build.

* A basic Python script main.py for creating a data visualization and generating descriptive statistics of a seaborn dataset on healthcare spending data across multiple countries and years.

* A testing script which tests the functions of the Python script main.py.

  
## Step 1: Set Up
Add seaborn and any other required packages along with the compatible versions to the requirements.txt.
<img width="246" alt="Screenshot 2024-09-23 at 6 23 05 PM" src="https://github.com/user-attachments/assets/456135eb-d472-462c-9fb0-a9a9f899b221">

Create Makefile and devcontainer folder with Dockerfile and json for environmental setup.


## Step 2: YML File for GH Actions Matrix
Update your GH Actions workflow yml file to build the code using different Python versions with a matrix build.
<img width="559" alt="Screenshot 2024-09-23 at 6 23 33 PM" src="https://github.com/user-attachments/assets/9ef21ad0-3b9a-40d9-bced-979cb56e41a9">


## Step 3: Create Python Scripts
Create a main.py file with a load_data() function, which loads a seaborn dataset called "healthexp" with the following columns: 
* Country (either the US, Japan, Canada, Germany, France, or Great Britain)
* Year (data collected between 1970-2020)
* Healthcare spending per person in USD
* Life expectancy

The main.py file also contains a generate_summary_stats() function to describe the dataset, and a generate_line_graph() function to produce a line graph of healthcare spending specifically in the US between 1970-2020. 

A separate test_main.py file is used to call the generate_summary_stats() and generate_line_graph() functions.

## Step 4: Validate the CI/CD output
Upon pushing to the repository, the GH Actions workflow is run using different Python versions, and all the steps of the Makefile successfully pass for each version.
<img width="1448" alt="Screenshot 2024-09-23 at 6 18 39 PM" src="https://github.com/user-attachments/assets/f7b29d84-0dde-4167-a5db-93368914a0df">
