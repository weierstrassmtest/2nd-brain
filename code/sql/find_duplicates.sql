SELECT duped_field, COUNT(*) FROM "sample"."db" GROUP BY duped_field HAVING COUNT(*) > 1;
