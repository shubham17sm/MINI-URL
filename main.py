from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi, sys, string, random, time
import mysql.connector

count = 1

try:
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password= "root",
    database="url_shortner"
    )
    mycursor = mydb.cursor()
    connection_status = True
    print("Successfully connected to database")
except Exception as databaseerr:
    print("Connection to database failed")
    print("Error: ", databaseerr)
    time.sleep(2)


collect_url = []

def randomStringGenerator():
    S = 5
    ran = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = S))
    try:
        mycursor.execute("""SELECT short_url FROM urlshort WHERE short_url = %s LIMIT 1;""", (ran,))
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            print("No results found in DB for short URL")
            return ran
    except:
        print("created new random string for short url", ran)
        return ran
    

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            route_path = self.path.split('/')[1]
            if self.path.endswith("/"):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                with open('Templates\index.html', 'r', encoding='UTF-8') as html_file:
                    output = html_file.read()
                self.wfile.write(output.encode('UTF-8'))
                # print(output)
                return
            elif self.path.endswith("/display"):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                new_mini_url = collect_url[-1]
                random_code = new_mini_url.split('/')[1]
                html = f"<html>\
                <head></head>\
                <body>\
                <h1>Short URL generated: <a href='/{random_code}' target='_blank'>{new_mini_url}</a></h1></br>\
                <h5><a href='http://127.0.0.1:8000'> Return to Homepage</a></h5>\
                </body>\
                </html>"

                # Writing the HTML contents with UTF-8
                self.wfile.write(bytes(html, "utf8"))
                # print(output)
                return
            else:
                mycursor.execute("""SELECT id, long_url, short_url FROM urlshort WHERE short_url = %s ORDER BY id DESC LIMIT 1;""", (route_path,))
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    longer_url = x[1]
                    shorter_url = x[2]

                    #if self.path matches with above query (if short URL available in db) then redirect it to long url.
                    if route_path == shorter_url:
                        self.send_response(301)
                        self.send_header('Location',longer_url)
                        self.end_headers()
                    else:
                        return self.send_error(404, "Non such URL found")
        except IOError:
            self.send_error(404, "File not found %s" % self.path)


    def do_POST(self):
        try:
            if self.path.endswith('/'):
                self.send_response(301)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Location', '/display')
                self.end_headers()

                ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
                # print(ctype, pdict)
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                content_len = int(self.headers.get('Content-length'))
                pdict['CONTENT-LENGTH'] = content_len
                if ctype == "multipart/form-data":
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
                    long_url_from_user = messagecontent[0]
                    # print(long_url_from_user)

                random_url_string = randomStringGenerator()
                if random_url_string is not None:
                    collect_url.append(f'127.0.0.1:8000/{random_url_string}')
                    mycursor.execute("""INSERT INTO urlshort(long_url, short_url) VALUES(%s, %s);""", (long_url_from_user, random_url_string))
                    mydb.commit()
                    print(f"User URL: {long_url_from_user}, generated short url: {random_url_string} values inserted in database")
                    print(collect_url[-1])
        except:
            self.send_error(404, "{}".format(sys.exc_info()[0]))
            print(sys.exc_info())
