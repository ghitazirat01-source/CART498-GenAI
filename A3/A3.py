!pip install -q openai

from google.colab import userdata
from openai import OpenAI

client = OpenAI(api_key=userdata.get("OPENAI_API_KEY"))

math_temperature = 1
math_top_p = 1.0

text_temperature = 1.9
text_top_p = .99


def gpt_math(number):

    response = client.responses.create(
        model="gpt-4.1-nano",
        temperature=math_temperature,
        top_p=math_top_p,
        input=[
            {
                "role": "developer",
                "content": """
Calculate the multiplication given by the user.
Return ONLY the numerical answer.
No words.
No explanations.
No symbols.
No commas.
"""
            },
            {
                "role": "user",
                "content": "12 * 12"
            },
            {
                "role": "assistant",
                "content": "144"
            },
            {
                "role": "user",
                "content": f"{number} * {number}"
            }
        ]
    )

    return response.output_text.strip()


def gpt_apology(mistakes):

    response = client.responses.create(
        model="gpt-4.1-nano",
        temperature=text_temperature,
        top_p=text_top_p,
        input=[
            {
                "role": "developer",
                "content": f"""
You are a mathematician .

The user is your Master.

You have just made mistake number {mistakes}.

Every time you make a mistake, apologize.
Become more embarrassed, desperate and dramatic
with each mistake.

On mistake 6, completely give up on mathematics.

Keep your response short and funny.
"""
            },
            {
                "role": "user",
                "content": "React to your mathematical failure."
            },
            {
                "role": "assistant",
                "content": "My apologies, Master. I have failed at mathematics."
            },
            {
                "role": "user",
                "content": f"This is mistake number {mistakes}. React to your failure."
            }
        ]
    )

    return response.output_text.strip()


def worst_mathematician(n, iterations):

    number = n
    mistakes = 0

    for i in range(iterations):

        python_answer = number * number
        gpt_answer = gpt_math(number)

        print()
        print(f"Iteration {i + 1}")
        print(f"Python calculation = {python_answer}")
        print(f"GPT calculation = {gpt_answer}")

        try:
            gpt_number = int(gpt_answer)
        except:
            gpt_number = None

        if gpt_number != python_answer:

            mistakes += 1

            print()
            print(gpt_apology(mistakes))

            if mistakes == 6:
                break

        number = python_answer


n = int(input("Enter n: "))
i = int(input("Enter iterations: "))

worst_mathematician(n, i)
