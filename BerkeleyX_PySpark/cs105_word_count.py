#cs105 word count
# Create DataFrame with sqlContext
# One
## 1
wordsDF = sqlContext.createDataFrame([('cat',),('dog',),('rat',),('rat,'),('rat',)],['word']) # a list of tuples
wordsDF.show()
print type(wordsDF)
wordsDF.printSchema()
## 2
wordCountsDF = wordsDF.groupBy(wordsDF['word']).count() # do not use select
     # automatically create 2 columns named 'word' and 'count' 
print type(wordCountsDF)
wordCountsDF.printSchema()
wordCountsDF.show()
## 3
     # Count average using GroupedData obj: groupBy, avg, flatMap, first
averageCount = wordCountsDF.groupBy().avg('count').first()
print averageCount
# Row(avg(count)=1.6666667)
averageCount = wordCountsDF.groupBy().avg('count').map(lambda x:x).first()
print averageCount
# Row(avg(count)=1.6666667)
averageCount = wordCountsDF.groupBy().avg('count').flatMap(lambda x:x).first()
print averageCount
# 1.6666667
	# Difference between map and flatMap
	# http://stackoverflow.com/questions/22350722/can-someone-explain-to-me-the-difference-between-map-and-flatmap-and-what-is-a-g
round(averageCount,2)
## 3.5: combine 2 and 3
averageCount = wordsDF.groupBy('word').count().groupBy().avg('count').flatMap(lambda x:x).first() #####################
print averageCount
# 1.6666667
def wordCount(wordListDF):
    """Creates a DataFrame with word counts.

    Args:
        wordListDF (DataFrame of str): A DataFrame consisting of one string column called 'word'.

    Returns:
        DataFrame of (str, int): A DataFrame containing 'word' and 'count' columns.
    """
    return wordListDF.groupBy('word').count()

## 4
	# remove capitalizations, punctuation, spaces
from pyspark.sql.functions import regexp_replace, lower, trim
def removePunctuation(column):
    """Removes punctuation, changes to lower case, and strips leading and trailing spaces.

    Note:
        Only spaces, letters, and numbers should be retained.  Other characters should should be
        eliminated (e.g. it's becomes its).  Leading and trailing spaces should be removed after
        punctuation is removed.

    Args:
        column (Column): A Column containing a sentence.

    Returns:
        Column: A Column named 'sentence' with clean-up operations applied.
    """
    sentence = lower(column)
    sentence = regexp_replace(sentence, 'p\{Punct}', '')
    sentence = trim(sentence)
    return sentence

sentenceDF = sqlContext.createDataFrame([('Hi, you!',),(' No under_score!',),(' *      Remove punctuation then spaces  * ',)], 
										['sentence'])
sentenceDF.show(truncate=False)
	# REMEMBER: add col('sentence') when calling removePunctuation
sentenceDF.select(removePunctuation(col('sentence'))).show(truncate=False)	

## 5
	# split and explode
fileName = "dbfs:/databricks-datasets/cs100/lab1/data-001/shakespeare.txt"
shakespeareDF = sqlContext.read.text(fileName).select(removePunctuation(col('value')))
shakespeareDF = shakespeareDF.select(col("trim(lower(regexp_replace(value,\p{Punct},)))").alias("sentence"))
shakespeareDF.show(15, truncate=False)

from pyspark.sql.functions import split, explode, lit, length
shakeWordsDF = shakespeareDF.select(explode(split(lit(shakespeareDF.sentence)," ")).alias('word'))
shakeWordsDF = shakeWordsDF.select(shakeWordsDF.word, length(shakeWordsDF.word).alias('len'))
shakeWordsDF = shakeWordsDF.filter(shakeWordsDF.len > 0)
shakeWordsDF = shakeWordsDF.select('word')
shakeWordsDF.show(15)
shakeWordsDFCount = shakeWordsDF.count()

## 6 
	# wordCount(), sort
from pyspark.sql.functions import desc
topWordsAndCountsDF = wordCount(shakeWordsDF)
topWordsAndCountsDF = topWordAndCountsDF.sort('count',ascending=False)
topWordsAndCountsDF.show() 



from pyspark.sql.functions import concat, lit
pluralDF = wordsDF.select(concat(wordsDF['word'],lit('s')).alias('word'))
pluralDF.show()

from pyspark.sql.functions import length
pluralLengthsDF = pluralDF.select(length(pluralDF['word']).alias('len'))
pluralLengthsDF.show()

from spark_notebook_helpers import printDataFrames
printDataFrames(True) # return all the DataFrames in the notebooks and their corresponding column names.
uniqueWordsCount = wordCountsDF.select()

# 3 ways to select a column
df.select(df.colname)
df.select(df['colname'])
df.select('colname')