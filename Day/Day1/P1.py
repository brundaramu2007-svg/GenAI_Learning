#variables
temperature = 0.8 #float
max_tokens = 2006 #int
is_streaming = False #boolean
content_box = None #none

#Type Hints
model_name: str = "gemini-2.0-flash"
temperature: float = 0.8 #float
max_tokens: int = 2006 #int
is_streaming: bool = False #boolean
content_box: str|None = None #none
print(type(model_name))
#strings: immutable | string formatting
#old version 
name = "LLM"
score = 97.3
print("Hello %s"%name)
print("SCore %.1f"%score)

# f-strings (Py 3.6+)
print(f"Hello{name}")
print(f"score: {score:.1f}")


# Expressions inside f-strings
word_limit = 200
print(f"{'over' if word_limit > 150 else 'under'}limit")
data = {"topic":"RAG"}
print(f"Topic: {data['topic']}")

#format specifiers
pi = 3.14159265
print(f"pi:{pi:.2f}")

# Debugging =
temp = 0.7
print(f"{temp=}")

# multi line f-strings formatting
user_input = "What is langchain?"
context_text = "Lamgchain is a framework for building LLM apps"
system_prompt = f"""
you are a helpfull Ai tutor.
Context provided: {context_text}
student question: {user_input}
Instuctions:
-Answer based on only on the context above
-If the answer is not in the context ,say "i dont know"
-Keep your answers undder 3 sentences
""".strip()
print(system_prompt)


#Lists: ordered,mutable,heterogenous sequences
# In Gen AI: Chat history, chunks of retreived documents
# Token sequences
chat_history: list[dict] = [
    {"role":"user","content":"What is an LLM"},
    {"role":"assistant","content":"A LLM is a neural n/w trained on vast amounts of text."},
]
#access
first_msg = chat_history[0]
print(first_msg)
print(chat_history[-1]["content"])# to getnthe last element


# modify
chat_history.append({"role":"user","content":"What is an RAG"})
print(chat_history)
chat_history.pop(0)
print(chat_history)

# Iterate
for msg in chat_history:
    print(f"{msg['role'].upper()}:{msg['content']}")

# List of document chunks
chunks:list[str] = [
    "RAG stands for Retreival Augumented Generation",
    "It combines a retrirver with a generation",
]    
# Filter the chunks based on length
valid_chunks = [c for c in chunks if len(c.split())>=6]
print(valid_chunks)


