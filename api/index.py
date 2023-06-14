from wsgi import app

# dev config
DEV = False
PORT = 5050

# Run app
if (DEV):
    print("Api running on port : {} ".format(PORT))
    app.run(debug=True, port=PORT)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
