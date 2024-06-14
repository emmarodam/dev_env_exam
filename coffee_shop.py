import os
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
import psycopg2


logging.basicConfig(level=logging.DEBUG)


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            dbname = os.environ['POSTGRES_DB']
            dbuser = os.environ['POSTGRES_USER']
            dbpass = os.environ['POSTGRES_PASSWORD']
            conn_str = f"host='db' dbname='{dbname}' user='{dbuser}' password='{dbpass}'"

            with psycopg2.connect(conn_str) as connection:
                cursor = connection.cursor()
                cursor.execute('select * from coffee_beans;')
                rows = cursor.fetchall()
                db_data = "\n".join([f"Coffee Bean ID: {row[0]}, Name: {row[1]}," f"Description: {row[2]}, Price: {row[3]}" for row in rows])

            self.send_response(200)
            self.end_headers()
            self.wfile.write(db_data.encode('utf-8'))

        except psycopg2.Error:
            logging.exception("An error occured:")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str.encode("Internal Server Error"))

if __name__ == '__main__':

    print('Serving coffee_shop server on 0.0.0.0:8000')
    httpd = HTTPServer(('0.0.0.0', 8000), HttpHandler)
    httpd.serve_forever()



