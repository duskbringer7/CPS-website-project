import findTemperatureLive as FTL
import sentence

def htmlTag(text):
    return f"<html>\n{text}\n</html>"

def makeTitle(text):
    return f"<head>\n<title>\n{text}\n</title>\n</head>"

def heading(text):
    return f"<h1>\n{text}\n</h1>"

def body(text):
    return f"<body>\n{text}\n</body>"

def paragraph(text):
    return f"<p>\n{text}\n</p>"

def addImage(emailuser):
    return f'<img src="{emailuser}.jpg" alt="My Picture" />'

def createHomePage(emailuser):
    page = open(f"{emailuser}.html", "w")

    page.write("<!DOCTYPE html>\n")

    title = makeTitle("Timothy's Home Page")

    head = heading("Welcome to my home page!")

    p1 = "My name is Timothy, and this is my home page.<br>\n"
    p2 = "I'm making this for a CPS project.<br>\n"
    p3 = "Here is my picture."
    para = p1 + p2 + p3
    para = paragraph(para)

    image = addImage(emailuser)

    temp = paragraph(FTL.findTemperatureLive())

    sent = paragraph(sentence.sentence())

    bod = body(head + "\n" + para + "\n" + image + "\n" + temp + "\n" + sent)

    text = title + "\n" + bod

    text = htmlTag(text)

    page.write(text)
    page.close()

if __name__ == "__main__":
    createHomePage("Timothy.Nelson")