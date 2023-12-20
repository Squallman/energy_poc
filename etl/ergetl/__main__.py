from ergetl.load.loader import write_gdf_to_postgres
from ergetl.utils.arg_parser import find_config_path
from ergetl.utils.config_reader import read_config_file
from ergetl.extract.extractor import extract_shp_to_gdf
from ergetl.preprocess.mapper import standardize, concat
from ergetl.preprocess.validator import validate_gdf

if __name__ == '__main__':
    # Find the path to the configuration file
    config_file_path = find_config_path()

    # Read the configuration file
    config_file = read_config_file(config_file_path)

    # Extract the data from the shapefiles
    datasets = {
        (entity_name, entity_config['geom_type']): extract_shp_to_gdf(entity_config['blob_name'])
        for entity_name, entity_config in config_file['input_entities'].items()
    }

    # Standardize the data
    data_list = [
        standardize(gdf, _[1], config_file['mapping_config'])
        for _, gdf in datasets.items()
    ]

    # Concatenate the data
    data = concat(data_list)

    # Validate the data
    validated_data = validate_gdf(data, config_file['validation_rules'])

    # Load the data into the database
    write_gdf_to_postgres(validated_data, config_file['table_name'])