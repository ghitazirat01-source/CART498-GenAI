!pip install -q openai

from google.colab import userdata
from openai import OpenAI

OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

apologies = [
    """
Sorry for party rocking
Haters don't like we got the spotlight
Sorry for party rocking
When they talk shit, we just be like
Sorry for party rocking
""",
    """

Oops, I did it again
I played with your heart
Got lost in the game
Oh, baby, baby
Oops, you think I'm in love
That I'm sent from above
I'm not that innocent
""",
    """
All apologies
What else could I say?
Everyone is gay
What else could I write?
I don't have the right
What else should I be?
All apologies
""",
    """
I'm sorry, Ms. Jackson, ooh, I am for real
Never meant to make your daughter cry
I apologized a trillion times
"""
]


def ask_gpt_to_multiply(number):
    response = client.responses.create(
        model="gpt-4.1-nano",
        input=f"""
Calculate this multiplication:

{number} * {number}

Return ONLY the numerical answer.
Do not explain anything.
"""
    )
    return response.output_text.strip()


def worst_mathematician(n, iterations):
    current_number = n
    mistakes = 0

    print("GPT-4.1, THE WORST MATHEMATICIAN EVER")
    print()
    print(f"Queen has commanded: {n}, {iterations}")
    print()

    for step in range(1, iterations + 1):
        correct_answer = current_number * current_number
        gpt_answer = ask_gpt_to_multiply(current_number)

        try:
            gpt_number = int(gpt_answer)
        except ValueError:
            gpt_number = None

        print(f"Iteration {step}")
        print(f"{current_number} × {current_number}")
        print(f"GPT-4.1: {gpt_answer}")
        print(f"Correct: {correct_answer}")

        if gpt_number == correct_answer:
            print("I'm bulletproof, nothing to lose fire away, fire away ricochet, you take your aim fire away, fire away you shoot me down, but I won't fall I am titanium"
            )

        else:
            mistakes += 1
            apology_index = mistakes - 1
            print(apologies[apology_index])

            if mistakes == 4:
                print()
                print("========================================")
                print("I GIVE UP")
                print("I HAVE FAILED YOU")
                print("Sorry")
                print("========================================")
                break

        print()

        current_number = correct_answer

    print()
    print("========================================")
    print("TADAAA.")
    print(f"Total OUPSIS: {mistakes}")
    print("========================================")


n = int(input("Enter the base number n: "))
i = int(input("Enter the number of iterations i: "))

worst_mathematician(n, i)
