import os
import geopandas as gpd
from azure.storage.blob import BlobServiceClient
import tempfile

account_url = os.environ['ACCOUNT_URL']
sas_token = os.environ['SAS_TOKEN']
container_name = os.environ['CONTAINER_NAME']


def extract_shp_to_gdf(blob_name):
    """
    Extracts data from a shapefile stored in Azure Blob Storage and returns it as a GeoPandas DataFrame.

    Parameters:
    blob_name (str): Name of the shapefile blob.

    Returns:
    GeoDataFrame: A GeoPandas DataFrame containing the data from the shapefile.
    """
    try:
        # Initialize Blob Service Client using SAS Token
        blob_service_client = BlobServiceClient(account_url=account_url, credential=sas_token)

        # Create a temporary directory to store shapefile components
        with tempfile.TemporaryDirectory() as temp_dir:
            # File extensions of a typical shapefile
            extensions = ['.shp', '.shx', '.dbf', '.prj', '.cpg', '.sbn', '.sbx', '.shp.xml']

            # Download each component of the shapefile
            for ext in extensions:
                file_name = blob_name.replace('.shp', ext)
                blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
                blob_data = blob_client.download_blob()
                file_path = os.path.join(temp_dir, file_name)

                with open(file_path, 'wb') as file:
                    file.write(blob_data.readall())

            # Read the shapefile using GeoPandas
            shp_path = os.path.join(temp_dir, blob_name)
            gdf = gpd.read_file(shp_path)
            return gdf

    except Exception as e:
        raise Exception(f"Error accessing blob storage: {str(e)}")
