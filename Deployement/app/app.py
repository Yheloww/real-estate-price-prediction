from flask import Flask, render_template, url_for, redirect
from form import TestForm
import json
from predict.prediction import predict

app = Flask(__name__)

app.config['SECRET_KEY'] = "password"


@app.route('/', methods=['GET', 'POST'])
def name():
    """
    base route of the  application 
    by default it render the form 
    when the form is submitted it create a dict of infos in a json file 
    then it redirect the user to the next route predicte
    """
    form = TestForm()
    # when the user submit the form
    if form.validate_on_submit():
        json_data = {
            "type_property_" + form.type_property.data: form.type_property.data,
            "number_bedrooms": form.number_bedroom.data,
            "living_area": form.living_area.data,
            "fully_equipped_kitchen": form.kitchen.data,
            "furnished": form.furnished.data,
            "terrace": form.terrace.data,
            "garden": form.garden.data,
            "facades_number": form.facades_number.data,
            "swimming_pool": form.swim.data,
            "fire_place": form.fire_place.data,
            "provinces_" + form.provinces.data: form.provinces.data,
            "building_state_" + form.building_state.data: form.building_state.data,
        }
        # creation of a json file
        with open("./sample.json", "w") as outfile:
            json.dump(json_data, outfile)
        # redirecting the user to the predicte route
        return redirect(url_for('predicte'))
    # by default it render the form
    return render_template("form.html",
                           form=form)


@app.route('/predicte', methods=['GET', 'POST'])
def predicte():
    """
    this route display the result of the prediction 
    it feeds the json to the predict function 
    it sends back the estimated price and print it on the screen
    """
    path = "./sample.json"
    infos = int(predict(path))
    return render_template('results.html', infos=infos)


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
