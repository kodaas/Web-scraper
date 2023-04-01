from requests_html import HTMLSession
import webbrowser
import time

# Counts the number of books
count = 0
year = 2017

with open('Download Links 2.txt', 'a') as file:

    file.write(" ********* Check point ************")
    print("*************👉 Check point *******")

    # Get the list of topics from the topics file.
    with open("topic.txt", "r") as topic_file:
        
        # Go over each topic
        for index, topic in enumerate(topic_file):
             
            # if index == 10:
                # break

            if index < -1:
                continue

            topic_url = f'https://www.pdfdrive.com/search?q={topic.strip().replace(" ", "+")}&pagecount=100-*&pubyear={year}&searchin=en'

            session = HTMLSession()

            r = session.get(topic_url)

            book_container = r.html.find('.files-new', first=True)

            books = book_container.find('ul', first=True).find('li')

            file.write(f'\n\nTopic {(index + 1)}: {topic.strip()} \nURL: {topic_url} \n\n')

            print(f'\n\nTopic {(index + 1)}: {topic.strip()} \nURL: {topic_url} \n\n')


            for j, book in enumerate(books):

                count = count + 1

                download_id = ""

                download_session_id = ""

                book_url = list(book.absolute_links)[0]

                book_name = book.find('img', first=True).attrs['title']

                s = session.get(book_url)

                preview_button = s.html.find("#previewButtonMain", first=True).attrs

                download_id = preview_button["data-id"]

                download_session_id = preview_button['data-preview'][-32:]

                download_url = f"https://www.pdfdrive.com/download.pdf?id={download_id}&h={download_session_id}&u=cache&ext=pdf"

                # status = True
                status = webbrowser.open(download_url, new=2)


                print(f'Book {(j + 1)}: \n\t Name: {book_name} \n\t ID: {download_id} \n\t Session Id: {download_session_id} \n\t Download URL: {download_url} \n\t Status: {"Success" if status else "Error"} \n')    
                file.write(f'Book {(j + 1)}: \n\t Name: {book_name} \n\t ID: {download_id} \n\t Session Id: {download_session_id} \n\t Download URL: {download_url} \n\t Status: {"Success" if status else "Error"} \n\n')

                time.sleep(2) 
            
        
            file.write(f'Total Number of Books: {count} \n\n')
            print(f'Total Number of Books: {count} \n\n')







       


































#define our URL
# url = 'https://www.pdfdrive.com/search?q=remember+the+titans&pagecount=&pubyear=&searchin=&em='


# url = 'https://www.pdfdrive.com/hamiltons-curse-how-jeffersons-arch-enemy-betrayed-the-american-revolution-and-what-it-means-for-americans-today-d161054832.html'

# #use the session to get the data
# r = session.get(url)

# r.html.render(sleep=2, wait=5, keep_page=True)

# print(r.html.find('#alternatives', first=True).find('a', first=True).absolute_links)

# book_container = r.html.find('.files-new', first=True)

# books = book_container.find('ul', first=True).find('li')


# for index, book in enumerate(books):

#     print((index + 1),book.absolute_links, '\n')




# #Render the page, up the number on scrolldown to page down multiple times on a page
# r.html.render(sleep=3, keep_page=True, scrolldown=1)

# #take the rendered html and find the element that we are interested in
# videos = r.html.find('#video-title')

# #loop through those elements extracting the text and link
# for item in videos:
#     video = {
#         'title': item.text,
#         'link': item.absolute_links
#     }
#     print(video)
