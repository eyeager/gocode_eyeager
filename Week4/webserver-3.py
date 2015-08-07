'''

Phase three: Templating

Templating allows a program to replace data dynamically in an html file. 

Ex: A blog page:, we wouldn't write a whole new html file for every blog page. We want to write the html part and styling just once, then just inject the different blog text into that page. 

In the last exercise, we added a piece of python code that got called when a request came in.  Ex: a request for / would call a function to handle that request and return html. 

By doing this, it allows us to change the html on the fly, and return a blog post with updated values.

Ex: When a request comes in for index (/), our index_page() function gets called and does the following:
   
   - read the file data for index.html 

   - change the ###Title### string to the string "This is templating"
  
   - return the changed html string 

Steps:

1) Add the following line to index.html in the body

<h2>###Title###</h2>

2) Write a function render_template to take an html template, and a hash called context. 

   render_template takes the html data as a string from the file and returns that string so that you can swap it out for the http_response variable.

   Ex: render_template("<html>...",{"Title":"This is templating"})

   - Render will the try to replace all the fields in that hash

   Ex: context = {"Title":"This is the title","BlogText":"this is blog data"}

   In the html template replace ###Title### and ###BlogText### with corresponding key values.

   - Test by using this context {"Title":"This is the title","BlogText":"this is blog data"}

3) Add render_template to index_page with the sample context above

'''

import socket


HOST, PORT = '', 8888
VIEWS_DIR = "./templates"

def render_template(html_template,context):

	for key,value in context.iteritems():
		key = "###" + key + "###"
		html_template = html_template.replace(key,value)

	return html_template

def index_page():

	with open("templates/index.html") as html_file:
		content = html_file.read()

	html_template = """\
	HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
	%s
	""" % content
	
	context = {"Owner":"Emilie","Title":"My Cat","BlogText":"She is not happy<br><img src=\"\" alt=\"Baby Zoe\">"}
	http_response = render_template(html_template, context)

	return http_response

def about_page():
	with open("templates/about.html") as html_file:
		content = html_file.read()

	http_response = """\
	HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
	%s
	""" % content
	return http_response

def cat_page():
	with open("templates/cat.html") as html_file:
		content = html_file.read()

	http_response = """\
	HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
	%s
	""" % content
	return http_response

def css_template():
	with open("templates/html_template.css") as html_file:
		content = html_file.read()

	http_response = """\
	HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n
	%s
	""" % content
	return http_response

def run_server():
    ''' 
    **** You don't need to change the lines below
    **** These lines allow you to accept connections through a web browser.
    **** If you do want to read more you can look at https://docs.python.org/2/howto/sockets.html
    '''
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)

    urls = {
    	"/" : index_page,
    	"/about" : about_page,
    	"/cat" : cat_page,
    	"/html_template.css" : css_template
    }
 
    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(4096)
        if not request:
            continue

        #update and add code here.
        uri = request.split('\r\n')[0].split(" ")[1]
        if uri == "/favicon.ico":
            continue

        if urls.has_key(uri):
        	http_response = urls[uri]()
        else:
        		http_response = """\
	HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n
	404 Not Found
	"""
        
        #you should not have to change the lines.
        client_connection.sendall(http_response)
        client_connection.close()

run_server()