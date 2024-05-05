from llm.invoke import LLM
from localqa.qa import VideoQA
import streamlit as st

llm = LLM("./model/Phi-3-mini-4k-instruct-q4.gguf")

st.set_page_config(page_title="🏗Llama-cpp-Python YouTube Video QA",
                   page_icon="📹")


def main():
    video_qa = None
    st.title("🏗Llama-cpp-Python YouTube Video QA")
    if 'video_url' not in st.session_state or st.session_state.video_url == "":
        video_url = st.text_input("Enter YouTube Video URL:", "")
        if video_url:
            st.session_state.video_url = video_url
    else:
        video_url = st.session_state.video_url
        st.write(f"Using video URL: {video_url}")
        change_url = st.button("Change Video URL")
        if change_url:
            st.session_state.video_url = ""
            st.experimental_rerun()

    question = st.text_input("Enter your question about the video:",
                             key="question")
    if st.button("Answer Question"):
        if video_url and question:
            if video_qa == None:
                video_qa = VideoQA(llm=llm, video_url=video_url)

            st.write_stream(video_qa(question))

        else:
            st.error("Please provide both a YouTube URL and a question.")


if __name__ == "__main__":
    main()
