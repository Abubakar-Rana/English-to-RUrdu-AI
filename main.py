# import streamlit as st
# from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# # Load the translation model using pipeline
# @st.cache_resource
# def load_pipeline():
#     return pipeline("text2text-generation", model="abdulwaheed1/english-to-urdu-translation-mbart")

# # Load model directly
# @st.cache_resource
# def load_model():
#     tokenizer = AutoTokenizer.from_pretrained("abdulwaheed1/english-to-urdu-translation-mbart")
#     model = AutoModelForSeq2SeqLM.from_pretrained("abdulwaheed1/english-to-urdu-translation-mbart")
#     return tokenizer, model

# # Initialize the Streamlit app
# def main():
#     st.title("English to Urdu Translator")
#     st.write("Enter English text below and get the translation in Urdu.")

#     # Load the pipeline and model
#     translation_pipeline = load_pipeline()
#     tokenizer, model = load_model()

#     # Input text box for user
#     english_text = st.text_area("Input English Text", height=150)

#     if st.button("Translate with Pipeline"):
#         if english_text:
#             # Use the pipeline for translation
#             translated_text = translation_pipeline(english_text, max_length=400)[0]['generated_text']
#             st.subheader("Translated Urdu Text (using Pipeline):")
#             st.write(translated_text)
#         else:
#             st.error("Please enter some text to translate.")

#     if st.button("Translate with Model"):
#         if english_text:
#             # Use the model directly for translation
#             inputs = tokenizer.encode(english_text, return_tensors="pt")
#             outputs = model.generate(inputs, max_length=400)
#             translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

#             st.subheader("Translated Urdu Text (using Model):")
#             st.write(translated_text)
#         else:
#             st.error("Please enter some text to translate.")

# if __name__ == "__main__":
#     main()
