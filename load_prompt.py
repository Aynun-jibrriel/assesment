# def load_prompt_template(file_path):
#     """Load a prompt template from a text file."""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             template = file.read()
#         return template
#     except FileNotFoundError:
#         print("Error: Template file not found.")
#         return None


# def fill_prompt(template, **kwargs):
#     """
#     Fill the template using keyword arguments.
#     Example: fill_prompt(template, purpose="Requesting leave")
#     """
#     for key, value in kwargs.items():
#         placeholder = f"{{{{{key}}}}}"   # Converts "purpose" → "{{purpose}}"
#         template = template.replace(placeholder, value)
#     return template


# if __name__ == "__main__":
#     template = load_prompt_template("prompt_template.txt")

#     if template:
#         filled_prompt = fill_prompt(
#             template,
#             purpose="Requesting an internship extension",
#             tone="Formal",
#             points="Reason for delay, new timeline, reassurance of progress",
#             closing="Regards"
#         )

#         print("\nGenerated Prompt:\n")
#         print(filled_prompt)
import os
from groq import Groq

def load_template(file_path: str) -> str:
    """Load prompt template from a file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def fill_template(template: str, values: dict) -> str:
    """Fill dynamic placeholders like {topic}, {tone}"""
    return template.format(**values)


def send_to_groq(prompt: str):
    """Send final prompt to Groq model"""
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]


if __name__ == "__main__":
    # 1. Load template
    template = load_template("template.txt")

    # 2. Values to fill dynamically
    values = {
        "topic": "Machine Learning fundamentals",
        "tone": "friendly"
    }

    # 3. Fill template
    final_prompt = fill_template(template, values)

    print("=== Final Prompt ===")
    print(final_prompt)
    print("====================\n")

    # 4. Send to Groq
    output = send_to_groq(final_prompt)

    print("=== Model Response ===")
    print(output)
