# Financial-Named-Entity-Recognition-How-Far-Can-LLM-Go
The artifacts for the paper "Financial Named Entity Recognition: How Far Can LLM Go?"
This Readme will introduce by each file and directories. 

### BERT_on_FiNER.ipynb

This code contains training code for BERT and RoBERTa models.

### results

This directory contains the result for each LLMs and transformer based model, each file is named by their related model name and prompting design.
The results are formatted in JSON, each containing the following key, value pair.

1. sentence: the sentence in the test set.
2. tags: the labelled entities in each sentence.
3. response: the response of LLMs for each NER task. We feed one sentence to the LLM at one time, each response is corresponding to one sentence in the test set. 
4. answer_tags: the tags of each recognized entities in each sentence by the model.
