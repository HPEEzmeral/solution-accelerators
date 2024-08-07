# Chatbot

In this tutorial, you build a Chatbot that uses a RAG (Retrieval Augmented Generation) system to
answer user queries leveraging both an SQL and a Vector database. 

![llm-high-level](images/conceptual-flow.png)

To make this happen, you:

* Deploy an embeddings model, using KServe.
* Deploy an SQL Coder LLM that can translate user queries to SQL statements.
* Deploy an LLM to respond to inquiries, leveraging the context extracted from the two databases, in
  a natural language format.
* Deploy an agent that decides whether to use the Vector or the SQL database to answer a specific
  user query.

1. [What You'll Need](#what-youll-need)
1. [Procedure](#procedure)
1. [Troubleshooting](#troubleshooting)
1. [Clean Up](#clean-up)
1. [References](#references)

## What You'll Need

For this tutorial, ensure you have:

- Access to an HPE Ezmeral Unified Analytics (EzUA) cluster.
- An API Token to pull images from NVIDIA NGC catalog.
- A Hugging Face token to pull models from Hugging Face Hub.

## Procedure

To complete the tutorial follow the steps below:

1. Login to your EzUA cluster, using your credentials.
1. Create a new Notebook server using the
   `marketplace.us1.greenlake-hpe.com/ezmeral/ezkf/jupyter:v1.3.0-e658264` image.
   Request at least `4Gi` of memory for the Notebook server, `4` CPUs and `1` GPU device.
1. Connect to the Notebook server, launch a new terminal window, and clone the repository locally.
   See the troubleshooting section if this step fails.
1. Navigate to the tutorial's directory (`chatbot`)
1. Launch the setup Notebook to create the necessary Kubernetes secrets.
1. Use the EzUA "Import Framework" wizard to upload the `chatbot.tgz` tarball located in the
   `deployment` directory. This creates a user interface for your application and deploys all the
   necessary components. Complete the steps and wait for a new endpoint to become ready.
1. Connect to the endpoint and submit your questions.

## Troubleshooting

If you're operating behind a proxy, you'll need to configure several environment variables to
successfully clone the `ezua-tutorials` repository to your local machine.

Launch a terminal window and execute the following commands:

- `export http_proxy=<your http proxy URL>`
- `export https_proxy=<your https proxy URL>`

## Conceptual Architecture

![flow-chart](images/flowchart.png)

**Path A**: Question related to structured data

A1. Database Search:

- The agent recognizes that the user's question pertains to structured data.
- The agent sends a database search request to the SQL Coder Service on the vLLM server.

A2. SQL Query:

- The SQL Coder Service generates an SQL query and executes it on the private SQL database.

A3. SQL Response:

- The SQL database returns the query result to the SQL Coder Service.

A4. Response:

- The SQL Coder Service sends the processed response back to the agent.

**Path B**: Question related to unstructured data

B1. Question:

- The agent recognizes that the user's question pertains to unstructured data.
- The agent sends the question to the RAG Chain.

B2. Question:

- The RAG Chain sends the question to the Embeddings Inference Service.

B3. Embedded Query:

- The Embeddings Inference Service converts the question into an embedded query.

B4. Embedded Query:

- The embedded query is sent to the Vector Store to find relevant document embeddings.

B5. Context:

- The relevant context information is retrieved from the Vector Store and sent back to the RAG Chain.

B6. Context & Question:

- The RAG Chain combines the context with the original question and sends it to the LLM Inference Service.

B7. Response:

- The LLM Inference Service processes the combined context and question to generate a response.

B8. Response:

- The response is sent back to the agent.

## Clean Up

To clean up the resources used during this experiment, follow the steps below:

1. Go to the EzUA "Import Framework" dashboard and delete the application.
1. Remove the Kubernetes secrets you created by running the setup Notebook.

## References

1. [A High-Level Introduction To Word Embeddings](https://predictivehacks.com/a-high-level-introduction-to-word-embeddings/)
1. [Nearest Neighbor Indexes for Similarity Search](https://www.pinecone.io/learn/series/faiss/vector-indexes/)
1. [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
1. [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)
