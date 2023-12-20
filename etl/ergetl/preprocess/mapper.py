import pandas as pd


def standardize(gdf: geopandas.GeoDataFrame, geom_type: str, mapping_config: dict) -> geopandas.GeoDataFrame:
    """
    This function takes a geopandas dataframe and standardizes its columns based on a mapping configuration.
    It also adds a new column called 'geom_type' that contains the geometry type of each feature.

    Args:
        gdf (geopandas.GeoDataFrame): The input geopandas dataframe.
        geom_type (str): The name of the column that contains the geometry type.
        mapping_config (dict): A dictionary that maps the old column names to the new column names.

    Returns:
        geopandas.GeoDataFrame: The standardized geopandas dataframe.

    Raises:
        ValueError: If the input geopandas dataframe is empty.
        ValueError: If the input geometry type column does not exist in the input geopandas dataframe.
        ValueError: If the input mapping configuration is not a dictionary.
    """
    if gdf.empty:
        raise ValueError("Input geopandas dataframe is empty.")

    if geom_type not in gdf.columns:
        raise ValueError(f"Input geometry type column '{geom_type}' does not exist in the input geopandas dataframe.")

    if not isinstance(mapping_config, dict):
        raise ValueError("Input mapping configuration is not a dictionary.")

    standardized_columns = {value: key for (key, value) in mapping_config.items()}
    gdf.rename(columns=standardized_columns, inplace=True)

    for column in mapping_config.keys():
        if column not in gdf.columns:
            gdf[column] = None

    gdf[geom_type] = geom_type
    return gdf


def concat(gdf_list: List[geopandas.GeoDataFrame]) -> geopandas.GeoDataFrame:
    """
    This function concatenates a list of geopandas dataframes along the index.

    Args:
        gdf_list (List[geopandas.GeoDataFrame]): A list of geopandas dataframes to concatenate.

    Returns:
        geopandas.GeoDataFrame: The concatenated geopandas dataframe.

    Raises:
        ValueError: If the input list is empty.
    """
    if not gdf_list:
        raise ValueError("Input list is empty.")

    return geopandas.GeoDataFrame(pd.concat(gdf_list, ignore_index=True))
