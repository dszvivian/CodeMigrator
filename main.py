import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro-latest')



def codeExplain(filepath):
  with open(filepath, 'r') as file:
    content = file.read()

  description_prompt = f"You will be given legacy code as input. You need to understand the entire code and generate detailed description of it such that the description generated explains all the variables, routines, classes, blocks or other structures present in the legacy code. \n{content}"
  description_response = model.generate_content(description_prompt)

  return description_response.text


def codeExplainFromContent(content):

  description_prompt = f"You will be given legacy code as input. You need to understand the entire code and generate detailed description of it such that the description generated explains all the variables, routines, classes, blocks or other structures present in the legacy code. \n{content}"
  description_response = model.generate_content(description_prompt)

  return description_response.text


def codeConvert(instructions,language):

  # Corrected Code Snippet

  code_prompt = (
      f"You are legacy to modern programming code generator. You\'ll be given a brief description of the legacy code. "
      f"You need to write a {language} code based on that description such that the entire description provided is followed "
      f"without any loss in programming feature from the legacy. Your response should be a single python markdown implementing "
      f"all the features mentioned in the description. If the code needs to have custom implementation, then implement it "
      f"using relevant libraries for that task.\nDescription: {instructions}"
      f"Let the response be the code in markdown format."
  )
  
  code_response = model.generate_content(code_prompt)

  return code_response.text

def explain_genearated_code(generated_code):
  code_prompt = (
    f"Explain the code .You need to understand the entire code and generate detailed description of it such that the description generated explains all the variables, routines, classes, blocks or other structures: \n{generated_code}"
  )

  code_response = model.generate_content(code_prompt)

  return code_response.text

def solve_error(generated_code,error_log):
  code_prompt = (
    f"Understand the Error Logs: {error_log}"
    f"fix the given Code:\n {generated_code}\n"
    f"Answer in Code Only"
  )

  code_repsonse = model.generate_content(code_prompt)

  return code_repsonse.text


def save_file(filename,data):
  folder_path = './results/' 
  file_name = filename 
  file_path = os.path.join(folder_path, file_name) 
  
  # Create the file 
  with open(file_path, 'w') as file: 
      file.write(data)


def remove_markdown(text):
    """
    Removes markdown
    """
    lines = text.splitlines()
    stripped_lines = lines[1:-1]
    stripped_text = '\n'.join(stripped_lines)
    return stripped_text








