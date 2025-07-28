from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


csharp_file = open(r"C:\Users\shaka\OneDrive\Documents\dotnet-csharp-language-reference.pdf", 'rb')

pdf_reader = PyPDF2.PdfReader(csharp_file)

for page in pdf_reader.pages:
      text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
            is_separator_regex=False
      )
      texts = text_splitter.create_documents([page.extract_text()])



csharp_file.close()
# loader = PyPDFLoader(file_path)

# docs = loader.load()
# print(docs[0])
# pprint.pp(docs[0].metadata)