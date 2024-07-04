# HRank: Developer Ranking and Co-Ranking Mechanism

## Overview

HRank is a mechanism for ranking developers and co-ranking them in the context of software engineering projects. This repository contains the implementation of the HRank algorithm and the necessary code to run and test it.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)


## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.10 or higher
- Git (for cloning the repository)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/BDA-IIITA/Investigating-Developer-Reviewer-Symphony.git
    cd Investigating-Developer-Reviewer-Symphony
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the codes, follow these steps:

1. **First run the "simple_ranking_FIRST.ipynb"**: This file will give you the ranking of developers across projects 

2. **Second run the "similarity_index.ipynb" file**: This code will give you the similarity comparision between the rankings using mongodb and the ranking using HRank.

3. **Third run the "RBO_AND_RANKING.ipynb" file**: This file will give you te=he similarity index and the Ranking of developers with their names.

4. **Fourth Run the "corank_first.ipynb" file**: This file will give you the coranking of developers across the projects.

5. **At last run the "corank_second.ipynb" file**: This file will give you the coranking of the developers in the top 5 projects.
    

