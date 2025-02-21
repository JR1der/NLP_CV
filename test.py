from transformers import BertTokenizer, BertModel
from scipy.spatial.distance import cosine

# Step 1: Load the pre-trained BERT model and tokenizer
model_name = 'bert-large-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)


