In this take-home assignment, I was given a list of questions and asked to find the most appropriate article to answer each question from the [Simple Wikipedia Dataset](https://huggingface.co/datasets/wikimedia/wikipedia/viewer/20231101.simple/train).

My approach:
1. Generate embeddings for each article and label them with their corresponding titles
2. Set up a vector database, [Milvus](https://milvus.io/), and store the embeddings into the database
3. For each question, generate embeddings for the question and look for the most similar entry in the database
