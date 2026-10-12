#Functions:
def build_prompt(topic:str,word_limit:int=150)->str:  #return type
    return f"Write about {topic}, with atmost {word_limit} words"

print(build_prompt("Gen AI"))
print(build_prompt("Prompt engineering",word_limit = 300))

# brushup following concepts
# *args,**kwargs
# List Comphrehension,Dict   Comphrehension 
