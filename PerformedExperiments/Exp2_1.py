from ai_config import get_gemini_resposne

#few shot chain of thought
Systembehaviour=""" You are a Customer Feedback Analyst. Your job is to classify comments into 
    Positive, Negative, or Neutral and provide a one-sentence justification.
    Format your response exactly like the examples provided."""

comment=input("Enter your comment for product.")

prompt=f""" Example 1:
    Input: "The delivery arrived two days early and the packaging was perfect!"
    Output: [POSITIVE] - Customer is happy with delivery speed and product condition.

    Example 2:
    Input: "The app keeps crashing every time I try to upload a photo. Very frustrating."
    Output: [NEGATIVE] - Customer is experiencing technical bugs and expressing anger.

    Example 3:
    Input: "It's an okay product. Does what it says, but nothing special."
    Output: [NEUTRAL] - Customer feels the product meets basic expectations but lacks 'wow' factor.

    Input:{comment}
    give output.
"""

answer=get_gemini_resposne(prompt=prompt,system_prompt=Systembehaviour)

print("Comment:"+comment)
print(answer)