from flask import Flask, request, render_template, jsonify, url_for,redirect
from form import TestForm
import json
from predict.prediction import predict
app = Flask(__name__)
app.config['SECRET_KEY'] = "password"

infos_dict = {}


@app.route('/', methods=['GET', 'POST'])
def name():
    form = TestForm()
    infos_dict = {}
    if form.validate_on_submit():
        json_data = {
            "type_property_" + form.type_property.data : form.type_property.data,
            "number_bedrooms": form.number_bedroom.data,
            "living_area": form.living_area.data,
            "fully_equipped_kitchen": form.kitchen.data,
            "furnished": form.furnished.data,
            "terrace": form.terrace.data,
            "garden": form.garden.data,
            "facades_number": form.facades_number.data,
            "swimming_pool": form.swim.data,
            "fire_place": form.fire_place.data,
            "provinces_" + form.provinces.data : form.provinces.data,
            "building_state_" + form.building_state.data : form.building_state.data,

        }
        with open("./sample.json", "w") as outfile:
            json.dump(json_data, outfile)

        return redirect(url_for('predicte'))

    return render_template("test.html",
                            form=form)

@app.route('/predicte', methods=['GET','POST'])
def predicte():
    path = "./sample.json"
    infos = int(predict(path))
    return render_template('results.html', infos=infos)



if __name__ == '__main__':
    app.run(port=5000, debug=True)