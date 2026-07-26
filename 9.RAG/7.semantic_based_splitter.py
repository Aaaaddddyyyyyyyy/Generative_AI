from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter= SemanticChunker(
    GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1
)

sample="""Artificial Intelligence (AI) is transforming industries across the world. Machine learning enables computers to identify patterns in data and make predictions without being explicitly programmed. Deep learning, a subset of machine learning, uses neural networks with multiple layers to solve complex tasks such as image recognition and natural language processing.

Healthcare is one of the biggest beneficiaries of AI. Hospitals use AI-powered systems to detect diseases from medical images, assist doctors in diagnosis, and predict patient outcomes. Wearable devices also monitor heart rate, sleep, and physical activity, helping people maintain healthier lifestyles.

Climate change is another major global challenge. Rising temperatures, melting glaciers, and increasing sea levels threaten ecosystems and human settlements. Governments and organizations are investing in renewable energy sources such as solar and wind power to reduce greenhouse gas emissions and build a more sustainable future.

Space exploration continues to capture human imagination. Modern rockets have significantly reduced the cost of launching satellites, enabling advances in communication, navigation, and weather forecasting. Scientists are also planning future missions to Mars to search for evidence of past life and prepare for long-term human exploration.

Personal finance is an important life skill. Creating a monthly budget, saving regularly, and investing wisely can help individuals achieve financial stability. Understanding concepts such as compound interest, inflation, and diversification allows people to make better long-term financial decisions.


"""

docs=text_splitter.create_documents([sample])
print(len(docs))
print(docs)