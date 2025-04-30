import streamlit as st
from chains import title_chain, content_chain, subtitle_chain, hashtag_chain
from utils import convert_to_pdf
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Blog Assistant", layout="centered")
st.title("📝 AI Blog Content Assistant")
st.markdown("Create engaging, SEO-ready blog posts using AI!")

# --- Title Generator ---
st.subheader('🔤 Generate Blog Titles')
with st.expander("Enter the topic for your blog post:"):
    topic_name = st.text_input("Topic name", key="topic_name")
    if st.button('Generate Titles'):
        if topic_name.strip():
            titles = title_chain.invoke({"topic": topic_name})
            st.text_area("Suggested Titles", value="\n".join(titles['text'].split('\n')), height=200)
        else:
            st.warning("Please enter a topic name.")

# --- Blog Generator ---
st.subheader('✍️ Generate Full Blog Content')
with st.expander("Provide details for your blog post:"):
    blog_title = st.text_input("Blog Title")
    blog_length = st.slider('Length (words):', 300, 1500, 500)

    if st.button("Generate Blog"):
        if blog_title.strip():
            with st.spinner("Generating blog content..."):
                blog = content_chain.invoke({"title": blog_title, "blog_length": blog_length})['text']
                subtitle = subtitle_chain.invoke({"title": blog_title})['text'].strip()
                hashtags = hashtag_chain.invoke({"title": blog_title})['text'].strip()

            st.markdown("### 📄 Blog Preview")
            st.markdown(f"**{blog_title}**  \n*{subtitle}*", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(blog)
            st.markdown("---")
            st.markdown(f"**📌 Suggested Hashtags:** `#{' #'.join(hashtags.splitlines())}`")

            st.download_button("📥 Download as TXT", data=blog, file_name=f"{blog_title}.txt", mime="text/plain")

            pdf_data = convert_to_pdf(blog, blog_title, subtitle)
            st.download_button("📄 Download as PDF", data=pdf_data, file_name=f"{blog_title}.pdf", mime="application/pdf")
        else:
            st.warning("Please enter a blog title.")
