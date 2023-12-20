SELECT
    fid,
    erg_id,
    significance,
    yield,
    extraction_rate_well,
    extraction_rate_works,
    rock_type,
    -- Example of a calculated field
    CASE
        WHEN shape_area IS NOT NULL AND shape_length IS NOT NULL THEN shape_area / shape_length
        ELSE NULL
    END AS area_length_ratio
FROM {{ source('gis', 'combined_ergw1000_data')}}