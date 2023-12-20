import os
from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import create_engine


# Database credentials and connection
# TODO Should be implemented connection builder to read credentials from environment variables
# Should be replaced with your own credentials
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
dbname = os.environ['POSTGRES_DB']
url = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
engine = create_engine(url)


def write_gdf_to_postgres(gdf, table_name):
    """
    Writes a GeoDataFrame to a PostgreSQL database.

    Parameters:
    gdf (GeoDataFrame): The GeoDataFrame to be written to the database.
    table_name (str): The name of the table to write the data to.
    engine (sqlalchemy.engine.Engine): The SQLAlchemy engine connected to the database.
    """
    # Convert geometry to WKTElement
    gdf['geom'] = gdf['geometry'].apply(lambda x: WKTElement(x.wkt, srid=4326))
    gdf.drop('geometry', axis=1, inplace=True)

    # Write to PostgreSQL
    gdf.to_sql(table_name, engine, if_exists='replace', index=False, dtype={'geom': Geometry('GEOMETRY', srid=4326)})
