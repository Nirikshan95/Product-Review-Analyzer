from src.llm_interface import get_chat_model
from src.output_parser import get_parser
from src.prompt_template import get_prompt

def main(review: str):
    """
    The main function takes a review as input, uses a chat model to generate a response, parses the
    response content, and returns the result.
    
    :param review: The `main` function takes a `review` parameter, which is a string representing a
    review. The function then uses this review to generate a response using a chat model, a parser, and
    a prompt. The response is then parsed and the result is returned
    :type review: str
    :return: The `result` variable is being returned from the `main` function.
    """
    model=get_chat_model()
    parser=get_parser()
    prompt=get_prompt(review)
    response=model.invoke(prompt)
    result=parser.parse(response.content)
    return result
    
if __name__=="__main__":
    review=input("Enter the review: ")
    result=main(review)
    print(result)