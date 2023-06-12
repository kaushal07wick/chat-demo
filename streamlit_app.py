import streamlit as st

from langchain.llms import OpenAI

from langchain import PromptTemplate

st.set_page_config(page_title="Query Demo App")
st.title('Query Demo App')
openai_api_key = st.sidebar.text_input('OpenAI API key', type='password')

def generate_response(topic):
	llm = OpenAI(model_name='text-davinci-003', openai_api_key=openai_api_key)
	template = 'As an experienced hiring manager, tell me the key qualifications required for {job} role.'
	prompt = PromptTemplate(input_variables=['job'], template=template)
	prompt_query = prompt.format(topic=topic)

	#run the llm model and return or print out the response

	response = llm(prompt_query)
	return st.info(response)

with st.form('theform'):
	topic_text = st.text_input('Enter the keyword:','')
	submitted = st.form_submit_button('Submit')
	if not openai_api_key.startswith('sk-'):
		st.warning('Please enter your OpenAI api key!', icon='⚠')
	if submitted and openai_api_key.startswith('sk-'):
		generate_response(topic_text)
		
