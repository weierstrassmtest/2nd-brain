SELECT duped_field, COUNT(*) FROM "sample_db"."table" GROUP BY duped_field HAVING COUNT(*) > 1;
