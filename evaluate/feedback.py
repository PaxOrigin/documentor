"""Manual feedback prompt."""


def prompt_feedback(answer: str) -> str:
    """Ask user for feedback on an answer."""
    # Placeholder interactive prompt
    return input(f"Was this helpful? ({answer}) [y/n]: ")
