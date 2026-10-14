
from classifier import classify_with_laya
from router import get_response


def main():
    print("=" * 45)
    print("       LAYA + LITELLM MODEL ROUTER")
    print("=" * 45)

    while True:
        user_input = input(
            "\nEnter your question (or 'exit' to quit): "
        ).strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Application closed.")
            break

        if not user_input:
            print("Please enter a question.")
            continue

        try:
            # Step 1: Classify with Laya
            complexity = classify_with_laya(user_input)
            print(f"\nLaya classification: {complexity}")

            # Step 2: Select the provider and get the answer
            if complexity == "SIMPLE":
                print("Selected provider: Groq")
            else:
                print("Selected provider: Gemini")

            answer = get_response(user_input, complexity)

            # Step 3: Display the answer
            print("\nAnswer:")
            print(answer)

        except Exception as error:
            print(f"\nRequest failed: {error}")


if __name__ == "__main__":
    main()
