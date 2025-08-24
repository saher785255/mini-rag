# mini-rag-app

this is a minimal implamation of the RAG model for questions and answers 

# Requirements 
 python 3.8 or newer vireions of pyhton 

# install python using miniconda

1) download miniconda form this link https://www.anaconda.com/download/success

2) after downloading creat a new envroment uing this command 
```bash

$ conda creat -n name of the envroment python=3.8
```

3) ativate the envroment using this command 
```bash
$ conda activate name of the envroment
```

# Optional Setup you command line interface for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```
# Install the required packages
```bash
$ pip install -r requirements.txt
```
# Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

# Run the api server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 3000
```
# POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)