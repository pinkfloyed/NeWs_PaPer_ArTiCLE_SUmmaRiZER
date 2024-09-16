import tkinter as tk
from textblob import TextBlob
from newspaper import Article

def summarize():
    url = utext.get('1.0', "end").strip()
    loading_label.config(text="Loading...")
    root.update_idletasks()

    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        # Display word count
        word_count = len(article.text.split())
        word_count_label.config(text=f"Word Count: {word_count}")

        title.config(state='normal')
        author.config(state='normal')
        publication.config(state='normal')
        summary.config(state='normal')
        sentiment.config(state='normal')
        keywords.config(state='normal')

        title.delete(1.0, 'end')
        title.insert('1.0', article.title)

        author.delete(1.0, 'end')
        author.insert('1.0', article.authors)

        publication.delete(1.0, 'end')
        publication.insert('1.0', article.publish_date)

        summary.delete(1.0, 'end')
        summary.insert('1.0', article.summary)

        keywords.delete(1.0, 'end')
        keywords.insert('1.0', ', '.join(article.keywords))

        analysis = TextBlob(article.text)  # Full text sentiment analysis
        sentiment.delete(1.0, 'end')
        sentiment.insert('1.0', f'Polarity : {analysis.polarity}, Sentiment : {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

        title.config(state='disabled')
        author.config(state='disabled')
        publication.config(state='disabled')
        summary.config(state='disabled')
        sentiment.config(state='disabled')
        keywords.config(state='disabled')

    except Exception as e:
        title.config(state='normal')
        title.delete(1.0, 'end')
        title.insert('1.0', "Error: Invalid URL or cannot download article.")
        title.config(state='disabled')

    finally:
        loading_label.config(text="")

def clear_fields():
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    keywords.config(state='normal')

    title.delete(1.0, 'end')
    author.delete(1.0, 'end')
    publication.delete(1.0, 'end')
    summary.delete(1.0, 'end')
    sentiment.delete(1.0, 'end')
    keywords.delete(1.0, 'end')
    utext.delete(1.0, 'end')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')
    keywords.config(state='disabled')

def save_summary():
    with open("summary.txt", "w") as f:
        f.write("Title: " + title.get("1.0", "end"))
        f.write("\nAuthors: " + author.get("1.0", "end"))
        f.write("\nPublication Date: " + publication.get("1.0", "end"))
        f.write("\nSummary: " + summary.get("1.0", "end"))
        f.write("\nSentiment: " + sentiment.get("1.0", "end"))

def toggle_mode():
    if root['bg'] == 'white':
        root.config(bg='black')
        title.config(bg='black', fg='white')
        author.config(bg='black', fg='white')
        publication.config(bg='black', fg='white')
        summary.config(bg='black', fg='white')
        sentiment.config(bg='black', fg='white')
        keywords.config(bg='black', fg='white')
    else:
        root.config(bg='white')
        title.config(bg='#91D8E4', fg='black')
        author.config(bg='#91D8E4', fg='black')
        publication.config(bg='#91D8E4', fg='black')
        summary.config(bg='#91D8E4', fg='black')
        sentiment.config(bg='#91D8E4', fg='black')
        keywords.config(bg='#91D8E4', fg='black')

root = tk.Tk()
root.title('Article Summarizer')
root.geometry('1200x800')

# Loading label
loading_label = tk.Label(root, text="")
loading_label.pack()

# Frame for the scrollable text areas
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=50, pady=20)  # Added padding here

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Canvas for adding scrolling functionality
canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill="both", expand=True)
scrollbar.config(command=canvas.yview)

# Scrollable frame inside the canvas
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# For the Title block
tlabel = tk.Label(scrollable_frame, text="Title")
tlabel.pack(pady=5)
title = tk.Text(scrollable_frame, height=2, width=140)
title.config(state='disabled', bg='#91D8E4')
title.pack()

# For the Author block
alabel = tk.Label(scrollable_frame, text="Author")
alabel.pack(pady=5)
author = tk.Text(scrollable_frame, height=2, width=140)
author.config(state='disabled', bg='#91D8E4')
author.pack()

# For the Publication Date block
plabel = tk.Label(scrollable_frame, text="Publication Date")
plabel.pack(pady=5)
publication = tk.Text(scrollable_frame, height=2, width=140)
publication.config(state='disabled', bg='#91D8E4')
publication.pack()

# For the Summary block
slabel = tk.Label(scrollable_frame, text="Summary")
slabel.pack(pady=5)
summary = tk.Text(scrollable_frame, height=20, width=140)
summary.config(state='disabled', bg='#91D8E4')
summary.pack()

# For the Keywords block
kwlabel = tk.Label(scrollable_frame, text="Keywords")
kwlabel.pack(pady=5)
keywords = tk.Text(scrollable_frame, height=2, width=140)
keywords.config(state='disabled', bg='#91D8E4')
keywords.pack()

# For the Sentiment Analysis block
selabel = tk.Label(scrollable_frame, text="Sentiment Analysis")
selabel.pack(pady=5)
sentiment = tk.Text(scrollable_frame, height=2, width=140)
sentiment.config(state='disabled', bg='#91D8E4')
sentiment.pack()

# Word Count
word_count_label = tk.Label(scrollable_frame, text="")
word_count_label.pack(pady=5)

# For the URL input block
ulabel = tk.Label(scrollable_frame, text="Enter the article URL")
ulabel.pack(pady=5)
utext = tk.Text(scrollable_frame, height=2, width=140)
utext.pack(pady=5)

# Button to Summarize
btn = tk.Button(scrollable_frame, text="Summarize", command=summarize)
btn.pack(pady=5)

# Button to Save Summary
save_btn = tk.Button(scrollable_frame, text="Save Summary", command=save_summary)
save_btn.pack(pady=5)

# Button to Clear Fields
clear_btn = tk.Button(scrollable_frame, text="Clear", command=clear_fields)
clear_btn.pack(pady=5)

# Button to Toggle Dark Mode
mode_btn = tk.Button(scrollable_frame, text="Toggle Dark Mode", command=toggle_mode)
mode_btn.pack(pady=5)

root.mainloop()

# Tested url
# url : https://edition.cnn.com/travel/article/dhaka-bangladesh-public-transport-metro-intl-hnk/index.html
# url : https://www.nytimes.com/2022/12/28/world/europe/ukraine-russia-peace-talks.html