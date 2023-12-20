CREATE TABLE ergw1000_uferfiltrat_v1_line (
    FID SERIAL PRIMARY KEY,
    erg_id INT,
    bedeutung VARCHAR(255),
    ergiebigke VARCHAR(255),
    entn_bru FLOAT,
    entn_werk FLOAT,
    gestein VARCHAR(255),
    Shape_STLe FLOAT,
    geom GEOMETRY(LineString, 3034) -- Assuming data is in EPSG 3034 coordinate system
);
