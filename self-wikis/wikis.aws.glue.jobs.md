The python code below contains the most commonly-used imports when building an AWS Glue job from scratch.

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pandas as pd
```

Boilerplate Glue Code (this auto-generates when creating a job but unsure of what exactly it does / if it's necessary):

```
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
```

Example of some code which passes a SQL statement:

```
raw_roster = glueContext.create_dynamic_frame.from_catalog(database = "hr_database", table_name = "roster", transformation_ctx = "datasource0")

roster = raw_roster.toDF()
roster.createOrReplaceTempView("roster")

result = spark.sql("SELECT employee_id FROM roster")
test = DynamicFrame.fromDF(result,glueContext,"test")

datasink2 = glueContext.write_dynamic_frame.from_options(frame = test, connection_type = "s3", connection_options = {"path": "s3://hr/database/"}, format = "csv")

job.commit()
```
