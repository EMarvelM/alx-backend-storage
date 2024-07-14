-- lists all bands with Glam rock as their main style, ranked by their longevity
SELECT A.band_name, COALESCE(A.split - A.formed, 2020 - A.formed) AS lifespan
FROM 
(
    SELECT band_name, formed, split FROM `metal_bands` WHERE style LIKE '%Glam rock%'
) A
ORDER BY lifespan DESC;
