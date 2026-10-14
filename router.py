
from dotenv import load_dotenv
from litellm import completion

load_dotenv()


def get_response(user_input: str, complexity: str) -> str:
    """Route SIMPLE requests to Groq and COMPLEX requests to Gemini."""

    if complexity == "SIMPLE":
        model = "groq/openai/gpt-oss-20b"

    elif complexity == "COMPLEX":
        model = "gemini/gemini-3.5-flash-lite"

    else:
        raise ValueError(f"Invalid complexity: {complexity}")

    response = completion(
        model=model,
        messages=[
            {"role": "user", "content": user_input}
        ],
        temperature=0.2,
    )

    answer = response.choices[0].message.content

    if not answer:
        raise RuntimeError(
            f"{model} returned an empty response."
        )

    return answer
