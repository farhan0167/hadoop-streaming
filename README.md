# N-gram Extraction with Hadoop Streaming

In this repository, I demonstrate how to extract n-grams from a large text file using Hadoop Streaming. Hadoop is an open-source framework for distributed storage and processing of big data, while Hadoop Streaming is a utility that allows us to use any executable (in my case, I'm using Python) as a mapper or reducer in a MapReduce job. N-grams are contiguous sequences of n items from a given text, and they are commonly used in natural language processing for tasks such as language modeling and text classification. By leveraging the power of Hadoop Streaming, we can efficiently extract n-grams from very large text files, making it a valuable tool for text analysis and processing at scale. In this repo, I provide step-by-step instructions on how to run bi-gram extraction using Hadoop Streaming.

The key idea behind this repo is using MapReduce to extract all the bi-grams. The paradigm is to divide the input data into smaller chunks, process each chunk in parallel across a distributed set of nodes, and then combine the results into a final output.

**Note**: This repo is a work in progress