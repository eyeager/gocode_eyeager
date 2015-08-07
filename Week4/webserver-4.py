'''

Phase four: Refactor urls

We want to move away from exact string matching, or having to write a special parser for each url. Changing it to use regex allows us to add complex url handling and pull out data to pass along easily.


1) Add this,


urlpatterns = [(r'^/$',index_page),
               (r'^/about$',about_page),
               (r'^/blog$',blog_index_page),
               (r'^/blog/(\d+)',blog_page)]

def blog_index_page():
    pass

def blog_page(id):
    pass

   - create a blog_index.html with some basic html
  
   - create a blog.html with basic html

2) Write a function url_dispatch(url) where url is the http file name request

   - this function loops through urlpatterns using re.match and urlpatterns[0]

   - if a match if found it calls the matching function

   - if a pattern has a grouping like /blog/(\d+) you pass the first group item to the function

   Ex: a request for /blog comes in the regular expressions matches the third url patter, so blog_index_page is called

'''

import re,socket

HOST, PORT = '', 8888
VIEWS_DIR = "./templates"

def url_dispatch(url):
  for pattern,function in urlpatterns:
    rm = re.match(pattern,url)
    if rm:
      if rm.groups():
        return function(rm.groups())
      else:
        return function()

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
  
  context = {"Owner":"Emilie","Title":"My Cat","BlogText":"She is not happy<br><img src=\"https://scontent-mia1-1.xx.fbcdn.net/hphotos-xtf1/v/t1.0-9/1927919_10152610175091554_4118619071211774019_n.jpg?oh=0312810642371d9f4b2c632436963064&oe=56463899\" alt=\"Baby Zoe\">"}
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

def blog_index_page():
    pass

def blog_page(id):
    pass

def css_template():
  with open("templates/html_template.css") as html_file:
    content = html_file.read()

  http_response = """\
  HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n
  %s
  """ % content
  return http_response

urlpatterns = [(r'^/$',index_page),
               (r'^/about$',about_page),
               (r'^/blog$',blog_index_page),
               (r'^/blog/(\d+)',blog_page),
               (r'^/html_template.css$',css_template)]

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

        http_response = url_dispatch(uri)
        
        #you should not have to change the lines.
        client_connection.sendall(http_response)
        client_connection.close()

run_server()