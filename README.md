Figure 1 : After running the project, output window is shown
![jj](https://github.com/user-attachments/assets/884cceee-6369-4049-8145-198a7383b425)
Figure 2 : After entering url of news article to summarize
![jj1](https://github.com/user-attachments/assets/539d81c4-cace-4aae-887e-cd7b108bfd60)
Figure 3 : Display the title, author, publication date, keywords, word count, and overall sentiment of the article
![jj2](https://github.com/user-attachments/assets/c60660b6-7a5b-42d2-8321-ecab47a0abf7)
Figure 4 : This figure displays important keywords from the article and total word count of the article
![jj3](https://github.com/user-attachments/assets/96b6f725-206f-4df3-9c22-851faab98d68)
Figure 5 : Users can save the summary and article details to a text file, also users can reset all fields to prepare for a new URL
![jj4](https://github.com/user-attachments/assets/371b85ac-39f2-4cc9-adde-08c7f3cee5e3)
Figure 6 : Dark Mode Toggle to switch between light and dark modes

## NeWs_PaPer_ArTiCLE_SUmmaRiZER
GUI-based application using Tkinter that allows users to input a news article URL and automatically summarize its content. The application also performs sentiment analysis on the article and provides additional features such as displaying the title, author, publication date, keywords, word count, and overall sentiment of the article.
### Key Features
1. URL Input: Users can input the URL of a news article for summarization.
2. Article Download and Parsing: Using the newspaper3k library, the article is downloaded and parsed. The article's text is then processed to extract key details.
3. Summary Display: The application extracts and displays the article's title, authors, publication date, and an auto-generated summary.
4. Sentiment Analysis: The app uses TextBlob to analyze the sentiment (positive, negative, or neutral) of the article's content based on its polarity.
5. Keyword Extraction: It shows important keywords from the article.
6. Word Count: The total word count of the article is displayed.
7. Save Summary: Users can save the summary and article details to a text file.
8. Clear Fields: A button allows users to reset all fields to prepare for a new URL.
9. Dark Mode Toggle: The app includes a feature to switch between light and dark modes.
10.Scrollable Window: A scrollbar allows easy navigation of the content even when the window is smaller than the content.
