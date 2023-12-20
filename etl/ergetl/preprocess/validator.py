import pandas as pd


def validate_gdf(gdf, rules):
    """
    Cleans and validates a GeoDataFrame based on a set of rules.

    Parameters:
    gdf (GeoDataFrame): The GeoDataFrame to be validated.
    rules (list of dicts): A list of rules for validation. Each rule is a dictionary.

    Returns:
    GeoDataFrame: The validated and cleaned GeoDataFrame.
    """
    for rule in rules:
        action = rule.get('action')
        if action == 'drop_null':
            gdf = gdf.dropna(subset=[rule['column_name']])
        elif action == 'drop_duplicates':
            gdf = gdf.drop_duplicates()
        elif action == 'convert_to_integer':
            gdf[rule['column_name']] = pd.to_numeric(gdf[rule['column_name']], downcast='integer', errors='coerce')
        else:
            print(f'Unknown action: {action}')
    return gdf
