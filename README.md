# Financial-Named-Entity-Recognition-How-Far-Can-LLM-Go
The artifacts for the paper "[Financial Named Entity Recognition: How Far Can LLM Go?](http://arxiv.org/abs/2501.02237)", more information can be found in the [paper](http://arxiv.org/abs/2501.02237).
This Readme will introduce by each file and directories. 

### Dataset

We use the dataset FiNER-ORD from the paper "[FiNER-ORD: Financial Named Entity Recognition Open Research Dataset](https://arxiv.org/abs/2302.11157)", their dataset is available both on [huggingface](https://huggingface.co/datasets/gtfintechlab/finer-ord) and [github](https://github.com/gtfintechlab/FiNER-ORD?tab=readme-ov-file), please go to these provided links for more information.

### Prompt Design


### BERT_on_FiNER.ipynb

This code contains training code for BERT and RoBERTa models, modified from the [huggingface token classificaion tutorial](https://huggingface.co/learn/nlp-course/chapter7/2).

### Results

This directory contains the result for each LLMs and transformer based model, each file is named by their related model name and prompting design. Under each LLM directory are three JSON file:
1. `CoT_response.json` is the LLM response using chain-of-thought prompt
2. `inContext_response.json` is the LLM response using in-context learning prompt
3. `direct_response.json` is the LLM response using direct prompting

The results are formatted in JSON, each containing the following key, value pair.

1. sentence: the sentence in the test set.
2. tags: the labelled entities in each sentence.
3. response: the response of LLMs for each NER task. We feed one sentence to the LLM at one time, each response is corresponding to one sentence in the test set. 
4. answer_tags: the tags of each recognized entities in each sentence by the model. We retrieved the named entity recognized in the LLM's responses, and labelled each word in the sentence through string matching.

### Evaluation Metrics

### Citation
If you find this repository useful, please cite our work.
