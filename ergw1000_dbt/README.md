# ERGW1000 Data
## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.6 or later)
- pip (Python package installer)
- A PostgreSQL database accessible to your environment

## Installation
### Install dbt-core and dbt-postgres

1. Create a Virtual Environment (optional):
    ```zsh
    python -m venv dbt-env
    source dbt-env/bin/activate
    ```
1. Install dbt-core and dbt-postgres:
    ```zsh
   pip install dbt-core dbt-postgres
   ```

## Data Models

### `combined_ergw1000_data`
This source table contains combined groundwater data from various ERGW1000 sources. It includes fields such as feature ID, dataset ID, significance, yield, and spatial data.

### `transformed_combined_ergw1000_data` View
The `transformed_combined_ergw1000_data` model is a dbt-generated view that transforms data from the `combined_ergw1000_data` source. It includes calculations like area to length ratio and any other transformations specified in the model SQL.

## Running the Project
To run the dbt project and generate the transformed models:
1. Set up your `profiles.yml` to connect to your PostgreSQL database. This file should be located at `~/.dbt/profiles.yml`.
1. Run dbt:
   ```zsh
   dbt run
   ```

## Testing the Project
To ensure data integrity and correctness, run the predefined tests in the project:
```zsh
dbt test
```