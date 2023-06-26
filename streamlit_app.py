import streamlit as st

from langchain.llms import OpenAI

from langchain import PromptTemplate

st.set_page_config(page_title="Personal AI Career Guide ")
st.title('Personal Career Guide')
st.caption("""This is a Personal Career Guiding bot, which helps you in taking neccessary steps to grow, excel or enter into a certain field, just enter your Field of interest and it would help you in properly managing all the stpes to excel in that.""")_
openai_api_key = st.sidebar.text_input('OpenAI API key', type='password')

def generate_response(topic):
	llm = OpenAI(model_name='text-davinci-003', openai_api_key=openai_api_key)
	template = 'You are a experienced career guide, hiring manager and role suggestion AI, who helps people on queries related to career. YOur job is to suggest best steps to excel or enter into the {topic_text}, with proper context and source.'
	prompt = PromptTemplate(input_variables=['topic'], template=template)
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

