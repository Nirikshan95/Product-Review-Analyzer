from langchain.prompts import PromptTemplate
from src.output_parser import get_parser

def get_prompt(review):
    """
    This Python function generates a prompt for a product review analysis, including instructions for
    analyzing pros, cons, summary, and sentiment of the review.
    
    :param review: It looks like you are trying to create a prompt for a product review analyzer. The
    `get_prompt` function takes a review as input and generates a template for analyzing the review. The
    template includes instructions for analyzing the pros, cons, summary, and sentiment of the review
    :return: The `get_prompt` function returns a prompt template that includes instructions for a
    product review analyzer. The template includes placeholders for the product review, format
    instructions, and the required information to be provided by the analyzer (pros, cons, summary,
    sentiment). The function uses a parser to get format instructions and then fills in the template
    with the provided review and format instructions before returning the complete prompt.
    """
    parser=get_parser()
    template = """You are a product review analyzer. You will be given a product review and you need to analyze it and provide the following information:
    1. Pros of the product
    2. Cons of the product
    3. Summary of the review
    4. Sentiment of the review (Positive, Negative, Neutral).
    
    review: {review} .\n
    {format_instructions}
    """
    
    prompt_temp= PromptTemplate(template=template, input_variables=["review"],partial_variables={"format_instructions":parser.get_format_instructions()})
    return prompt_temp.invoke({"review":review})