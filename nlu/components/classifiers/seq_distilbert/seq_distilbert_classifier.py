from sparknlp.annotator import *
class SeqDilstilBertClassifier:
    @staticmethod
    def get_default_model():
        return DistilBertForSequenceClassification.pretrained() \
            .setInputCols(["token", "sentence"]) \
            .setOutputCol("category") \
            .setCaseSensitive(True)

    @staticmethod
    def get_pretrained_model(name, language, bucket=None):
        DistilBertForSequenceClassification.name = "DistilBertForSequenceClassification"
        return DistilBertForSequenceClassification.pretrained(name, language, bucket) \
            .setInputCols(["token", "sentence"]) \
            .setOutputCol("category") \
            .setCaseSensitive(True)





