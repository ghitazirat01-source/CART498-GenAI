import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "openai-community/gpt2"
X = 7

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

poem = """One must have a mind of winter
To regard the frost and the boughs
Of the pine-trees crusted with snow;
And have been cold a long time
To behold the junipers shagged with ice,
The spruces rough in the distant glitter
Of the January sun; and not to think
Of any misery in the sound of the wind,
In the sound of a few leaves,
Which is the sound of the land
Full of the same wind
That is blowing in the same bare place
For the listener, who listens in the snow,
And, nothing himself, beholds
Nothing that is not there and the nothing that is."""

lines = poem.splitlines()


def get_xth_token(prompt, x=7):

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits[0, -1, :]
    probabilities = torch.softmax(logits, dim=-1)

    top_probs, top_ids = torch.topk(probabilities, x)

    token_id = top_ids[x - 1].item()

    return tokenizer.decode([token_id]).strip()


for line in lines:

    if not line.strip():
        print()
        continue

    words = line.split()

    if len(words) < 2:
        print(line)
        continue

  
    beginning = " ".join(words[:-1])


    new_word = get_xth_token(beginning, X)


    print(beginning + " " + new_word)


---------------------------------- p+1000 ------------------


import torch
import nltk
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "openai-community/gpt2"
X = 1000

nltk.download("averaged_perceptron_tagger_eng", quiet=True)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()


poem = """One must have a mind of winter
To regard the frost and the boughs
Of the pine-trees crusted with snow;
And have been cold a long time
To behold the junipers shagged with ice,
The spruces rough in the distant glitter
Of the January sun; and not to think
Of any misery in the sound of the wind,
In the sound of a few leaves,
Which is the sound of the land
Full of the same wind
That is blowing in the same bare place
For the listener, who listens in the snow,
And, nothing himself, beholds
Nothing that is not there and the nothing that is."""

lines = poem.splitlines()


def get_xth_noun(prompt, x=1000):

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits[0, -1, :]
    probabilities = torch.softmax(logits, dim=-1)
  
    sorted_ids = torch.argsort(probabilities, descending=True)

    noun_count = 0

    for token_id in sorted_ids:

        token = tokenizer.decode([token_id.item()])
        word = token.strip()
      
        if not word.isalpha():
            continue

        if not token.startswith(" "):
            continue

        # Identify nouns
        tag = nltk.pos_tag([word])[0][1]

        if tag in ["NN", "NNS", "NNP", "NNPS"]:
            noun_count += 1

            if noun_count == x:
                return word

    raise ValueError("Could not find 1000 complete noun tokens.")



for line in lines:

    if not line.strip():
        print()
        continue

    words = line.split()

    if len(words) < 2:
        print(line)
        continue


    beginning = " ".join(words[:-1])


    new_word = get_xth_noun(beginning, X)


    print(beginning + " " + new_word)



