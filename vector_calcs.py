# Import the required libraries from Hugging Face Transformers
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity


# There are a lot of BERT based models available on HuggingFace,
# and you have to pick one that is suitable for you.
BERT_Model = "bert-base-uncased"

# Initialise the BERT Transformer model
tokenizer = AutoTokenizer.from_pretrained(BERT_Model)
model = AutoModel.from_pretrained(BERT_Model)

# Function to compute the sentence embedding using BERT
def sent_embedding(sent):
    
    # Tokenize the sentence
    # This basically converts the sentence into a sequence of tokens
    # Each token is either a complete word or a sub-word
    tokens = tokenizer.encode_plus(sent, max_length=128, truncation=True,
                                    padding='max_length', return_tensors='pt')
    
    # Now feed the tokens into the model and get the embeddings as the output
    outputs = model(**tokens)

    # Create an empty list to store two different kinds of embeddings
    embedding_list = []

    # last_hidden_state contains the output at the last hidden layer of all the sentence tokens
    # pooler_output contains the embedding corresponding to only the [CLS] token, which in a way represents the whole sentence. 
    # This pooler_output is, however, different from the embeddings corresponding to the 1st token of last_hidden_state
    # Although both represent the CLS token, the pooler_output is after some more processing, 
    # and more suitable for use in sentence classification tasks.

    # This stores the embedding corresponding to the CLS token
    embedding_list.append(outputs.last_hidden_state[0][0].detach().numpy().reshape(1,-1))

    # This stores the embedding corresponding to the pooler_output
    embedding_list.append(outputs.pooler_output.detach().numpy())

    return embedding_list

def calculate_similarities(sent_embedding1, sent_embedding2):
    # Sentence similarity using CLS token embedding
    cls_embedding_similarity = cosine_similarity(sent_embedding1,sent_embedding2)

    # Sentence similarity using pooler_output 
    # pooler_embedding_similarity = cosine_similarity(sent_embedding(sent1)[1],sent_embedding(sent2)[1])

    return cls_embedding_similarity  # , pooler_embedding_similarity
