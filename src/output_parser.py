from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

class Review(BaseModel):
    pros:str=Field(description="Pros of the product")
    cons:str=Field(description="Cons of the product")
    summary:str=Field(description="Summary of the review")
    sentiment:Literal["Positive","Negative","Neutral"]=Field(description="Sentiment of the review")
    
def get_parser():
    return PydanticOutputParser(pydantic_object=Review)