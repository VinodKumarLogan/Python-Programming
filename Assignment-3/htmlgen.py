import argparse,webbrowser

parser = argparse.ArgumentParser()
parser.add_argument("-t","--title", help="Enter the title for the html page",default="")
parser.add_argument("-b","--body", help="Enter the body for the html page",default="")
args = parser.parse_args()

title = str(args.title)
body = str(args.body)

f = open("gen.html",'w')
f.write("<html><head><title>"+title+"</title></head><body>"+body+"</body></html>")
f.close()
webbrowser.open("gen.html")
