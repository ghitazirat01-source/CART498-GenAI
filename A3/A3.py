!pip install -q openai

from google.colab import userdata
from openai import OpenAI

client = OpenAI(api_key=userdata.get('OPENAI_API_KEY'))

temperature = 1.0
top_p = 1.0


def gpt_math(number):

    response = client.responses.create(
        model="gpt-4.1-nano",
        temperature=temperature,
        top_p=top_p,
        input=[
            {
                "role": "developer",
                "content": "Calculate the multiplication. Return only the number."
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
        temperature=temperature,
        top_p=top_p,
        input=[
            {
                "role": "developer",
                "content": """
You are GPT-4.1, the worst mathematician ever.
The user is your Master.

Every time you make a mistake, apologize.
Become more embarrassed, desperate and dramatic with each mistake.
On mistake 4, completely give up on mathematics.
Keep it short and funny.
"""
            },
            {
                "role": "user",
                "content": "You made your first mistake."
            },
            {
                "role": "assistant",
                "content": "My apologies, Master. I have failed at mathematics."
            },
            {
                "role": "user",
                "content": f"You just made mistake number {mistakes}. React."
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

            if mistakes == 4:
                break

        number = python_answer


n = int(input("Enter n: "))
i = int(input("Enter iterations: "))

worst_mathematician(n, i)
