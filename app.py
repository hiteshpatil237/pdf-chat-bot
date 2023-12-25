import streamlit as st


def main():
    st.set_page_config(page_title="PDF Chatbot", page_icon=":books:")

    st.header("PDF Chatbot :books:")
    st.text_input("Ask a question about the inputted pdfs: ")

    with st.sidebar:
        st.subheader("Your PDFs")
        st.file_uploader("Upload your PDFs here and click on Process")
        st.button("Process")

if __name__ == '__main__':
    main()