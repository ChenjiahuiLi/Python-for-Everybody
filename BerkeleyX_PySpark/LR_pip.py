# Linear Regression Pipline
from pyspark.sql.functions import split
from pyspark.mllib.regression import LabeledPoint
import numpy as np    

def parse_points(DF):
    """Converts a DataFrame of comma separated unicode strings into a DataFrame of `LabeledPoints`.

    Args:
        df: DataFrame where each row is a comma separated unicode string. The first element in the string
            is the label and the remaining elements are the features.

    Returns:
        DataFrame: Each row is converted into a `LabeledPoint`, which consists of a label and
            features. To convert an RDD to a DataFrame, simply call toDF().
    """
    df2 = DF.select(split(DF.value, ',').alias('s'))
    rd1 = df2.rdd
    rd2 = rd1.map(lambda x: x[0])
    rd3 = rd2.map(lambda x: (x[0],x[1:]))   
    rd4 = rd3.map(hash_labeledpoint)
    df4 = rd4.toDF()
    return df4

### feature to Array
# takeSample(withReplacement, num, [seed]) 
# randomly selects num elements from the dataset with/without replacement, and has an
# optional seed parameter that one can set for reproducible results

data_values = (parsed_points_df
               .rdd
               .map(lambda lp: lp.features.toArray())
               .takeSample(False, 50, 47))
# Note that data_values is a list
data_values[0]

