CREATE EXTENSION IF NOT EXISTS postgis; -- Enable PostGIS extension

CREATE TABLE combined_ergw1000_data (
    id SERIAL PRIMARY KEY, -- A primary key for the table
    fid INT, -- Feature ID
    erg_id INT, -- Groundwater yield dataset ID
    significance VARCHAR(255), -- Significance or importance
    yield VARCHAR(255), -- Yield or capacity
    extraction_rate_well FLOAT, -- Potential extraction rate for individual wells
    extraction_rate_works FLOAT, -- Potential extraction rate for waterworks
    rock_type VARCHAR(255), -- Type of groundwater-bearing rock
    shape_area FLOAT, -- Area for polygon features (if applicable)
    shape_length FLOAT, -- Length for line features (if applicable)
    geom_type VARCHAR(50), -- Type of geometry ('Polygon', 'LineString', etc.)
    geom GEOMETRY, -- Geometry column for spatial data
    CONSTRAINT enforce_geotype_geom CHECK (
        (geom_type = 'Polygon' AND GeometryType(geom) = 'POLYGON') OR
        (geom_type = 'LineString' AND GeometryType(geom) = 'LINESTRING')
    )
);

-- Add a spatial index for better performance on spatial queries
CREATE INDEX combined_ergw1000_data_geom_idx ON combined_ergw1000_data USING GIST (geom);
