import os

import jinja2

import webapp2

import codecs

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        in_text = self.request.get("text")
        self.render("rot13.html")

    def post(self):
        in_text = self.request.get("text")
        out_text = codecs.encode(in_text, "rot_13")
        self.render("rot13.html", in_text = out_text)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ],
    debug=True)