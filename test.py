from facebook_scraper import get_posts
import csv
page = "beaverconfessions"
#page = "Fake-MIT-Confessions-100691552123875"
count = 0
with open('MIT_Confessions.csv', 'w', newline='', encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for post in get_posts(page, pages=1000, extra_info=True):
        #print(len(post["comments_full"]))
        post_text = post["post_text"]
        print(post)
        comments = post["comments_full"]
        to_write = [post_text]
        #print("***COMMENTS***")
        for comment in comments:
        #    print(comment["comment_text"])
            to_write.append(comment["comment_text"])
        count += 1
        spamwriter.writerow(to_write)
#        if count > 5:
#            break
