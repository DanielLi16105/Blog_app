from flask import Flask
app = Flask(__name__)

#Routs

# Rout for homepge
@app.route("/") #route to main page
@app.route("/home") #Rout to home page
def home():
    return render_template('home.html', posts=posts) # call to render the home page template

# Rout for about page
@app.route("/about")
def about():
    return render_template('about.html')

# Allows main app to run the web server
if __name__=='__main__':
    app.run(debug=True)
