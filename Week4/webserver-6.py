'''

Phase Six: Form Support


1) Add a new html file into views called "new_post.html"

   - add a html form to the page

   - the form has inputs, post_name and post_text

   - add a submit input

   - This doc has good guidlines for forms: http://learn.shayhowe.com/html-css/building-forms/

2) Add a new action for 'blog/new' tied to blog_new

   - renders the new_post.html

3) Update the form url in new_post.html to <form action="/blog/create" method="post">

4) Add a new action for 'blog/create' tied to blog_create

   - have it return blog_index_page

5) Refactor the functions blog_index, blog_create... 

   - to accept the body of the http request

6) Write a new helper function called process_form 
 
   - it takes the http request body parses the form line from the end of body

   Ex: 'post_name=test&post_text=test'

   - and returns a hash {'post_name':'test','post_text':'test'}

7) Use process_form in blog_create to create a new row in the db using BlogModel

'''

import sqlite3, socket, re, urllib
from blogmodel import BlogModel

HOST, PORT = '', 8888
VIEWS_DIR = "./templates"


#######################
def url_dispatch(url,request):
  for pattern,function in urlpatterns:
    rm = re.match(pattern,url)
    http_get = request.split('\n')[-1]
    if rm:
      if rm.groups():
        return function(rm.groups())
      elif http_get:
        return function(http_get)
      else:
        return function()

def render_template(html_template,context):
  for key,value in context.iteritems():
    html_template = html_template.replace("###" + key + "###",value)

  return html_template

def page_exist(html_template,content):
   if content:
      context = {"Title":content[0][0],"BlogText":content[0][1]}
      http_response = render_template(html_template, context)
   else:
      http_response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\nERROR: page does not exist"

   return http_response

# To find page in DB the combine content with html template
def get_page(page_name):
  with open("templates/blog.html") as html_file:
    content = html_file.read()

  html_template = """\
  HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
  %s
  """ % content
  
  http_response = page_exist(html_template,blog.read_title(page_name))

  return http_response

def process_form(http_request):
  post_dict = {}
  regex = r"^(\w+)=(\d{4}-\d{2}-\d{2})&(\w+)=(\w+)&(\w+)=(.*)&submit=Post$"
  post_data = re.findall(regex,http_request)

  for array in post_data:
    for i in range(0,len(array),2):
      post_dict[array[i]] = array[i+1]
  post_dict["post_text"] = urllib.unquote(post_dict["post_text"]).replace('+',' ').replace('\n','<br>\n')

  return post_dict

# Finds the Index page and combines it with template
def index_page():
  return get_page("Home")

# Finds the About page and combines it with template
def about_page():
  return get_page("About Me")

# Finds the all the blog archives and returns html for listing of all existing blogs
def blog_index_page():
  
  #return get_page("Blog Archive")
  return get_page("Home")

# Finds the blog data in the database and combines it with the template
def blog_page(id):
  with open("templates/blog.html") as html_file:
    content = html_file.read()

  html_template = """\
  HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
  %s
  """ % content

  http_response = page_exist(html_template,blog.read("".join(id)))

  return http_response

def blog_new():
  with open("templates/new_post.html") as html_file:
    content = html_file.read()
  
  html_template = """\
  HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
  %s
  """ % content

  return html_template

def blog_create(request):

  request = process_form(request)
  blog.insert(request["post_name"],request["post_text"])
  return blog_index_page()

# Returns the css_template
def css_template():
  with open("templates/html_template.css") as html_file:
    content = html_file.read()

  http_response = """\
  HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n
  %s
  """ % content
  return http_response

############### Globals ###################
blog = BlogModel("blog.db","posts")

# Must be after functions are declared
urlpatterns = [(r'^/$',index_page),
               (r'^/about$',about_page),
               (r'^/blog$',blog_index_page),
               (r'^/blog/(\d+)',blog_page),
               (r'^.*/html_template.css$',css_template),
               (r'^/blog/new$',blog_new),
               (r'^/blog/create$',blog_create)]

###########################################

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

        uri = request.split('\r\n')[0].split(" ")[1]
        if uri == "/favicon.ico":
            continue

        http_response = url_dispatch(uri,request)
        
        #you should not have to change the lines.
        client_connection.sendall(http_response)
        client_connection.close()

run_server()
