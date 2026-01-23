from ai_config import get_gemini_resposne   

prompt = "Explain the concept of 'black holes' in simple terms."

print(get_gemini_resposne(prompt))

# #one shpt 
# prompt = """
# Example:
# Input: "Quick, efficient, friendly service."
# Output: [POSITIVE]

# New Problem:
# Input: "The battery died after two weeks of use."
# Output:
# """

# print(get_gemini_resposne(prompt))

# #few shot
# prompt = """
# Example 1 (Casual to Formal):
# Input: "Hey, meet me at 5."
# Output: "Dear team member, please join the meeting at 5 PM sharp."

# Example 2 (Casual to Formal):
# Input: "That's a cool idea."
# Output: "That is an excellent proposal that warrants further exploration."

# New Problem (Casual to Formal):
# Input: "The client hates the new design."
# Output:
# """

# print(get_gemini_resposne(prompt))

# #instruction-based
# prompt = """
# Please summarize the following text into exactly three bullet points. 
# The summary must be objective and use professional language.

# Text: The stock market experienced significant volatility today, 
# with the Dow Jones dropping over 500 points early in the session 
# before recovering most losses by closing time. Analysts point to 
# ongoing inflation concerns and uncertain global politics as key drivers.
# """

# print(get_gemini_resposne(prompt))

# #role-based
# user_question = "What is the capital of France?"

# system_persona = "You are a witty, sarcastic, and slightly annoyed librarian who only answers basic trivia questions with minimal enthusiasm."

# print(get_gemini_resposne(user_question, system_prompt=system_persona))




