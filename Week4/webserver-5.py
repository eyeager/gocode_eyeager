'''

Phase Five: DB Support

1) Using "sqlite3 blog.db"
   
    - create a table called posts, which has an id, post_name, post_text
    - add a row to this table, with a post name and post text

2) add the line below - your file must be named blogmodel.py

import blogmodel 

3) Update blog.html template to have two template tags for ###post_name###, ###post_text###

4) Update blog_page(id) to use BlogModel to read, getting back post_name and post_text for a given primary key id

5) Using the data, render blog.html with the right text

Once completed, you should be able to add rows through sqlite3 then go to your webserver:

localhost:8888/blog/1 -> returns a blog post with the data from the first row in the db
localhost:8888/blog/2 -> next row
localhost:8888/blog/... 

   


'''

import sqlite3, socket, re
from blogmodel import BlogModel

HOST, PORT = '', 8888
VIEWS_DIR = "./templates"


#######################
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
    html_template = html_template.replace("###" + key + "###",value)

  return html_template

def page_exist(html_template,content):
	if content:
		context = {"Title":content[0][0],"BlogText":content[0][1]}
		http_response = render_template(html_template, context)
	else:
		http_response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\nERROR: page does not exist"

	return http_response

# Finds the Index page and combines it with template
## Can be combined
def index_page():
  with open("templates/index.html") as html_file:
    content = html_file.read()

  html_template = """\
  HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
  %s
  """ % content
  
  context = {"Owner":"Zoe","Title":"My Cat","BlogText":"She is not happy<br><img src=\"https://scontent-mia1-1.xx.fbcdn.net/hphotos-xtf1/v/t1.0-9/1927919_10152610175091554_4118619071211774019_n.jpg?oh=0312810642371d9f4b2c632436963064&oe=56463899\" alt=\"Baby Zoe\">"}
  http_response = render_template(html_template, context)

  return http_response

# Finds the About page and combines it with template
## Can be combined
def about_page():
  with open("templates/blog.html") as html_file:
    content = html_file.read()

  html_template = """\
  HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
  %s
  """ % content
  
  http_response = page_exist(html_template,blog.read_title("About Me"))

  return http_response

# Finds the all the blog archives and returns html for listing of all existing blogs
## Can be combined
def blog_index_page():
  with open("templates/blog.html") as html_file:
    content = html_file.read()

  html_template = """\
  HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
  %s
  """ % content
  
  http_response = page_exist(html_template,blog.read_title("Blog Archive"))

  return http_response

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
               (r'^.*/html_template.css$',css_template)]
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

        #update and add code here.
        uri = request.split('\r\n')[0].split(" ")[1]
        if uri == "/favicon.ico":
            continue

        http_response = url_dispatch(uri)
        
        #you should not have to change the lines.
        client_connection.sendall(http_response)
        client_connection.close()

run_server()
