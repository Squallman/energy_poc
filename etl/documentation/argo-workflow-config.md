# Configuration Guide for ERGW1000 Data Processing

## Introduction

This guide provides detailed instructions on how to set up and utilize a configuration file for processing ERGW1000 data. The configuration file is in JSON format and contains various parameters to control the data transformation process.

## Configuration File Structure
The configuration file consists of several key sections:

- `table_name`: Specifies the name of the output table.
- `mapping_config`: Defines the mapping of source data columns to the desired output columns.
- `input_entities`: Lists the input data sources along with their respective geometries.
- `validation_rules`: Outlines various data validation and transformation rules.
- 
Below is a detailed explanation of each section along with example configurations.

### 1. Table Name

```json
"table_name": "combined_ergw1000_data"
```
- `table_name` is the name of the table where the transformed data will be stored.

### 2. Mapping Configuration
```json
"mapping_config": {
  "fid": "FID",
  "erg_id": "erg_id",
  "significance": "bedeutung",
  "yield": "ergiebigke",
  "extraction_rate_well": "entn_bru",
  "extraction_rate_works": "entn_werk",
  "rock_type": "gestein",
  "shape_area": "Shape_STAr",
  "shape_length": "Shape_STLe"
}
```
- `mapping_config` contains key-value pairs where the key is the name of the column in the destination table, and the value is the corresponding column name in the source data.

### 3. Input Entities
```json
"input_entities": {
  "bergbaugebiete": {
    "blob_name": "ergw1000_bergbaugebiete__v1_poly.shp",
    "geom_type": "Polygon"
  },
  // ... other entities
}
```
- `input_entities` lists the source data files (e.g., shapefiles) and their geometry types. Each entity is a table_name as a key in the JSON object with details about the file name (blob_name) and geometry type (geom_type).

### 4. Validation Rules
```json
"validation_rules": [
  {
    "action": "drop_null",
    "column_name": "erg_id"
  },
  {
    "action": "drop_duplicates"
  },
  {
    "action": "convert_to_integer",
    "column_name": "erg_id"
  }
]
```
- `validation_rules` specifies a set of operations to clean or validate the data. It includes actions like dropping null values (drop_null), removing duplicate rows (drop_duplicates), and converting column types (convert_to_integer).

## Available Validation Rules

### 1. `drop_null`
This action removes rows where the specified column's value is NULL.
- format:
```json
{
  "action": "drop_null",
  "column_name": "column_to_check"
}
```
- exmample:
```json
{
  "action": "drop_null",
  "column_name": "erg_id"
}
```
This rule will drop all rows where the erg_id column has NULL values.

### 2. `drop_duplicates`
This action removes duplicate rows from the dataset.
- format:
```json
{
  "action": "drop_duplicates"
}
```
- example:
```json
{
  "action": "drop_duplicates"
}
```
This rule will remove all duplicate rows in the dataset, considering all columns.

### 3. `convert_to_integer`
This action converts the data type of specified column to an integer.
- format:
```json
{
  "action": "convert_to_integer",
  "column_name": "column_to_convert"
}
```
- example:
```json
{
  "action": "convert_to_integer",
  "column_name": "erg_id"
}
```
This rule will convert the data type of the erg_id column to an integer.

## Usage
The configuration file serves as a key component in guiding the data processing operations conducted by the ergetl Python module. It can be utilized in two primary ways:

### As an Argument in the `ergetl` Python Module
When running the ergetl module, the configuration file can be passed as an argument. This allows the module to dynamically adapt its processing logic based on the settings defined in the file. The module will read the configuration, applying the specified mappings, input entities, and validation rules during the data processing workflow.
```zsh
python -m ergetl config.json
```

### As a Parameter in Argo Workflow Submission
In scenarios where the data processing is orchestrated using Argo Workflows within a Kubernetes environment, the configuration file can be incorporated as a parameter in the Argo workflow template. This integration facilitates the passing of configuration details to the ergetl module as it executes as part of a broader, automated workflow.
```zsh
argo submit argo.yaml -p jsonContent=$(base64 -i config.json) -f params.yaml -n argo
```