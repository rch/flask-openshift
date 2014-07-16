from flask import Response, render_template, current_app, make_response
from datetime import datetime, timedelta
from container import app
from container.tasks import add_together


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/admin")
@app.route("/admin/<int:chk>")
@app.route("/admin.html")
def admin(chk=0):
    return render_template('admin.html', msg=chk)


@app.route("/robots.txt")
def robots():
    """Generate robots.txt. TODO: make allow/disallow rules."""
    robots_txt = render_template('robots.txt')
    response = make_response(robots_txt)
    response.headers["Content-Type"] = 'text/plain'
    
    return response


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago = (datetime.now() - timedelta(days=10)).date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )
      sitemap_xml = render_template('sitemap.xml', pages=pages)
      response = make_response(sitemap_xml)
      response.headers["Content-Type"] = 'text/xml'
      
      return response
