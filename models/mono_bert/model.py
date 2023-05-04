from transformers import *


class MonoBERT(BertPreTrainedModel):
    def __init__(self, config):
        config.num_labels = 1
        super(MonoBERT, self).__init__(config)
        self.bert = BertForSequenceClassification(config)
        self.init_weights()

    def forward(self, input_ids, attention_mask, token_type_ids):
        outputs = self.bert(input_ids, attention_mask, token_type_ids)
        logits = outputs[0]
        return logits