import laya

# Load Laya once when this module is imported.
# The first run may download the model checkpoint.
agent = laya.load("convaiinnovations/laya")

QUESTIONS = {
    "complexity": {
        "type": "choice",
        "instructions": (
            "Classify the user's request according to the "
            "reasoning and problem-solving required."
        ),
        "criteria": {
            "SIMPLE": (
                "Straightforward factual questions, definitions, "
                "basic explanations, simple calculations, or "
                "simple text transformations."
            ),
            "COMPLEX": (
                "Multi-step reasoning, challenging coding or "
                "debugging, system design, detailed analysis, "
                "or tasks with several interacting constraints."
            ),
        },
    }
}


def classify_with_laya(user_input: str) -> str:
    """Return SIMPLE or COMPLEX using local Laya inference."""

    result = agent.predict(
        {"request": user_input},
        QUESTIONS,
    )

    complexity = (
        result["answers"]["complexity"]["choice"]
    ).upper()

    if complexity not in {"SIMPLE", "COMPLEX"}:
        raise ValueError(
            f"Unexpected classification: {complexity}"
        )

    return complexity
