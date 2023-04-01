from requests_html import HTMLSession
import webbrowser
import time

# Initial Variables
count = 0
min_year = 2016
interval = 2
start_topic_index = 3
end_topic_index = 5
number_of_books = 3
number_of_books_skiped = 0


with open('Download Links 2.txt', 'a') as file:

    file.write(" ********* Check point ************")
    print("*************👉 Check point *******")

    # Get the list of topics from the topics file.
    with open("topic.txt", "r") as topic_file:
        
        # Go over each topic
        for index, topic in enumerate(topic_file):
             
            if index == end_topic_index:
                break

            if index < (start_topic_index - 1):
                continue

            # Generated link to download books
            topic_url = f'https://www.pdfdrive.com/search?q={topic.strip().replace(" ", "+")}&pagecount=100-*&pubyear={min_year}&searchin=en'

            # Initilaze session 1 <Search for books based on a perticular topic>
            session = HTMLSession()

            try:
                # Store session
                r = session.get(topic_url)

                # Find the books wrapper
                book_container = r.html.find('.files-new', first=True)

                # Store books
                books = book_container.find('ul', first=True).find('li')
            except:
                continue

            # Document each book title in the "Download Links File"
            file.write(f'\n\nTopic {(index + 1)}: {topic.strip()} \nURL: {topic_url} \n\n') 
            print(f'\n\nTopic {(index + 1)}: {topic.strip()} \nURL: {topic_url} \n\n')


            # Navigate to the download page to get each book
            for j, book in enumerate(books):

                if j == number_of_books:
                    break

                book_url = list(book.absolute_links)[0]

                book_name = book.find('img', first=True).attrs['title']

                # Initialize session 2 <For Downloading a single book>
                try:
                    s = session.get(book_url)

                    preview_button = s.html.find("#previewButtonMain", first=True).attrs

                    download_id = preview_button["data-id"]

                    download_session_id = preview_button['data-preview'][-32:]
                except:
                    number_of_books_skiped += 1
                    continue

                download_url = f"https://www.pdfdrive.com/download.pdf?id={download_id}&h={download_session_id}&u=cache&ext=pdf"

                status = True 
                # status = webbrowser.open(download_url, new=2)

                # Sores the number of books for each topic
                count = count + 1

                print(f'Book {(j + 1)}: \n\t Name: {book_name} \n\t ID: {download_id} \n\t Session Id: {download_session_id} \n\t Download URL: {download_url} \n\t Status: {"Success" if status else "Error"} \n')    
                file.write(f'Book {(j + 1)}: \n\t Name: {book_name} \n\t ID: {download_id} \n\t Session Id: {download_session_id} \n\t Download URL: {download_url} \n\t Status: {"Success" if status else "Error"} \n\n')

                time.sleep(interval)
            
        
            file.write(f'Total Number of Books: {count} \n')
            print(f'Total Number of Books: {count} \n')

            file.write(f'Total Number of Books Skiped: {number_of_books_skiped} \n\n')
            print(f'Total Number of Books Skiped: {number_of_books_skiped} \n\n')