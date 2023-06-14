from wsgi import app

PORT = 5100
DEV = False

# Run app
if (DEV):
    app.run(debug=True, port=5050)

if __name__ == '__main__':
    print("Api running on port : {} ".format(PORT))
    app.run(host="0.0.0.0", port=PORT)
