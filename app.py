from flask import Flask, request, render_template


def prime_nos_upto(n):
    result = []
    for num in range(2, n):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            result.append(num)
    return result
    


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def getvalues():
    num = request.form["no"]
    result = prime_nos_upto(int(num))
    name = "Aditya"
    return render_template("submit.html",result=result,name = name)


if __name__ == "__main__":
    app.run(debug=True)
