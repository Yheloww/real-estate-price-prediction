from flask import Flask, request, render_template, jsonify
from form import TestForm
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = "password"

infos_dict = {}


@app.route('/', methods=['GET','POST'])
def name():
    form = TestForm()
    infos_dict = {}
    if form.validate_on_submit():
        infos_dict["type_property"] = form.type_property.data
        infos_dict["fire_place"] = form.fire_place.data
        infos_dict["Number_bedrooms"] = form.number_bedroom.data
        return jsonify(list(infos_dict))
    return render_template("form.html",
                            form=form)


if __name__ == '__main__':
    app.run(port=5000, debug=True)