!pip install transformers
!pip install transformers fpdf
from transformers import pipeline
from fpdf import FPDF
#load pre-trained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#get input from the user and summarize
def summarize_text():
  text = input("Please enter the text you need to summarize: ")

  summary = summarizer(text, max_length = 150, min_length=40, do_sample = False)
  summary_text = summary[0]['summary_text']
  print("Summary:")
  print(summary_text)

  #save_summary(summary_text)

summarize_text()

#save summary as pdf file
def save_summary(summary_text):
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Arial", size= 11)

  pdf.cell(200,10, txt="summary", ln=True, align='C')

  pdf.multi_cell(0,10, txt=summary_text)

  pdf.output("summary.pdf")
  print("Summary saved to summary.pdf")
