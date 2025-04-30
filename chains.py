from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

llm = ChatGroq(
    temperature=0.6,
    model="Gemma2-9b-It",
    model_kwargs={"top_p": 0.9},
    api_key=os.getenv("GROQ_API_KEY")
)

title_prompt = PromptTemplate(
    input_variables=['topic'],
    template='''I'm planning a blog post on the topic: {topic}.
Suggest a list of ten creative and attention-grabbing titles for this blog post.
Don't give any explanation or overview for each title.'''
)

blog_prompt = PromptTemplate(
    input_variables=['title', 'blog_length'],
    template='''Write a high-quality, informative, and plagiarism-free blog post on the topic: "{title}". 
Aim for a content length of {blog_length} words.
Use markdown formatting with headings and paragraph breaks.
Make it conversational and engaging with intro, body, and conclusion.'''
)

subtitle_prompt = PromptTemplate(
    input_variables=['title'],
    template='''Write a short and compelling subtitle (meta description) for a blog post titled "{title}". Keep it under 25 words.'''
)

hashtag_prompt = PromptTemplate(
    input_variables=['title'],
    template='''Suggest 5 relevant and popular hashtags for a blog post titled "{title}". Don't include the '#' symbol. Just give the words.'''
)

title_chain = LLMChain(llm=llm, prompt=title_prompt)
content_chain = LLMChain(llm=llm, prompt=blog_prompt)
subtitle_chain = LLMChain(llm=llm, prompt=subtitle_prompt)
hashtag_chain = LLMChain(llm=llm, prompt=hashtag_prompt)
