from llm import ask_gemini

def find_match(found_item, lost_items):

    prompt = f"""
You are an AI Lost and Found matching system.

Found Item:
{found_item}

Lost Items:
{lost_items}

Compare the found item with each lost item.

Consider:
- Item name
- Description
- Location
- Date
- Important identifying details

Return the best possible matches with:
1. Item name
2. Match percentage
3. Reason for the match

Do not invent information.
"""

    return ask_gemini(prompt)