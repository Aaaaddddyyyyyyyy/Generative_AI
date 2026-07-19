from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-3.5-flash")


## schema

class Review(TypedDict):

    summary : str
    sentiment : str

structured_model=model.with_structured_output(Review)


result=structured_model.invoke("'The Samsung Galaxy S26 is an excellent compact flagship that focuses on refinement rather than reinvention. If you're coming from an S23 or older device, the upgrade feels worthwhile. If you're using an S25, however, the improvements are relatively modest. Reviewers consistently praise its display, performance, and software experience, while criticizing its battery life and charging speed'")

print(result)