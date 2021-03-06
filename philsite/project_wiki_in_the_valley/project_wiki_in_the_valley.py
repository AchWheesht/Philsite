from philsite import app, render_template, request, json, send_from_directory
import philsite.project_wiki_in_the_valley.valley_generator as valley_generator
import os

wiki_in_use = False

dir_name ="project_wiki_in_the_valley/"
app_dir = os.getcwd()
static_dir = app_dir + "/philsite/project_wiki_in_the_valley/static"

@app.route("/wiki_static/<path:filename>")
def wiki_static(filename):
    return send_from_directory(static_dir, filename)

@app.route("/wiki_in_the_valley_o")
def wiki_in_the_valley_o():
    return render_template(dir_name+"templates/template_in_the_valley_o.html")

@app.route("/wiki_in_the_valley_o/get_song", methods=["POST"])
def get_song():
    global wiki_in_use
    # print("INVOKED")
    url = request.form["url"]
    # print(url[:25])
    if url[:24] != "https://en.wikipedia.org" and url[:25] != "https://www.wikipedia.org":
        return json.dumps(("use a wikipedia url!", "use a wikipedia url!"))
    while True:
        if wiki_in_use == True:
            print("In use, waiting...")
            time.sleep(1)
        elif wiki_in_use == False:
            wiki_in_use = True
            break
    list_and_song = valley_generator.make_a_song(url)
    wiki_in_use = False
    # print("List:\n\n", list_and_song[0])
    # print("Song:\n\n", list_and_song[1])
    list_and_song[0] = list_to_string(list_and_song[0])
    response = json.dumps(list_and_song)
    return response

@app.route("/wiki_in_the_valley_o/about")
def about_wiki():
    return render_template(dir_name+"templates/about_wiki.html")

def list_to_string(the_list):
    string = ""
    for item in the_list:
        string += item
        string += "\n"
    return string
