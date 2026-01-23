from ai_config import get_gemini_resposne

# chain of thought 
systembehaviour="""
    You are a logical reasoning assistant. 
    For every request, follow these steps:
    1. Analyze the core problem and constraints.
    2. Break the solution into a clear, numbered sequence of logical steps.
    3. Verify each step for accuracy before proceeding to the next.
    4. Provide the final answer only after your reasoning is complete.
    Always format your internal reasoning clearly.
    """

prompt="i have 1 pen which  price is 4 then how much total rpice of 4 pens give answer step by step."

answer=get_gemini_resposne(system_prompt=systembehaviour,prompt=prompt)

print(answer)


