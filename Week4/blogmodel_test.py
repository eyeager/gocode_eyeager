from blogmodel import BlogModel

blog = BlogModel("testblog.db")

blog.insert("A title","Some words")

print blog.read(1)

blog.close()