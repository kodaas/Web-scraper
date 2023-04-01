from requests_html import HTMLSession
import webbrowser
import time

with open("topic.txt", "r") as topic_file:

        for index, line in enumerate(topic_file):

            if index < 1:
                 continue
             
            if index == 2:
                break

            topic_url = f'https://www.pdfdrive.com/search?q={line.strip().replace(" ", "+")}&pagecount=100-*&pubyear=2015&searchin=en'

            session = HTMLSession()

            r = session.get(topic_url)

            book_container = r.html.find('.files-new', first=True)

            books = book_container.find('ul', first=True).find('li')

            # file.write(f'\n\n Topic {(index + 1)}: {line.strip()}  \n\n')

            print(line.strip())
            print("Topic",(index + 1), "URL:", topic_url)
            print(r.html, '\n')

            temp = []

            for j, book in enumerate(books):

                if j == 5:
                    break

                download_id = ""

                download_session_id = ""

                book_url = list(book.absolute_links)[0] 

                s = session.get(book_url)

                preview_button = s.html.find("#previewButtonMain", first=True).attrs

                download_id = preview_button["data-id"]

                download_session_id = preview_button['data-preview'][-32:]

                download_url = f"https://www.pdfdrive.com/download.pdf?id={download_id}&h={download_session_id}&u=cache&ext=pdf"

                status = webbrowser.open(download_url, new=2)


                print(download_id, download_session_id, download_url, status, '\n')    
                time.sleep(2) 


                # for i in reversed(range(len(book_link_list))):

                #     if book_link_list[i] == 'e':
                #         book_link_list[i] = 'd'
                #         break

                
                # book_download_url = "".join(book_link_list)

                # temp.append(book_download_url)
                # print((j + 1), book_download_url, '\n')
